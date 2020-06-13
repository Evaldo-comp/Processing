angle = 0.0

def setup():
    size(420, 420)
def draw():
    global angle
    translate(mouseX, mouseY)
    rotate(angle)
    rect(-50, -50, 50, 30)
    line(mouseX, mouseY, height, angle)
    angle+=0.1
