from model.avaliacao import Avaliacao
from model.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas=[]
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)
       
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da Biblioteca'.ljust(25)} | {'Nota média:'.ljust(25)} | {'Status'}")
        for b in Biblioteca.bibliotecas:
            print(f'{b.nome.ljust(25)} | {str(b.media_avaliacoes).ljust(25)} | {b.ativo}')
    
    def alterna_estado(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"
    
    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)   
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao),1)
        return media        
    
    def adicionar_item(self,item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
    
    def exibir_itens(self):
        print(f'Itens da Biblioteca: {self.nome}')
        for i, item in enumerate(self._itens,start=1):
            if hasattr(item,'isbn'):
                msg= f"{i}. Titulo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}"
            else:
                msg= f"{i}. Titulo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}"
                    
            print(msg)