def setup():
    size(400, 400)
    background(0)#cor de fundo

    olho(random(10, 400),random(10, 400), random(50, 100))
    olho(random(10, 400),random(10, 400), random(50, 100))
    olho(random(10, 400),random(10, 400), random(50, 100))
    
#Definindo a função olho

def olho(x, y, tamanho):
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho/2)
    fill(0)
    circle(x, y, tamanho*.40)
