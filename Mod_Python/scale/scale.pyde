#Scale

def setup():
    size(400, 400)
    
def draw():
    translate(mouseX, mouseY)
    scale(mouseX/60.0)
    rect(-15, -15, 30, 30)
