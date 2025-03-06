import pandas as pd
import numpy as np

dados_aba1= {
    'ID': [1, 2, 3, 4],
    'Nome': ['João', 'Maria', 'José', 'Pedro'],
    'Idade': [25, 30, 35, 40],
    'Sexo': ['M', 'F', 'M', 'M']
}
dados_aba2= {
    'ID': [5, 6, 7, 8],
    'Nome': ['Renato', 'Lilian', 'Martha', 'Teófilo'],
    'Idade': [40, 45, 32, 31],
    'Sexo': ['M', 'F', 'M', 'M']
}
dados_aba3 = {
    'ID': [9, 10, 11, 12],
    'Nome': ['Ana', 'Carlos', 'Juliana', 'Rafael'],
    'Idade': [28, 50, 23, 37],
    'Sexo': ['F', 'M', 'F', 'M']
}

dados_aba4 = {
    'ID': [13, 14, 15, 16],
    'Nome': ['Camila', 'Roberto', 'Sandra', 'Lucas'],
    'Idade': [29, 41, 36, 22],
    'Sexo': ['F', 'M', 'F', 'M']
}

df_aba1=pd.DataFrame(dados_aba1)
df_aba2=pd.DataFrame(dados_aba2)
df_aba3=pd.DataFrame(dados_aba3)
df_aba4=pd.DataFrame(dados_aba4)

caminho_arquivo="clientes.xlsx"
with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba1", index=False)
    df_aba2.to_excel(writer, sheet_name="Aba2", index=False)
    df_aba3.to_excel(writer, sheet_name="Aba3", index=False)
    df_aba4.to_excel(writer, sheet_name="Aba4", index=False)    