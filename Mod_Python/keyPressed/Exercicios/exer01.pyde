#Exercício: Faça com que o retângulo se movimente nas quatro direções:
x = 215
y = 60
def setup():
    size(480, 120)
    
def draw():
    global x, y
    if keyPressed and key == CODED:   #verifica se a tecla pressioanda e do tipo codificada
        if keyCode == LEFT:
            x -=1
        elif keyCode == RIGHT:
            x +=1
        elif keyCode == UP:
            y -=1
        elif keyCode == DOWN:
            y +=1
    rect(x, y, 50, 50)
