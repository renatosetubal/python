from decorator import my_decorator, uppercase_decorator, split_string

@my_decorator
def minha_funcao():
    print("Dentro da função")

minha_funcao()

@uppercase_decorator
def text():
    return "Hello world!"

print(text())

@split_string
def text():
    return "Hello world!"

print(text())