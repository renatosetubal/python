import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import sys
from tkinter.font import Font
import ldap
import configparser
import threading
import logging
from datetime import datetime

# Configuração de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='ad_manager.log',
    filemode='a'
)
logger = logging.getLogger('ADManager')

class ADManager:
    """Classe principal para gerenciar operações com o Active Directory."""
    
    def __init__(self, server, base_dn, username, password):
        """Inicializa a conexão com o Active Directory."""
        self.server = server
        self.base_dn = base_dn
        self.username = username
        self.password = password
        self.conn = None
        
    def connect(self):
        """Estabelece conexão com o servidor AD."""
        try:
            # Inicializa a conexão LDAP
            ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
            ldap.set_option(ldap.OPT_REFERRALS, 0)
            
            self.conn = ldap.initialize(self.server)
            self.conn.protocol_version = 3
            self.conn.set_option(ldap.OPT_REFERRALS, 0)
            
            # Autenticação
            self.conn.simple_bind_s(self.username, self.password)
            logger.info("Conexão com AD estabelecida com sucesso")
            return True
        except ldap.LDAPError as e:
            logger.error(f"Erro ao conectar ao AD: {str(e)}")
            return False
    
    def search_users(self, search_filter):
        """Pesquisa usuários no AD com base no filtro especificado."""
        try:
            if not self.conn:
                if not self.connect():
                    return []
            
            search_attrs = ['cn', 'sAMAccountName', 'mail', 'department', 'title', 'memberOf']
            search_scope = ldap.SCOPE_SUBTREE
            
            # Construir filtro LDAP
            if search_filter:
                ldap_filter = f"(&(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(|(cn=*{search_filter}*)(sAMAccountName=*{search_filter}*)(mail=*{search_filter}*)))"
            else:
                ldap_filter = "(&(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
            
            result = self.conn.search_s(self.base_dn, search_scope, ldap_filter, search_attrs)
            
            users = []
            for dn, attrs in result:
                if dn:  # Ignorar entradas vazias
                    user = {
                        'dn': dn,
                        'username': attrs.get('sAMAccountName', [b''])[0].decode('utf-8'),
                        'name': attrs.get('cn', [b''])[0].decode('utf-8'),
                        'email': attrs.get('mail', [b''])[0].decode('utf-8') if 'mail' in attrs else '',
                        'department': attrs.get('department', [b''])[0].decode('utf-8') if 'department' in attrs else '',
                        'title': attrs.get('title', [b''])[0].decode('utf-8') if 'title' in attrs else '',
                        'groups': [g.decode('utf-8') for g in attrs.get('memberOf', [])]
                    }
                    users.append(user)
            
            logger.info(f"Pesquisa retornou {len(users)} usuários")
            return users
        except ldap.LDAPError as e:
            logger.error(f"Erro na pesquisa de usuários: {str(e)}")
            return []
    
    def search_groups(self, search_filter):
        """Pesquisa grupos no AD com base no filtro especificado."""
        try:
            if not self.conn:
                if not self.connect():
                    return []
            
            search_attrs = ['cn', 'description', 'member', 'distinguishedName']
            search_scope = ldap.SCOPE_SUBTREE
            
            # Construir filtro LDAP
            if search_filter:
                ldap_filter = f"(&(objectClass=group)(|(cn=*{search_filter}*)(description=*{search_filter}*)))"
            else:
                ldap_filter = "(objectClass=group)"
            
            result = self.conn.search_s(self.base_dn, search_scope, ldap_filter, search_attrs)
            
            groups = []
            for dn, attrs in result:
                if dn:  # Ignorar entradas vazias
                    group = {
                        'dn': dn,
                        'name': attrs.get('cn', [b''])[0].decode('utf-8'),
                        'description': attrs.get('description', [b''])[0].decode('utf-8') if 'description' in attrs else '',
                        'members': [m.decode('utf-8') for m in attrs.get('member', [])]
                    }
                    groups.append(group)
            
            logger.info(f"Pesquisa retornou {len(groups)} grupos")
            return groups
        except ldap.LDAPError as e:
            logger.error(f"Erro na pesquisa de grupos: {str(e)}")
            return []
    
    def create_user(self, user_data):
        """Cria um novo usuário no AD."""
        try:
            if not self.conn:
                if not self.connect():
                    return False, "Falha na conexão com o AD"
            
            # Preparar atributos do usuário
            user_dn = f"CN={user_data['name']},{user_data['ou']}"
            attrs = [
                ('objectClass', [b'top', b'person', b'organizationalPerson', b'user']),
                ('cn', [user_data['name'].encode('utf-8')]),
                ('sAMAccountName', [user_data['username'].encode('utf-8')]),
                ('userPrincipalName', [f"{user_data['username']}@{user_data['domain']}".encode('utf-8')]),
                ('givenName', [user_data['first_name'].encode('utf-8')]),
                ('sn', [user_data['last_name'].encode('utf-8')])
            ]
            
            if 'email' in user_data and user_data['email']:
                attrs.append(('mail', [user_data['email'].encode('utf-8')]))
            
            if 'department' in user_data and user_data['department']:
                attrs.append(('department', [user_data['department'].encode('utf-8')]))
            
            if 'title' in user_data and user_data['title']:
                attrs.append(('title', [user_data['title'].encode('utf-8')]))
            
            # Adicionar usuário
            self.conn.add_s(user_dn, attrs)
            
            # Definir senha e habilitar conta
            self.conn.modify_s(user_dn, [
                (ldap.MOD_REPLACE, 'unicodePwd', 
                 ('"%s"' % user_data['password']).encode('utf-16-le')),
                (ldap.MOD_REPLACE, 'userAccountControl', [b'512'])  # Conta normal e ativa
            ])
            
            logger.info(f"Usuário {user_data['username']} criado com sucesso")
            return True, "Usuário criado com sucesso"
        except ldap.LDAPError as e:
            error_msg = str(e)
            logger.error(f"Erro ao criar usuário: {error_msg}")
            return False, f"Erro ao criar usuário: {error_msg}"
    
    def modify_user(self, dn, attributes):
        """Modifica atributos de um usuário existente."""
        try:
            if not self.conn:
                if not self.connect():
                    return False, "Falha na conexão com o AD"
            
            mod_attrs = []
            for attr_name, attr_value in attributes.items():
                if attr_value:
                    mod_attrs.append((ldap.MOD_REPLACE, attr_name, attr_value.encode('utf-8')))
            
            if mod_attrs:
                self.conn.modify_s(dn, mod_attrs)
                logger.info(f"Usuário {dn} modificado com sucesso")
                return True, "Usuário modificado com sucesso"
            else:
                return False, "Nenhum atributo para modificar"
        except ldap.LDAPError as e:
            error_msg = str(e)
            logger.error(f"Erro ao modificar usuário: {error_msg}")
            return False, f"Erro ao modificar usuário: {error_msg}"
    
    def create_group(self, group_data):
        """Cria um novo grupo no AD."""
        try:
            if not self.conn:
                if not self.connect():
                    return False, "Falha na conexão com o AD"
            
            group_dn = f"CN={group_data['name']},{group_data['ou']}"
            attrs = [
                ('objectClass', [b'top', b'group']),
                ('cn', [group_data['name'].encode('utf-8')]),
                ('sAMAccountName', [group_data['name'].encode('utf-8')])
            ]
            
            if 'description' in group_data and group_data['description']:
                attrs.append(('description', [group_data['description'].encode('utf-8')]))
            
            # Adicionar grupo
            self.conn.add_s(group_dn, attrs)
            
            logger.info(f"Grupo {group_data['name']} criado com sucesso")
            return True, "Grupo criado com sucesso"
        except ldap.LDAPError as e:
            error_msg = str(e)
            logger.error(f"Erro ao criar grupo: {error_msg}")
            return False, f"Erro ao criar grupo: {error_msg}"
    
    def add_user_to_group(self, user_dn, group_dn):
        """Adiciona um usuário a um grupo."""
        try:
            if not self.conn:
                if not self.connect():
                    return False, "Falha na conexão com o AD"
            
            # Modificar o grupo para adicionar o usuário como membro
            self.conn.modify_s(group_dn, [(ldap.MOD_ADD, 'member', user_dn.encode('utf-8'))])
            
            logger.info(f"Usuário {user_dn} adicionado ao grupo {group_dn}")
            return True, "Usuário adicionado ao grupo com sucesso"
        except ldap.LDAPError as e:
            error_msg = str(e)
            logger.error(f"Erro ao adicionar usuário ao grupo: {error_msg}")
            return False, f"Erro ao adicionar usuário ao grupo: {error_msg}"
    
    def remove_user_from_group(self, user_dn, group_dn):
        """Remove um usuário de um grupo."""
        try:
            if not self.conn:
                if not self.connect():
                    return False, "Falha na conexão com o AD"
            
            # Modificar o grupo para remover o usuário como membro
            self.conn.modify_s(group_dn, [(ldap.MOD_DELETE, 'member', user_dn.encode('utf-8'))])
            
            logger.info(f"Usuário {user_dn} removido do grupo {group_dn}")
            return True, "Usuário removido do grupo com sucesso"
        except ldap.LDAPError as e:
            error_msg = str(e)
            logger.error(f"Erro ao remover usuário do grupo: {error_msg}")
            return False, f"Erro ao remover usuário do grupo: {error_msg}"
    
    def disconnect(self):
        """Encerra a conexão com o servidor AD."""
        if self.conn:
            self.conn.unbind_s()
            self.conn = None
            logger.info("Conexão com AD encerrada")


class Config:
    """Classe para gerenciar a configuração do aplicativo."""
    
    def __init__(self, config_file='config.ini'):
        """Inicializa o gerenciador de configuração."""
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        
        if os.path.exists(config_file):
            self.config.read(config_file)
        else:
            self._create_default_config()
    
    def _create_default_config(self):
        """Cria um arquivo de configuração padrão."""
        self.config['AD'] = {
            'server': 'ldap://your-domain-controller.example.com',
            'base_dn': 'DC=example,DC=com',
            'username': 'CN=Administrator,CN=Users,DC=example,DC=com',
            'password': '',
            'default_ou': 'CN=Users,DC=example,DC=com'
        }
        
        self.config['APP'] = {
            'theme': 'sistema',
            'language': 'pt_BR',
            'save_credentials': 'False'
        }
        
        with open(self.config_file, 'w') as f:
            self.config.write(f)
    
    def get(self, section, option, fallback=None):
        """Obtém um valor de configuração."""
        return self.config.get(section, option, fallback=fallback)
    
    def set(self, section, option, value):
        """Define um valor de configuração."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        
        self.config.set(section, option, value)
        
        with open(self.config_file, 'w') as f:
            self.config.write(f)


class App(tk.Tk):
    """Classe principal do aplicativo."""
    
    def __init__(self):
        """Inicializa a aplicação."""
        super().__init__()
        
        self.title("Gerenciador de Active Directory")
        self.geometry("1024x768")
        self.minsize(800, 600)
        
        # Carregar configurações
        self.config = Config()
        
        # Configurar tema
        self.style = ttk.Style()
        self.configure_theme()
        
        # Inicialização de variáveis
        self.ad_manager = None
        self.current_frame = None
        
        # Criar menu
        self.create_menu()
        
        # Criar frame principal
        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Mostrar tela de login
        self.show_login_frame()
    
    def configure_theme(self):
        """Configura o tema da aplicação."""
        theme = self.config.get('APP', 'theme', fallback='sistema')
        
        if theme == 'claro':
            self.style.theme_use('clam')
            self.style.configure('TFrame', background='#f0f0f0')
            self.style.configure('TLabel', background='#f0f0f0')
            self.style.configure('TButton', background='#e0e0e0')
            self.style.configure('TEntry', background='#ffffff')
            self.style.configure('TNotebook', background='#f0f0f0')
            self.style.configure('TNotebook.Tab', background='#e0e0e0', padding=[10, 2])
        elif theme == 'escuro':
            self.style.theme_use('clam')
            self.style.configure('TFrame', background='#2e2e2e')
            self.style.configure('TLabel', background='#2e2e2e', foreground='#ffffff')
            self.style.configure('TButton', background='#3e3e3e')
            self.style.configure('TEntry', fieldbackground='#3e3e3e', foreground='#ffffff')
            self.style.configure('TNotebook', background='#2e2e2e')
            self.style.configure('TNotebook.Tab', background='#3e3e3e', foreground='#ffffff', padding=[10, 2])
        else:
            # Tema do sistema (default)
            available_themes = self.style.theme_names()
            if 'vista' in available_themes:
                self.style.theme_use('vista')
            elif 'winnative' in available_themes:
                self.style.theme_use('winnative')
            else:
                self.style.theme_use('clam')
    
    def create_menu(self):
        """Cria o menu da aplicação."""
        menubar = tk.Menu(self)
        
        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Conectar ao AD", command=self.show_login_frame)
        file_menu.add_command(label="Configurações", command=self.show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        
        # Menu Usuários
        users_menu = tk.Menu(menubar, tearoff=0)
        users_menu.add_command(label="Pesquisar Usuários", command=self.show_user_search_frame)
        users_menu.add_command(label="Novo Usuário", command=self.show_user_create_frame)
        menubar.add_cascade(label="Usuários", menu=users_menu)
        
        # Menu Grupos
        groups_menu = tk.Menu(menubar, tearoff=0)
        groups_menu.add_command(label="Pesquisar Grupos", command=self.show_group_search_frame)
        groups_menu.add_command(label="Novo Grupo", command=self.show_group_create_frame)
        menubar.add_cascade(label="Grupos", menu=groups_menu)
        
        # Menu Ajuda
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Manual", command=self.show_manual)
        help_menu.add_command(label="Sobre", command=self.show_about)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        
        self.config(menu=menubar)
        self.menubar = menubar
    
    def show_frame(self, frame_class):
        """Exibe um frame na janela principal."""
        # Remover frame atual
        if self.current_frame:
            self.current_frame.destroy()
        
        # Criar e mostrar novo frame
        self.current_frame = frame_class(self.main_container, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_login_frame(self):
        """Exibe o frame de login."""
        self.show_frame(LoginFrame)
    
    def show_user_search_frame(self):
        """Exibe o frame de pesquisa de usuários."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        self.show_frame(UserSearchFrame)
    
    def show_user_create_frame(self):
        """Exibe o frame de criação de usuário."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        self.show_frame(UserCreateFrame)
    
    def show_user_details_frame(self, user_data):
        """Exibe o frame de detalhes do usuário."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        
        # Remover frame atual
        if self.current_frame:
            self.current_frame.destroy()
        
        # Criar e mostrar frame de detalhes
        self.current_frame = UserDetailsFrame(self.main_container, self, user_data)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_group_search_frame(self):
        """Exibe o frame de pesquisa de grupos."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        self.show_frame(GroupSearchFrame)
    
    def show_group_create_frame(self):
        """Exibe o frame de criação de grupo."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        self.show_frame(GroupCreateFrame)
    
    def show_group_details_frame(self, group_data):
        """Exibe o frame de detalhes do grupo."""
        if not self.ad_manager:
            messagebox.showwarning("Aviso", "Você precisa se conectar ao AD primeiro.")
            self.show_login_frame()
            return
        
        # Remover frame atual
        if self.current_frame:
            self.current_frame.destroy()
        
        # Criar e mostrar frame de detalhes
        self.current_frame = GroupDetailsFrame(self.main_container, self, group_data)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_settings(self):
        """Exibe o frame de configurações."""
        self.show_frame(SettingsFrame)
    
    def show_manual(self):
        """Exibe o manual do aplicativo."""
        messagebox.showinfo("Manual", "O manual está disponível em: https://exemplo.com/manual")
    
    def show_about(self):
        """Exibe informações sobre o aplicativo."""
        messagebox.showinfo("Sobre", "Gerenciador de Active Directory v1.0\n\nUm aplicativo Python com Tkinter para gerenciar usuários e grupos no Active Directory.")
    
    def connect_to_ad(self, server, base_dn, username, password):
        """Conecta ao servidor Active Directory."""
        try:
            self.ad_manager = ADManager(server, base_dn, username, password)
            
            # Executar conexão em uma thread separada com timeout
            def connect_thread():
                return self.ad_manager.connect()
            
            thread = threading.Thread(target=connect_thread)
            thread.daemon = True
            thread.start()
            thread.join(timeout=5)  # Timeout de 5 segundos
            
            if thread.is_alive():
                # Timeout ocorreu
                messagebox.showerror("Erro de Conexão", "Timeout ao tentar conectar ao servidor AD.")
                self.ad_manager = None
                return False
            
            # Verificar se conexão foi bem-sucedida
            if not self.ad_manager.conn:
                messagebox.showerror("Erro de Conexão", "Falha ao conectar ao servidor AD.")
                self.ad_manager = None
                return False
            
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao AD: {str(e)}")
            self.ad_manager = None
            return False


class LoginFrame(ttk.Frame):
    """Frame de login para conexão ao Active Directory."""
    
    def __init__(self, parent, controller):
        """Inicializa o frame de login."""
        super().__init__(parent)
        self.controller = controller
        
        # Carregar configurações
        self.server = tk.StringVar(value=controller.config.get('AD', 'server'))
        self.base_dn = tk.StringVar(value=controller.config.get('AD', 'base_dn'))
        self.username = tk.StringVar(value=controller.config.get('AD', 'username'))
        self.password = tk.StringVar()
        self.save_credentials = tk.BooleanVar(value=controller.config.get('APP', 'save_credentials') == 'True')
        
        # Carregar senha salva, se disponível
        if self.save_credentials.get():
            saved_password = controller.config.get('AD', 'password', fallback='')
            if saved_password:
                self.password.set(saved_password)
        
        # Criar widgets
        self.create_widgets()
    
    def create_widgets(self):
        """Cria os widgets do frame de login."""
        # Título
        title_label = ttk.Label(self, text="Conectar ao Active Directory", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # Frame para formulário
        form_frame = ttk.Frame(self)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=50)
        
        # Servidor
        server_label = ttk.Label(form_frame, text="Servidor LDAP:")
        server_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        server_entry = ttk.Entry(form_frame, textvariable=self.server, width=40)
        server_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Base DN
        base_dn_label = ttk.Label(form_frame, text="Base DN:")
        base_dn_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        base_dn_entry = ttk.Entry(form_frame, textvariable=self.base_dn, width=40)
        base_dn_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Usuário
        username_label = ttk.Label(form_frame, text="Usuário:")
        username_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        username_entry = ttk.Entry(form_frame, textvariable=self.username, width=40)
        username_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Senha
        password_label = ttk.Label(form_frame, text="Senha:")
        password_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        password_entry = ttk.Entry(form_frame, textvariable=self.password, show="*", width=40)
        password_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Checkbox para salvar credenciais
        save_check = ttk.Checkbutton(form_frame, text="Salvar credenciais", variable=self.save_credentials)
        save_check.grid(row=4, column=1, sticky=tk.W, pady=10)
        
        # Botões
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=20)
        
        connect_button = ttk.Button(button_frame, text="Conectar", command=self.connect)
        connect_button.pack(side=tk.RIGHT, padx=10)
        
        # Adicionar evento de Enter para conectar
        self.bind_all("<Return>", lambda event: self.connect())
    
    def connect(self):
        """Tenta conectar ao servidor AD com as credenciais fornecidas."""
        # Obter valores dos campos
        server = self.server.get()
        base_dn = self.base_dn.get()
        username = self.username.get()
        password = self.password.get()
        
        # Validar campos
        if not server or not base_dn or not username or not password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        # Tentar conectar
        if self.controller.connect_to_ad(server, base_dn, username, password):
            # Salvar configurações se checkbox marcado
            if self.save_credentials.get():
                self.controller.config.set('AD', 'server', server)
                self.controller.config.set('AD', 'base_dn', base_dn)
                self.controller.config.set('AD', 'username', username)
                self.controller.config.set('AD', 'password', password)
                self.controller.config.set('APP', 'save_credentials', 'True')
            else:
                self.controller.config.set('AD', 'server', server)
                self.controller.config.set('AD', 'base_dn', base_dn)
                self.controller.config.set('AD', 'username', username)
                self.controller.config.set('AD', 'password', '')
                self.controller.config.set('APP', 'save_credentials', 'False')
            
            # Mostrar tela de pesquisa de usuários
            self.controller.show_user_search_frame()
            messagebox.showinfo("Sucesso", "Conexão estabelecida com sucesso!")


class UserSearchFrame(ttk.Frame):
    """Frame para pesquisa de usuários no Active Directory."""
    
    def __init__(self, parent, controller):
        """Inicializa o frame de pesquisa de usuários."""
        super().__init__(parent)
        self.controller = controller
        
        # Inicializar variáveis
        self.search_var = tk.StringVar()
        self.users = []
        
        # Criar widgets
        self.create_widgets()
    
    def create_widgets(self):
        """Cria os widgets do frame de pesquisa."""
        # Título
        title_frame = ttk.Frame(self)
        title_frame.pack(fill=tk.X, pady=10)
        
        title_label = ttk.Label(title_frame, text="Pesquisa de Usuários", font=("Arial", 14, "bold"))
        title_label.pack(side=tk.LEFT, padx=10)
        
        new_button = ttk.Button(