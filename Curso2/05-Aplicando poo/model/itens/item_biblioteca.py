from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
        
    def __str__(self):
       return f'{self.titulo} ({self.ano})'
   
    @abstractmethod
    def aplicar_desconto(self):
        pass