#Modificando variáveis globais
x = 0
y = 0
def draw():
    global x, y  #necessário para modificar variável global
    x = x+1
    y = y +1
    ellipse(x, y, 10, 10)
    
