# nome=input("Digite o nome do filme:\n")
# ano=int(input("Digite o ano do lançamento:\n"))
# nota=float(input("Digite a avaliação do filme: "))
# if nota > 8 and ano > 2015:
#     print(f'O filme {nome} é muito bom. Recomendo assistí-lo')
# else:
#     print(f'O filme não é tão bom, procure outro! e')

n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
op=input("Digite a operação a ser realizada (+ - * /): ")
result=0
if op == "+":
    result=n1 +n2
elif op == "-":
    result=n1-n2
elif op == "*":
    result=n1*n2
elif op == "/":
    if(n2 == 0):
        print("Não é possível fazer divisão por zero")
    else:    
        result=n1/n2
else:
    print("Operação inválida, reinicie o programa!")
    result = 0
print(f"O resultado da operação é: {result:.2f}")