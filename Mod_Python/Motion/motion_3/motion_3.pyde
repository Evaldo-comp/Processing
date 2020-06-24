"""Neste código a forma vai e quando o radius +x for maior que a largura da tela, seja 
quando a forma sair da área visivel ela volta na direção oposta
"""

radius = 40.0
x = 110.0
speed = 1.5
direction =1 # Varivel nova para determinar a direção em que a forma irá se mover

def setup():
    size(240, 120)
    ellipseMode(RADIUS)
def draw():
    global x, direction
    background(0)
    x+=speed * direction
    if x > width - radius or x < radius:
        direction = -direction
    if direction ==1:
        arc(x, 60, radius, radius, 0.52, 5.76)
    else:
        arc(x, 60, radius, radius, 3.67, 8.9)
    
    
