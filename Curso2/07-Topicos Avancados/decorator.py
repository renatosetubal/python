def my_decorator(function):
    def wrapper():
        print("Antes de executar a função")
        function()
        print("Depois de executar a função")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func=function()
        changeToUppercase=func.upper()
        return changeToUppercase
    return wrapper
    
def split_string(function):
    def wrapper():
        func=function()
        splittedString=func.split()
        return splittedString
    return wrapper
            