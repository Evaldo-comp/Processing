# Desenha  letras na tela
def setup():
    size(120, 120)
    textSize(64)
    textAlign(CENTER)
    
def draw():
    background(0)
    if keyPressed:
        text(key, 60, 80)
