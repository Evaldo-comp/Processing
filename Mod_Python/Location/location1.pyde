x = 0.0

def setup():
    global x
    size(240, 120)
    x = width /2
    
def draw():
    global x
    background(204)
    offset = 0
    if mouseX > x:
        x+= 0.5
        offset = -10
    if mouseX < x:
        x -= 0.5
        offset = 10
    #Desenha a coluna dependendo do valor de "offset"
    line(x, 0, x, height)
    line(mouseX, mouseY , mouseX+ offset, mouseY - 10 )
    line(mouseX, mouseY , mouseX+ offset, mouseY + 10 )
    line(mouseX, mouseY , mouseX+ offset * 3, mouseY  )
    
