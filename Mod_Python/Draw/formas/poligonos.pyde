#Poligonos_5 lados mais

size(400, 200)

beginShape()#Inicia o poligonoa esquerda
vertex(10, 10) #vertice1
vertex(50, 50) #vertice2
vertex(190, 30) #vertice3
vertex(90, 150) #vertice4
vertex(30, 100) #vertice5
endShape() #poligono aberto


beginShape() #inicia poligonoa direita
vertex(210, 10) #vertice1
vertex(250, 50) #vertice2
vertex(390, 30) #vertice3
vertex(290, 150) #vertice4
vertex(230, 100) #vertice5
endShape(CLOSE) #poligono fechado
