import gradio as gr

# Lista para armazenar os usuários cadastrados (simulação de banco de dados)
usuarios_cadastrados = []

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, senha):
    # Verificar se o e-mail já está cadastrado
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email:
            return "Erro: E-mail já cadastrado!"
    
    # Validar comprimento da senha
    if len(senha) < 6:
        return "Erro: A senha deve ter pelo menos 6 caracteres."
    
    # Adicionar o novo usuário à lista
    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    usuarios_cadastrados.append(novo_usuario)
    return f"Usuário {nome} cadastrado com sucesso!"

# Função para alterar os dados de um usuário
def alterar_usuario(email, novo_nome, nova_senha):
    # Procurar o usuário pelo e-mail
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email:
            # Atualizar os dados do usuário
            usuario["nome"] = novo_nome
            usuario["senha"] = nova_senha
            return f"Dados do usuário {email} atualizados com sucesso!"
    
    return "Erro: Usuário não encontrado."

# Função para excluir um usuário
def excluir_usuario(email):
    # Procurar o usuário pelo e-mail
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email:
            usuarios_cadastrados.remove(usuario)
            return f"Usuário {email} excluído com sucesso!"
    
    return "Erro: Usuário não encontrado."

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios_cadastrados:
        return "Nenhum usuário cadastrado."
    
    # Formatar a lista de usuários como uma string
    lista = "\n".join([f"Nome: {u['nome']}, E-mail: {u['email']}" for u in usuarios_cadastrados])
    return lista

# Criar a interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Sistema de Gerenciamento de Usuários")
    
    # Cadastro de Usuário
    with gr.Tab("Cadastro"):
        nome = gr.Textbox(label="Nome Completo")
        email = gr.Textbox(label="E-mail")
        senha = gr.Textbox(label="Senha", type="password")
        botao_cadastrar = gr.Button("Cadastrar")
        saida_cadastro = gr.Textbox(label="Resultado do Cadastro")
        botao_cadastrar.click(cadastrar_usuario, inputs=[nome, email, senha], outputs=saida_cadastro)
    
    # Alteração de Usuário
    with gr.Tab("Alteração"):
        email_alteracao = gr.Textbox(label="E-mail do Usuário")
        novo_nome = gr.Textbox(label="Novo Nome")
        nova_senha = gr.Textbox(label="Nova Senha", type="password")
        botao_alterar = gr.Button("Alterar")
        saida_alteracao = gr.Textbox(label="Resultado da Alteração")
        botao_alterar.click(alterar_usuario, inputs=[email_alteracao, novo_nome, nova_senha], outputs=saida_alteracao)
    
    # Exclusão de Usuário
    with gr.Tab("Exclusão"):
        email_exclusao = gr.Textbox(label="E-mail do Usuário")
        botao_excluir = gr.Button("Excluir")
        saida_exclusao = gr.Textbox(label="Resultado da Exclusão")
        botao_excluir.click(excluir_usuario, inputs=email_exclusao, outputs=saida_exclusao)
    
    # Listagem de Usuários
    with gr.Tab("Listagem"):
        botao_listar = gr.Button("Listar Usuários")
        saida_listagem = gr.Textbox(label="Lista de Usuários", lines=10)
        botao_listar.click(listar_usuarios, inputs=None, outputs=saida_listagem)

# Executar a interface
demo.launch()