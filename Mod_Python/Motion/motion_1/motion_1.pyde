""" O movimento no processing funciona semelhante às antigas animações,
onde uma sequência de imagens eram sobrepostas em intervalos de tempo tão rápidos que nos davam a sensação de movimento, ou seja, quanto mais rápido essa sobreposição acontece mais fluida fica o movimento na nossa percepção.
Podemos dizer que o movimento e o bloco dentro da função draw() sendo executado em uma quantidade x de vezes por segundo
o que chamamos de frame.

"""
#Essa função apenas imprime no console a quantidade de frames executadas por segundo
def draw():
    print(frameRate)
    
# Modificando a velocidade dos frames através da função frameRate()

def setup():
    #frameRate(30)
    #frameRate(100)
    #frameRate(10)
    frameRate(1)

def draw():
    print(frameRate)
