'''Location 3: 
    O programa a seguir faz o teste de localização do cursor em relação
    ao retângulo, se estiver dentro o preechimento ser a da cor preta
    se estiver fora o preechimento ser ad cor branca
'''
x = 80
y = 30
w = 80
h = 60

def setup():
    size(240, 120)
    
def draw():
    background(204);
    if mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h:
        #Essa linha faz testes utilizando conectivos and para 
        #verificar se o cursor estpa dentro do triângulo
        fill(0)
    else:
        fill(255)
    rect(x, y, w, h)
    
