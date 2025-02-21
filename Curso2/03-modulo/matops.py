def sum(x,y):
    return x + y
def sub(x,y):
    return x -y

def mult(x,y):
    return x * y

def div(x,y):
    if y != 0:
        return x / y
    else:
       raise ValueError("Divisão por zero não permitido!")
