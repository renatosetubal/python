import gradio as gr 
import numpy as np
from PIL import Image
import io,base64

def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo = (
        f"background-color: {cor_fundo};"
        f"color: {cor_texto};"
        "padding: 20px;"
        "text-align:center;"      
    )
    #Converte imagem para base64 se estiver presente.
    image_html=""
    if imagem is not None:
        buffeered = io.BytesIO()
        Image.fromarray(imagem).save(buffeered,format="PNG")
        img_str = base64.b64encode(buffeered.getvalue()).decode()
        imagem_html= (
            f"<img src='data:image/png;base64,{img_str}'"
            "style='max-width:100%; height:auto;'>"
        )

    slide_html = f"""
        <div style="{estilo}">
        <h1>{titulo}</h1>
        <p>{texto}</p>
        {imagem_html}
        </div>
    """
    return slide_html

iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Título do Slide", placeholder="Digite o título do slide"),
        gr.Textbox(label="texto do Slide", placeholder="Digite o texto do slide"),
        gr.Image(type="numpy", label="Imagem do slide"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto")
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de slide",
    description="Crie um slide personalizado"
)
iface.launch()