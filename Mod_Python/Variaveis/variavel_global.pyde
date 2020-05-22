def setup():
    size(256, 256)
    background(100, 0, 0)
    olho(128, 128, 128)
    
    
def olho(x, y, tamanho):
    metade = tamanho /2
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, metade)
    fill(200, 200, 0)
    ellipse(x, y, metade - 5, metade -5)
    fill(0)
    ellipse(x, y, tamanho * 0.2, tamanho * 0.2)   
