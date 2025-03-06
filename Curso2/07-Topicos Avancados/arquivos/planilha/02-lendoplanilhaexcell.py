import pandas as pd

#1-Importando os dados
caminho_arquivo="clientes.xlsx"
tb_clientes=pd.read_excel(caminho_arquivo, sheet_name="Aba1")

#2-Definindo o indice
tb_clientes=pd.read_excel(caminho_arquivo, index_col=1)
print(tb_clientes)

#3 - Importar colunas específicas
tb_clientes=pd.read_excel(caminho_arquivo, usecols=[1,2])
print(tb_clientes)

#4 - Exportar dados para outra planilha
tb_clientes_aba1 = pd.read_excel("clientes.xlsx", sheet_name="Aba1")
tb_clientes_aba2 = pd.read_excel("clientes.xlsx", sheet_name="Aba2")
with pd.ExcelWriter("novaplanilha.xlsx") as nova_planilha:
    tb_clientes_aba1.to_excel(nova_planilha, sheet_name="Aba1", index=False)
    tb_clientes_aba2.to_excel(nova_planilha, sheet_name="Aba2", index=False)