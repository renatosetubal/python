import gradio as gr 
import string
from collections import Counter

def converter_temperatura(temperatura,escala):
    if escala=="Celsius":
        return(temperatura * 9/5) + 32
    else:
        return (temperatura -32) * 5/9
    
def ant(texto):
    texto=texto.translate(str.maketrans("","",string.punctuation))
    palavras=texto.split()
    npalavras=len(palavras)
    ncaracteres=len(texto)
    frequencia=Counter(palavras)
    frequencia_html="<br>".join(f"{palavra}: {contagem}" for palavra, contagem in frequencia.items())
    return npalavras, ncaracteres, frequencia_html

def criar_relatorio(temperatura, escala, condicao, texto):
    temperatura_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia = ant(texto)
    relatorio=(
        f"**Relatório de clima**\n\n"
        f"Temperatura: {temperatura_convertida:.2f}{'F' if escala=='Celsius' else 'C'}\n"
        f"Condição: {condicao}\n"
        f"Número de Palavras: {num_palavras}\n"  
        f"Número de Caracteres: {num_caracteres}\n"  
    )
    return relatorio

iface= gr.Interface(
    fn=criar_relatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Dropdown(
            choices=["Celsius","Fahrenheit"],
            label="Converter de"
        ),
        gr.Radio(
            choices=["Ensolarado","Nublado","Chuvoso","Neve","Quente","Frio"],
            label="Condição do tempo"
        ),
        gr.Textbox(label="Descrição do dia", placeholder="Descreva o dia de hoje", lines=4)
    ],
    outputs=gr.Markdown(label="Relatório do clima"),
    title="Relatório de Clima", 
    description="Crie um relatório de clima com base na temperatura e na descrição do dia"
)
iface.launch()