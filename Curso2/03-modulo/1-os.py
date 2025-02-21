import os
#1 - Retornar pasta atual
print(os.getcwd())
print(os.listdir())
os.system('ver')
os.system('systeminfo')
os.system('cls')
#os.system('shutdown /s')
#os.system('shutdown /s /t 0')
#os.system('shutdown /a')
#os.system('shutdown /s /t 3600')


def turn_off_one_hour():
    os.system('shutdown /s /t 3600')
    
def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')
    
def cancel_shutdown():
    os.system('shutdown /a')    