def setup():
    size(256, 256)
    background(0, 100, 0) #Fundo verde
    
def draw():
    if mouseY < 128 : #Mouse  na metade de cima da tela
        fill(255)     #preenchimento branco
        
    else:
        fill(100)     #preenchimento cinza
            
    #Condição caso o mouse seja pressionado
    if mousePressed:
       
        background(12, 33, 200)
        ellipse(mouseX, mouseY, 50, 50) #desenha um circulo na posição do mouse
        
    #Condicional para fazer algo caso a tecla'a' seja pressionada
    
    if keyPressed and key == 'a':
        background(0, 100, 0) #apaga a tela com fundop verde
