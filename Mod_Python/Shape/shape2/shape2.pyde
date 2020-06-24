""" Imagens vetoriais nao perdem qualidade quando sao redimensionadas,
no exmeplo que se segue o redimensionamento e feito atraves da variável
especial mouseX e a funçao shapeMode e utilizada para desenhar a forma
no centro da tela ao inves do padrao, canto superior esquerdo"""

network = None

def setup():
    global network
    size(240, 120)
    shapeMode(CENTER) #Desenha a forma no centro da tela
    network = loadShape('network.svg')
    
def draw():
    background(0)
    diameter = map(mouseX, 0, width, 10, 800)
    shape(network, 120, 60, diameter, diameter)
