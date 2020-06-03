#Variaveis

a = 10 #cria variavel a apontando para o valor 10
b=10   #cria variavel b apontando para o valor 10
rect(a, 10, 40, 40)   #retângulo com x:10 e y:10
a = a+45              #a agora vale 55, ou seja, desloca-se para a direita
rect(a, 10, 40, 40)   #gera novo retangulo com as novas medidas
b = b+45              #b agora vale 55
rect(10, b, 40, 40)    #desloca b, para baixo
rect(a, b, 40, 40)    


#Variáveis Naturais do processing (width, height)
size(480, 120)
line(0,0,width, height) #inicio da linha (0,0) fim da linha (480, 120)
line(width,0,0, height)
ellipse(width/2, height/2, 60, 60)  #Constroi uma elipse


#Utilizando Artimética básica 
size(480, 120)
x = 25
h = 20
y = 25
rect(x, y, 300, h)
x = x +100
rect(x, y + h, 300, h)  #operações simples
x = x - 250
rect(x, y + h*2, 300, h) 
