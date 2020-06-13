
#Utilizando a função map()
def setup():
    size(240, 120)
    strokeWeight(12)
    
def draw():
    background(204)
    stroke(102)
    line(mouseX, 0, mouseX, height) #Linha cinza
    stroke(0)
    mx = mouseX/2 + 60
    line(mx, 0, mx, height)  #Linha preta
