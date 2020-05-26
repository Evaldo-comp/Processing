def setup():
    size(256, 256)
    background(255)
    smooth()
    noStroke()
    
def draw():
    if (frameCount % 10 == 0):
        fill(frameCount * 3 % 255,
             frameCount * 5 % 255,
             frameCount * 7 % 255)
        pushMatrix()
        translate(128, 128)
        rotate(radians(frameCount * 2 % 360))
        rect(0, 0, 100, 25)
        popMatrix()
