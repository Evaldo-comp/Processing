"""Imagens vetorias também podem ser carregadas no seu sketch
a forma de carregamento é semelhante a das imagens.
1 - Adciona o arquivo SVG na pasta data do sketch
2 - Criar uma variável para guardar o arquivo vetorial
3 - Carregar o vetor através da variável loadShape()"""

#Exemplo1:
network = None

def setup ():
    global network
    size(480, 120)
    network = loadShape('network.svg')
    
def draw():
    background(0)
    shape(network, 30, 10)
    shape(network, 180, 10, 280, 280)
    
