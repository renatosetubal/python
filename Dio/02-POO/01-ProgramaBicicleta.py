class Bicicleta:
    def __init__(self, cor, marca, ano,valor):
        self.cor=cor
        self.marca=marca
        self.ano=ano
        self.valor=valor
    
    def buzinar(self):
        print('Boooom...')  
    
    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta Parada!")            
    def correr(self):
        print("Aumentando velocidade...")
        print("Velocidade máxima alcançada, cuidado!")      
    
    # def __str__(self): Modelo pedreiro de se fazer
    #     return f"Bicicleta: {self.cor},{self.marca},{self.ano},{self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike = Bicicleta("preta", "Caloi Explorer", 2018, 3.200)
print(bike.cor)
# bike.parar()
# bike.correr()
# bike.buzinar()
print(bike.__str__())
