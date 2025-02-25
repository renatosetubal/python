class Game:    
    
    def __init__(self,nome="",ano="",multiplayer=0,nota=0):
        self.nome=nome
        self.ano=ano
        self.multiplayer=multiplayer
        self.nota=nota
        
        
    def __str__(self):
        return f"Game: {self.name}"
    
