#animando uma estrela


def setup():
    
    size(400, 400)

def draw():
    background(0, 0, 200) #limpa a rea do desenho
    x, y = width/2, height/2  #coordenadas de centro
    
    a = mouseX / 4
    b = mouseY / 4
    
    beginShape()
    vertex(x - a, y - a)
    vertex(x - b, y) #vertice1
    vertex(x - a, y + a) #vertice2
    vertex(x    , y + b) #vertice3
    vertex(x + a, y + a) #vertice4
    vertex(x + b, y) #vertice5
    vertex(x + a, y - a)
    vertex(x    , y - b) #vertice5 #vertice5
    endShape(CLOSE) #poligono aberto 
