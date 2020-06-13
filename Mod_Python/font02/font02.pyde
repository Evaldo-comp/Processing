# Guardando o texto em uma variável do tipo string

font = None
quote = "Testando strings"

def setup():
    global font
    size(480, 120)
    font = createFont("SourceCodePro-Regular.ttf", 32)
    textFont(font)
    
def draw():
    background(102)
    text(quote, 26, 24, 240, 100)
