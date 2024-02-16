# Desafio
# Um supermercado está fazendo uma promoção de venda de refrigerantes. 
# Se um dia você comprar refrigerantes e levar os cascos vazios no dia 
# seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa 
# cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso 
# comprou várias garrafas no primeiro dia da promoção. Agora ele quer
# saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

# Faça um programa para calcular isso.

# Entrada
# A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. 
# Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  
# respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

T = int(input())

for i in range(T):
    i = input()
    i = i.split()
    N = int(i[0])
    K = int(i[1])
    garrafas_cheias = N // K
    garrafas_vazias = N % K
    total = garrafas_vazias + garrafas_cheias
    print(total)