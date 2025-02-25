from model.biblioteca import Biblioteca
from model.itens.livro import Livro
from model.itens.revista import Revista

biblioteca_cidade = Biblioteca("Vila Velha")
biblioteca_sh = Biblioteca("Vila Nova")
# biblioteca_cidade.alterna_estado()
# biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
# biblioteca_cidade.receber_avaliacao("Sicrano", 9.5)
# biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
# Biblioteca.listar_bibliotecas()

lv1=Livro('Python para iniciantes','Fulano',50.00,'123456789')
rv1=Revista('Contigo','Fulano',10.00,'35ª')
biblioteca_cidade.adicionar_item(lv1)
biblioteca_cidade.adicionar_item(rv1)
lv1.aplicar_desconto()
rv1.aplicar_desconto()




def main():
    biblioteca_cidade.exibir_itens()


if __name__ == "__main__":
    main()