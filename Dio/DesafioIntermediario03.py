a = input()

b = input()

c = input()

if a == "invertebrado" and b == "inseto" and c == "hematofago":
    print("pulga")
elif  a == "vertebrado" and b == "ave" and c == "carnivoro":
    print("aguia")  
elif  a == "invertebrado" and b == "anelideo" and c == "onivoro":
    print("minhoca")  
elif  a == "invertebrado" and b == "anelideo" and c == "hematofago":
    print("sanguessuga")  
elif  a == "invertebrado" and b == "inseto" and c == "herbivoro":
    print("lagarta")  
    
    
    ou
    
    a = input() 
b = input() 
c = input() 

if a == 'vertebrado':
    if b == 'mamifero':
        print('homem')  
    elif c == 'herbivoro':
        print('vaca')
    elif b == 'ave':
       if c == 'carnivoro':
           print('aguia')
       else:     
           print('pomba')
    ''' 
    TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
    o esquema da imagem.
    TODO Imprima, de acordo com as condições, o animal identificado.
    '''
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
           print('pulga')
        elif c == 'herbivoro':
           print('lagarta')
    elif b == 'anelideo':
       if c == 'hematofago':
           print('sanguessuga')
       elif c == 'onivoro':
           print('minhoca')
           
           
código que passou
a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave' and c == 'carnivoro':
        print('aguia')
    elif b == 'ave' and c == 'onivoro':
        print('pomba')
    elif b == 'mamifero' and c == 'onivoro':
        print('homem')
    elif b == 'mamifero' and c =='herbivoro':
        print('vaca')
elif a == 'invertebrado':

    if b == 'inseto' and c == 'hematofago':
        print('pulga')
    elif b == 'inseto' and c == 'herbivoro':
        print('lagarta')
    elif b == 'anelideo' and c == 'hematofago':
        print('sanguessuga')
    elif b == 'anelideo' and c =='onivoro':
        print('minhoca')