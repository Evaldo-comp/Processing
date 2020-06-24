""" Para gerar movimentos mais fluidos e aconcelhavel utilizar dados do tipo float
pois eles oferecem possibilidades maiores de velocidade do os ints
"""

radius = 40.0
x =-radius
y =-radius
speed = 2.5

def setup():
    size(240, 120)
    ellipseMode(RADIUS)
    
def draw():
    global x,y
    background(0)
    x += speed # incrementa o valor de x
    #y += speed
    if x > width+radius: #verifica se a forma sai da janela, 
        x =-radius  
    arc(x, 40, radius, radius, 0.52, 5.76)
    
#Prática: Faça com que a mesma forma se movimento de forma initerrupta na vertical
