def setup():
    size(500, 500)
    background(0, 100, 0) #Fundo verde
    
def draw():
    if mouseY <128:
        fill(100)
        a = 60
    else:
        fill(0)
        a =20
       
    if mousePressed:
 
       square(mouseX, mouseY, a)

