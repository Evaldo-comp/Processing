###  FORMAS PRIMITIVAS

Algumas formas já vem pré determinadas pelo processing, cabendo a nós apenas invocá-las e fornecer os parâmetros necessários. cada forma tem uma quantidade específica de parâmetros, é possível desenhá-las utilizando apenas os comandos básicos da linguagem, mas utilizar sua forma primitiva de construção fornecida pelo Processing facilita muito o trabalho e permite que possamos focar nossa atenção em outras coisas mais importantes.

______

#### Ponto:
Desenha um ponto na tela, esse ponto ocupa especificamente um pixel, nas coordenadas que você indicar como parâmetro.

***Código***
```Java
void setup(){
  size(200, 200);
}
void draw(){
point(x, y) // Necessita de dois parâmetros: o x coordenada horizontal e y a coordenada vertical 
}
```
***Tela:***<br>
![Ponto](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/ponto/point.png)

______

#### Linha:

Para desenhar uma linha precisamos inserir quatro parâmetros, sendo o primeiro par a ponta inicial ou outro par as coordenadas da ponta final da linha.

***Código***
```Java
void setup(){
  size(200, 200);
}
void draw(){
 line(30, 30, 200, 200);
 }
```
***Tela:***<br>
![Linha](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/line/line.png)

______

#### Triângulo:
Para desenhar um triângulo iremos inserir 6 parâmetros cada par é referente a um vértice do triângulo.<br> 
*triangle(x1, y1, x2, y2, x3, y3)*

***Código***
```Java
 void setup(){
  size(200, 200);
}

void draw(){
  triangle(100, 0, width, height/2, 0, height/2);
  
}
```
***Tela:***<br>
![Triângulo](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/triangle/triangulo.png)


______


#### Quadrilátero
Segue a mesma lógica do triângulo, devemos apenas acrescentar mais um par de coordenadas para gerar o quarto ângulo.
quad(x1, y1, x2, y2, x3, y3, x4, y4)

***Código***
```Java
 void setup(){
  size(200, 200);
}

void draw(){
  triangle(100, 0, width, height/2, 0, height/2);
  
}
```
***Tela:***<br>
![Triângulo](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/quadrilatero/quad.png)















