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
  quad(50, 50, 40, 80, 110, 120, 140, 40);
  
}
```
***Tela:***<br>
![Quadrilátero](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/quadrilatero/quad.png)


______


#### Retângulo:
Recebe quatro parâmetros, onde os dois primeiros são as coordenadas do canto superior direito do retângulo e os dois últimos são referentes a largura e altura, respectivamente.
rect(x, y, width, height);

***Código***
```Java
 void setup(){
  size(200, 200);
}

void draw(){
  rect(50, 50, width/2, height/2);
  
}
```
***Tela:***<br>
![Retângulo](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/rect/rect.png)


______


#### Ellipse:
Uma ellipse necessita de quatro parâmetros, os dois primeiros determinam a localização do centro da elipse e os dois últimos são referentes a largura e altura respectivamente.
ellipse(x, y, width, height);

***Código***
```Java
 void setup(){
  size(200, 200);
}

void draw(){
  ellipse(100, 100, 100, 100);
  
}
```
***Tela:***<br>
![Ellipse](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/ellipse/ellipse.png)

#### Ordem de apresetação
A ordem na qual as formas são apresentadas depende de quem é desenhada primeiro no código, a forma que for declarada primeiro ficará abaixo das que forem declaradas na sequência, ou seja abaixo dela no código,  a primeira imagem a ser declarada ficará por trás das outras quando for mostrada na tela. Confuso? Não é pra ser, eu que devo ter me expressado mal :smile:

***Código***
```Java
 void setup(){
  size(400, 400);
}

void draw(){
  line(0,height,  width, 0); // Primeira linha, abaixo de todas as formas posteriores
  rect(150, 150, 100, 100);// Desenhado primeiro que a ellipse fica por trás da mesma
  ellipse(160, 160, 90, 90); // Fica a frente do retângulo
  line(30,height,  width, 30); // Última linha, acima de todas as formas anteriores
}

```
***Tela:***<br>
![Ordem](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/ordem_desenho/ordem.png)






______
:house:[HOME](https://github.com/Evaldo-comp/Processing)





















