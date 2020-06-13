#Verifica qual tecla codificada foi pressionada
#cria um retangulo e movimenta esse retangulo de acordo com a tecla presionada
x = 215
def setup():
    size(480, 120)
    
def draw():
    global x
    if keyPressed and key == CODED:   #verifica se a tecla pressioanda e do tipo codificada
        if keyCode == LEFT:
            x -=1
        elif keyCode == RIGHT:
            x +=1
    rect(x, 45, 50, 50)
