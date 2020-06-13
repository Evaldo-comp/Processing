# Fontes: Importando e desenhando as primeiras palavras.

font = None

def setup():
    global font
    size(480, 120)
    font= createFont("SourceCodePro-Regular.ttf", 32) 
    textFont(font)
    
def draw():
    background(102)
    textSize(32)
    text("Esse é um pequeno passo para um homem..", 25, 60)
    textSize(16)
    text("Esse é um pequeno passo para um homem..", 27, 90) 
    # Aqui podem ser utilizados um quarto e
    #e quinto parâmentro para determianr as coordenadas das letras
    
