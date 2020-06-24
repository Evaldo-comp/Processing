# Movendo uma forma de forma randômica

speed = 2.5
diameter = 20
x = 0.0
y = 0.0
def setup():
    global x, y
    size(240, 120)
    x = width/2
    y = height/2
def draw():
    global x, y
    x += random(-speed, speed)
    y += random(-speed, speed)
    #As duas linhas abaixo impedem que a forma saia da tela
    x = constrain(x, 0, width)
    y = constrain(y, 0, height)
    ellipse(x, y, diameter, diameter)
