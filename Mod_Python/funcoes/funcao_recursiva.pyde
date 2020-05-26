def setup():
    size(800, 400)
    desenha_retangulos(0, 0, 399, 10)
    
def desenha_retangulos(x, y, tam, level):
    rect(x, y, tam, tam)
    if level > 1:
        level = level -1
        desenha_retangulos(x, y, tam/2, level)
        desenha_retangulos(x + tam, y, tam/2, level)

