
salario = 2000

def add_bonus(bonus):
    global salario #Aqui estou dizendo que vou utilizar a variável global
    salario+=bonus
    return salario

print(add_bonus(700))