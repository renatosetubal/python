class Game:
    nome = ""
    anoLancamento = 0
    multiplayer = False
    nota = 0.0
    genero = ""
    
    def __init__(self, nome, anoLancamento, multiplayer, nota, genero):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        self.genero = genero