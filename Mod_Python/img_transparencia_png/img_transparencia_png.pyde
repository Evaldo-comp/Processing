# Utilizando transparencias com PNG
img = None
def setup():
    global img
    size(480, 120)
    img = loadImage("clouds.png")
    
    
def draw():
    background(255)
    image(img, 0, 0)
    image(img, 0, mouseY * -1)
    
