y = 100  #variavel global

def setup():
    global x  #cria uma variavel global dentro do setup
    size(256, 256)
    x = width/2
    
def draw():
    global x #Altera a variavel global dentro do draw
    background(random(100, 150))
    tamanho = random(100, 150)
    ellipse(x, y, tamanho, tamanho)
    x = x+1
    if x>width:
        x=0
    
