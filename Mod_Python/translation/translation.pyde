x = 60.0
y = 440.0
radius = 45
bodyHeight = 160
neckHeight = 70
easing = 0.02
#Exemplo do uso da função translation com mouseX

def setup():
    size(120, 120)
    
def draw ():
    translate(mouseX, mouseY)
    rect(0, 0, 30, 30)
  
