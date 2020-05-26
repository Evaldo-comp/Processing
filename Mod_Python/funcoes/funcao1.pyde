def setup():
    size(400, 400)
    fill(cor())
    rect(random(10, 400), random(10, 400), random(10, 400), 300)

def cor():
    r=random(256)
    g=random(256)
    b=random(256)
    cor = color(r, g, b)
    return cor

