#Modificando a direçao de uma forma depois de um tempo predeterminado

time1 = 2000
time2 = 4000
x = 0.0
def setup():
    size(480, 120)
def draw():
    global x
    currentTime = millis()
    background(204)
    if currentTime > time2:
        x -= 0.5
    elif currentTime > time1:
        x += 2
    ellipse(x, 60, 90, 90)
