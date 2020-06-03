#Variaveis Especiais
#PmouseY e Pmouse x: essas variaveis guardam a coordenada anterior percorrida pelo mouse nos #eixos horizontal e vertical
def setup():
    size(480, 120)
    strokeWeight(4)
    stroke(0, 102)
    
def draw():
    line(mouseX, mouseY, pmouseX,pmouseY)

