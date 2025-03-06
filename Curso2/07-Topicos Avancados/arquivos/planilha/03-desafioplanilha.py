import pandas as pd
import os
from pathlib import Path

#1-Importando os dados de todas as sheets
tb_clientes_dict = pd.read_excel("clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)

#2-Criando a pasta planilha_separada
pasta_saida="planilha_separada"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
#3 - Separar as planilhas
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)

#4 - Consolidando as planilhas
pasta_consolidada="planilha_consolidada"
if not os.path.exists(pasta_consolidada):
    os.makedirs(pasta_consolidada)
#5- Criando o aquivo consolidado
caminho_arquivo_consolidado = os.path.join(pasta_consolidada, "consolidado.xlsx")
with pd.ExcelWriter(caminho_arquivo_consolidado) as consolidado:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidado, sheet_name=arquivo.stem, index=False)