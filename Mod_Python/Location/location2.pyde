#Esse programa rastreia a localização do cursor em relação ao centro do círculo
# Se o cursor estiver dentro do círculo, a área do círculo irá se expandir 
# e o seu preechimento irá ser mudado para a cor preta

x = 120
y = 60
radius = 12

def setup():
    size(240, 120)
    ellipseMode(RADIUS)
    
def draw():
    global radius
    background(204)
    d = dist(mouseX, mouseY, x, y)
    if d < radius:
        radius +=1 # Aumenta a area do circulo
        fill(0)     # Preeche com a cor preta
    else:
        fill(255)   #Preenche com a cor branca
    
    ellipse(x, y, radius, radius)
    
