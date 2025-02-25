import gradio as gr
import math

def fatorial(n):
    if n < 0:
        return "Não existe fatorial de número negativo"
    return math.factorial(n)

iface=gr.Interface(
    fn=fatorial,
    inputs='number',
    outputs='text',
    title="Calculadora de fatorial",
    description="Calcula o fatorial do número que você digitar",
    theme="cosmo"
)   

iface.launch()

