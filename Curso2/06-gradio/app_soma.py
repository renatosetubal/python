import gradio as gr 


def somar(x,y):
    return x + y

iface=gr.Interface(
    fn=somar,
    inputs=['number',"number"],
    outputs='number',
    title="Calculadora de soma",
    description="Uma calculadora simples para colocar em prática o Gradio",
    theme="cosmo"
)

iface.launch()