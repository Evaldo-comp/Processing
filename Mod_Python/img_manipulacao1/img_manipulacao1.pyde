# PARA CARREGAR UMA IMAGEM IMPORTADA
# 1 - Importe uma imagem para a pasta data
# 2 - Crie uma variável para essa imagem
# 3 - Chame pela função loadImage()passando a variavel da iamgem como argumento

img = None  #Inicializa a variável da imagem
def setup():
    size(400, 400)
    global img
    img =  loadImage("lunar.jpg")
    
def draw():
   image(img, 0, 0, 100, 100) 
   #1 parâmetro(variavel da imagem)
   #2 e 3 parâmetros(coordenadas)
   #3 e 4 parâmetros(medidas da iamgem)
   
   
