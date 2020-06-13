

#MousePressed
def setup():
    size(240, 120)
    strokeWeight(30)
    
def draw():
    background(204)
    stroke(102)
    line(40, 0, 70, height)
    if mousePressed:
        if mouseButton == LEFT:# Pinta a linha branca se o botão esquerdo for pressionado
            stroke(255)
        else:
            stroke(0)               
        line(0, 70, width, 50)


