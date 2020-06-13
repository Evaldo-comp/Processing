x = 0.0
y = 0.0
px = 0.0
py = 0.0

#MousePressed
def setup():
    size(240, 120)
    strokeWeight(30)
    
def draw():
    background(204)
    stroke(102)
    line(40, 0, 70, height)
    if mousePressed == True:  # outra opção seria 'if mousePressed:', ou seja, a comparação não é obrigatória
        stroke(0)
    line(0, 70, width, 50)


