import gradio as gr 
import string
from collections import Counter

def ant(texto):
    texto=texto.translate(str.maketrans("","",string.punctuation))
    palavras=texto.split()
    npalavras=len(palavras)
    ncaracteres=len(texto)
    frequencia=Counter(palavras)
    frequencia_html="<br>".join(f"{palavra}: {contagem}" for palavra, contagem in frequencia.items())
    return npalavras, ncaracteres, frequencia_html
    


iface= gr.Interface(
    fn=ant,
    inputs=[
        gr.Textbox(label="Digite o texto aqui", lines=6)
        
    ],
    outputs=(
        gr.Number(label="Numero de palavras"),
        gr.Number(label="Numero de caracteres"),
        gr.HTML(label="Frequência de palavras")     
        ),
    title="Analisador de texxto", 
    description="Digite um texto para obter uma análise sobre ele"
)
iface.launch()