# Utilizando mouseX e mouseY para mover as imagens e alterar sua dimensão
img1 = None


def setup():
    
    global img1
    size(480, 120)
    img1 = loadImage("lunar.jpg")

    
def draw():
    background(0)
    image(img1,0,0, mouseX * 2, mouseY * 2 )
