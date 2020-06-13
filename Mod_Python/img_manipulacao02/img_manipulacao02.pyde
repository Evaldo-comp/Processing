# Trabalhando com duas imagens e alterando suas dimensoes

img1 = None
img2 = None

def setup():
    
    global img1, img2
    size(480, 120)
    img1 = loadImage("lunar.jpg")
    img2 = loadImage("capsule.jpg")
    
def draw():
    image(img1, -120, 0)
    image(img1, 130, 0, 240, 120)
    image(img2, 300, 0, 240, 120)
