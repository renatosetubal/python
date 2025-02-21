import random
# 1 - Seleciona valor aleatório de uma lista
lista1=[7,6,4,3,2,1]
print(random.choice(lista1))

#2 - Gerar um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

#3 - Selecionar caractere aleatório de uma string
name = "Curso de Python"
r2 = random.choice(name)
print(r2)

#4 - Selecionar mais de um valor aleatório
# random.sample(sequencia, tamanho)
print(random.sample(lista1,2))
print(random.sample(lista1,3))
s = "renato miranda setubal"
print(random.sample(s,2))

#5 - Programa de sorteio
done= False
while not done:
    print("O que você deseja fazer? (1- Advininhar o número 2 - Sair)")
    escolha = input("=> ")
    if escolha == "1":
        print("=======Adivinha o número de 1 a 10:============\n")
        n = int(input("Digite o número de 1 ao 10: "))
        r = random.randint(1,10)
        if n == r:
            print(f"Parabéns você acertou o número! {n}")
        else:
            print(f'Errou! O número sorteado foi: {r}')  
    elif escolha == "2":
        done = True
    else:
        print("Opção inválida, escolha 1 ou 2!")
        