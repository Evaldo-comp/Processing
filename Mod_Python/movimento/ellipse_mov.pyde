raio = 50 #tamanho do raio do circulo
vx = 2.5  #velocidade horizontal inicial
vy = -1.5 #verlocidade vertical incial

def setup():
    global px, py
    size(400, 400)
    px, py = width/2, height/2  #define a posição incial do circulo no centro
    
def draw ():
    global px, py, vx, vy
    #background(0, 0, 200)#limpa o framde com fundo azul
    px = px+vx
    py = py+vy #atualiza as variaveis na posição do circulo
    
#testa se o circulo esta fora da tela,
#se estiver inverte a velocidade
    if px > width - raio or px < raio:
        vx = -vx
        background(1, 23, 2)
        fill(240, 22, 22)
    if py > height -raio or py < raio:
        vy = -vy
        background(1, 23, 2)
        fill(239, 240,22)
        
    # Desenha o circulo
    stroke(100) #Sem traço de contorno
    ellipse(px, py, raio * 2, raio * 2)



