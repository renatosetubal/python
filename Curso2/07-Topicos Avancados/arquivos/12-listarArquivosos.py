import glob, os, zipfile

#1-Diretório de trabalho atual
print(os.getcwd())

#2-Listar arquivos de um diretório
for file in glob.glob("dados/*.txt"):
    print(file)

#3-Listar arquivos de um diretório e subdiretórios
for file in glob.glob("arquivos/**/*", recursive=True):
    print(file)
#4 -compactar arquivos
with zipfile.ZipFile("arquivos.zip", "w") as zip:
    for file in glob.glob("arquivos/**/*", recursive=True):
        zip.write(file)
