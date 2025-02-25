import gradio as gr 

def reverter_texto(texto):
    revertido= texto[::-1]
    return revertido, len(revertido)

iface=gr.Interface(
    fn=reverter_texto,
    inputs='text',
    outputs=['text','number'],
    title="Reverter texto",
    description="Reverte o texto que você digitar",
    theme="cosmo"
)

iface.launch()

