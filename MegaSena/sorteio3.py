from random import sample
jogos = int(input('Digite o número jogos quer fazer? '))
for n in range(jogos):
    print(f'\nJOGO{n+1} - ',end='')
    for jogo in sorted(sample(range(1,61),6)):
        print(jogo,end=' ' )