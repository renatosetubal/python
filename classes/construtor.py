class Funcionarios:
    def __init__(self, nome, sobrenome, idade):
        self.nome= nome
        self.sobrenome = sobrenome
        self.idade = idade

    def imprime_nome_sobrenome(self):
        return self.nome + ' - ' + self.sobrenome
    
    
u = Funcionarios( 'Renato', 'Miranda', 12)
print(Funcionarios.imprime_nome_sobrenome(u))    
        