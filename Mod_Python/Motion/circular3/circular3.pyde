#Uma pequena alteração feita para aumentar o valor escalar em cada quadro
#produz uma espiral, em vez de um círculo:

angle = 0.0
offset = 60.0
scalar = 2.0
speed = 0.05
def setup():
    size(120, 120)
    fill(0)
def draw():
    global angle, scalar
    x = offset + cos(angle) * scalar;
    y = offset + sin(angle) * scalar;
    ellipse( x, y, 2, 2)
    angle += speed
    scalar += speed
