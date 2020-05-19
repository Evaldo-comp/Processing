#Esse programa cria uam ellipse simples na tela que muda de cor quando o usuário pressuina o mouse

def setup(): #função para criar a janela
    size(500, 500)
    
def draw(): #função de desenho na tela
    if mousePressed:
        fill(0) #cor do traço quando mouse é pressinado
    else:
        fill(255) #cor do traço
    ellipse(mouseX, mouseY, 40, 10)
