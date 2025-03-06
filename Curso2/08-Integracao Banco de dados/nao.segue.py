import instaloader
import os

# Função para salvar a lista de seguidores em um arquivo
def salvar_seguidores(username, seguidores):
    with open(f"{username}_seguidores.txt", "w", encoding="utf-8") as file:
        for follower in seguidores:
            file.write(f"{follower}\n")
    print("Lista de seguidores salva com sucesso!")

# Função para carregar a lista de seguidores de um arquivo
def carregar_seguidores(username):
    if not os.path.exists(f"{username}_seguidores.txt"):
        print("Arquivo de seguidores não encontrado. Criando uma nova lista...")
        return set()
    
    with open(f"{username}_seguidores.txt", "r", encoding="utf-8") as file:
        seguidores = set(line.strip() for line in file if line.strip())
    return seguidores

# Função principal para verificar quem deixou de seguir
def verificar_nao_seguidores():
    # Inicializa o Instaloader
    L = instaloader.Instaloader()

    # Entrar com suas credenciais do Instagram
    username = input("Digite seu nome de usuário do Instagram: ")
    password = input("Digite sua senha do Instagram: ")

    try:
        # Fazer login no Instagram
        L.interactive_login(username)  # Usar login interativo para lidar com 2FA
        print("Login realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        return

    # Carregar o perfil do usuário logado
    profile = instaloader.Profile.from_username(L.context, username)

    print(f"Verificando seguidores para @{username}...")

    # Obter a lista atual de seguidores
    seguidores_atuais = set(follower.username for follower in profile.get_followers())

    # Carregar a lista anterior de seguidores (se existir)
    seguidores_antigos = carregar_seguidores(username)

    # Verificar quem deixou de seguir
    nao_seguidores = seguidores_antigos - seguidores_atuais

    # Exibir os resultados
    if nao_seguidores:
        print(f"\n{len(nao_seguidores)} pessoa(s) deixaram de te seguir:")
        for user in nao_seguidores:
            print(f"- {user}")
    else:
        print("\nNinguém deixou de te seguir desde a última verificação!")

    # Salvar a nova lista de seguidores para futuras comparações
    salvar_seguidores(username, seguidores_atuais)

# Executar o programa
if __name__ == "__main__":
    verificar_nao_seguidores()