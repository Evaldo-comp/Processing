#Rotate

def setup():
    size(120, 120)
    
def draw():
    rotate(mouseX / 50.0)
    rect(40, 30, 160, 20)
