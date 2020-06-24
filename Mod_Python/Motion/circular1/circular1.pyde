# No processing é usado valores de seno e cosseno apra obeter ondas senoidais que por sua
# vez gerrão movimentos mais fluidos e naturais

angle = 0.0
offset = 60.0
scalar = 70.0
speed = 0.10
def setup():
    size(240, 120)
def draw():
    global angle
    background(0)
    y1 = offset + sin(angle) * scalar
    y2 = offset + sin(angle + 0.1) * scalar
    y3 = offset + sin(angle + 0.8) * scalar
    ellipse( 80, y1, 40, 40)
    ellipse(120, y2, 40, 40)
    ellipse(160, y3, 40, 40)
    angle += speed
