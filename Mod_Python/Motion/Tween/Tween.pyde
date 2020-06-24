""" A interpolação, ou em inglês Tween, faz um cálculo entre posição final e inicial
para mover um forma de um ponto a outro da tela.

"""
startX = 20.0
stopX = 160.0
startY = 30.0
stopY = 80.0
x = startX 

y =startY
step = 0.005 #tamanho de cada passo (0.0 a 1.0)
pct = 0.0

def setup():
    size(240, 120)
    
def draw():
    global x, y, pct
    background(0)
    if pct < 1.0:
        x = startX + ((stopX - startX) * pct)
        y = startY + ((stopY - startY) * pct)
        pct +=step
    ellipse(x, y, 20, 20)
