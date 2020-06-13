x = 0.0
y = 0.0
px = 0.0
py = 0.0

easing = 0.05

def setup():
    size(480, 480)
    stroke(0, 102)
    
def draw():
    
    global x, y, px, py  #altera as variaveis globais
    targetX = mouseX;  # a variável targetX recebe a localização do mouse
    x +=(targetX - x) * easing
    targetY = mouseY
    y+=(targetY - y) * easing
    weight = dist(x, y, px, py)
    strokeWeight(weight)
    line(x, y, px, py)
    py = y
    stroke(214, 78, 83)
    px = x



