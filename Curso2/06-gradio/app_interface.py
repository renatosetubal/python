import gradio as gr 

def customText(texto,cor_fundo, cor_texto,tamanho_fonte,estilo_fonte):
    estilo = (
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        f"font-size: {tamanho_fonte};"
        f"font-family: {estilo_fonte};"
    )
    return f'<div style="{estilo}">{texto}</div>'
iface = gr.Interface(
    fn=customText,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite um texto aqui..."),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da fonte", value=20),
        gr.Radio(
            choices=["Arial","Courier New","Times New Roman","Verdana"],
            label="Estilo da fonte"
        )
    ],
    outputs=gr.HTML(label="Texto formatado"),
    title="Formatador de texto",
    description="Insira um texto e personalize a aparência com as opções disponíveis"
)
iface.launch()
    