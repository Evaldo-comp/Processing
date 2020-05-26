def setup():
    size(200, 200)
    background(255)
    noStroke()
    
    #Desenha a posição original em cinza
    fill(192)
    rect(20, 20, 40, 40)
    
    #Vermelho, translúcido mudando as coordenadas
    fill(255, 0, 0, 128)
    rect(20+60, 20+80, 40, 40)
    
    #Azul translúcido mudando a grade
    fill(0, 0, 255, 128)
    pushMatrix()
    translate(60, 80)
    rect(20, 20, 40, 40)
    popMatrix()
