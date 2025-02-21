#1- Fatorial de um número
def fatorial(num):
    if num ==1:
        return 1
    else:
        return(num * fatorial(num -1))

n = int(input("Digite o número para o cálculo de fatorial: "))
print(f"O fatorial de {n} é {fatorial(n)}")

#2- Soma total de um número
def totalSoma(n):
    if n == 1:
        return 1
    else:
        return(n + totalSoma(n -1))

n = int(input("Digite o número para soma: "))
print(f"a soma de6 {n} é {fatorial(n)}")