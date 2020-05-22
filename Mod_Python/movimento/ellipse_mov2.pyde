x = 0 #variavel global
y =0

def setup():
    size(500, 500)
    background(10, 0, 200)
    
def draw():
    ellipse(width/2, height/2, mouseX, mouseY)
    
def keyPressed():
    global x
    x = x+1



