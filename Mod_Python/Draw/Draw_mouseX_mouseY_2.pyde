# É acrescentado o background no drwa para limpar o fundo

def setup():
    size(480, 120)
    fill(0, 102)
    noStroke()
    
def draw():
    background(204)
    ellipse(mouseX, mouseY, 9,9)
                                
