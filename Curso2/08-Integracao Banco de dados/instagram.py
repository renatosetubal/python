import instaloader

# Função principal
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

    print(f"Verificando seguidores e seguindo para @{username}...")

    # Obter lista de seguidores
    seguidores = set()
    for follower in profile.get_followers():
        seguidores.add(follower.username)

    # Obter lista de pessoas que você segue
    seguindo = set()
    for followee in profile.get_followees():
        seguindo.add(followee.username)

    # Comparar as listas para encontrar quem não segue você de volta
    nao_seguidores = seguindo - seguidores

    # Exibir os resultados
    if nao_seguidores:
        print(f"\n{len(nao_seguidores)} pessoa(s) não estão te seguindo de volta:")
        for user in nao_seguidores:
            print(f"- {user}")
    else:
        print("\nTodos os usuários que você segue também estão te seguindo!")

# Executar o programa
if __name__ == "__main__":
    verificar_nao_seguidores()