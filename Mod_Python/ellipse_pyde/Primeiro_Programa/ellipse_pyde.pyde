def setup():
    size(500, 500)
    
def draw():
    if mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 40, 10)
