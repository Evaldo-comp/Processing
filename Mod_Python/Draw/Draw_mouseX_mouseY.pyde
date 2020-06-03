# As cordenadas são dadas pelas variaveis que guardão a posição do mouse

def setup():
    size(480, 120)
    fill(0, 102)
    noStroke()
    
def draw():
    background(204)
    ellipse(mouseX, mouseY, 9,9)
                                
