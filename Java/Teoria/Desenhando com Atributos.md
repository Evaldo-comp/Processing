### DESENHANDO COM ATRIBUTOS

Antes de falarmos dos atributos que podems er utilizados na construção das formas, primeiramente vamos conhcer algumas funções que manipulam cores dentro de um desenho no Processing.

#### fill():
Essa função determina o preenchimento da forma, como parâmetro podemos incluir números referentes ao esquema de cores RGB,valores dentro de um range de 0 a 255. Não é obrigatório a inserção dos três parâmetros, podemos incluir apenas um tipo, como pode ser observado no exemplo que segue. Caso não queira preenchimento algum no seu desenho basta chamar a função ```noFill()```.

##### Exemplo:
```java
void setup(){
  size(200, 200);
}

void draw(){
 
  rect(10, 10, 50, 50);
  fill(204, 123, 100); // preenchimento da forma desenhada abaixo
  rect(20, 20, 50, 50);
  fill(153, 233, 123, 100); // preenchimento da forma desenhada abaixo
  rect(30, 30, 50, 50);
  fill(102); // preenchimento da forma desenhada abaixo
  rect(40, 40, 50, 50);
 
   
}
```

##### Tela:

![preenchimento](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/preenchimento/preenchimento.png)

______


#### stroke()
Essa função define a cor da borda da forma, caso não seja passado nenhum valor como parâmetro a cor padrão setada pelo processing será preta, e se você não quizer que a forma possua borda, basta chamar a função ```noStroke()```.

##### Exemplo:
```java
void setup(){
  size(200, 200);
}

void draw(){
  background(0); // Fundo preto
  fill(61, 242, 34); // Preenchimento da cor verde
  stroke(242, 46, 46); //Borda da cor vemelha
  rect(40, 40, 100, 100);
 }
```



##### Tela:

![Borda](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/borda_stroke/rec_bord.png)


______


#### strokeWeight()
Através de um atributo númerico determina a espessura da linha

##### Exemplo:
```java
void setup(){
  size(200, 200);
}

void draw(){
  smooth();
  line(50, 20, 150, 20);
  strokeWeight(6);
  line(50, 40, 150, 40);
  strokeWeight(18);
  line(50, 70, 150, 70);
}
```
##### Tela:

![Expessura](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeWeight/expessura.png)

______


#### strokeCap():
Recebe como parâmetro uma das três constantes(*ROUND, SQUARE ou PROJECT*). Esses atributos alteram a forma das pontas das linhas.
- ***ROUND:*** para pontas redondas
- ***SQUARE:***  para pontas quadradas
- ***PROJECT:*** é uma soma das duas anteriores.

##### Exemplo:
```java
void setup(){
  size(200, 200);
}

void draw(){
  smooth();
  strokeWeight(12);
  strokeCap(ROUND);
  line(20, 30, 180, 30);
  strokeCap(SQUARE);
  line(20, 70, 180, 70);
  strokeCap(PROJECT);
  line(20, 110, 180, 110);
  }
  ```
  
  ##### Tela:
  
  ![CAP](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeCap/strokeCAP.png)
  
  ______
  
  
#### strokeJoin()
Esse parâmetro determina como as bordas se conectam ao redor da forma. Essa função pode receber três parâmetros.

- ***BEVEL:*** -  Cantos quadrados
- ***MITER:*** -   Une linhas com cantos esse é o default 
- ***ROUND:*** - Cria um curva na conexão

##### Exemplo:
```java
void setup(){
  size(200, 200);

}

void draw(){
  smooth();
  strokeWeight(12);
  strokeJoin(BEVEL);
  rect(30, 33, 30, 66);
  strokeJoin(MITER);
  rect(90, 33, 30, 66);
  strokeJoin(ROUND);
  rect(150, 33, 30, 66);
  }
  ```
  
  ##### Tela:
  
  ![Join](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeJoin/strokeJoin.png)
  
  
  ______
  
  
  
#### ellipseMode()
Como vimos anteriormente para desenhar uma elipse precisamos fornecer quatro parâmetros, os dois primeiros são referentes às coordenadas x e y, e os dois últimos são referentes a altura e largura da forma. Quando utilizamos o ```ellipseMode()```  nós alteramos a referência dos dois primeiros parâmetros dependendo do parâmetro que o ```ellipseMode()``` irá receber, cada parâmetro do ```ellipseMode()``` age de forma diferente sobre os parâmetros do ```ellipse()```.

- ***RADIUS:*** - Pega o primeiro e o segundo parâmetro do ```ellipse()``` para indicar o centro , o terceiro para setar o meio da largura e o quarto para setar o meio da altura.
- ***CORNER:*** -  Faz com que a ```ellipse()``` se comporte de forma semelhante ao retângulo, pega os dois primeiros parâmetros para posicionar no canto superior esquerdo do retângulo que circunscreve a ellipse, o terceiro e quarto servem para indicar normalmente a largura e altura.
- ***CORNERS:*** - Funciona de forma semelhante ao ```CORNER```, mas ele pega o terceiro e quarto parâmetro para setar o canto inferior esquerdo do retângulo.

##### Exemplo:
```java
void setup(){
  size(200, 200);

}

void draw(){
  smooth();
  noStroke();
  ellipseMode(RADIUS);
  fill(126);
  ellipse(50, 50, 100, 100);
  fill(255);
  ellipseMode(CORNER);
  ellipse(50, 50, 100, 100);
  fill(0);
  ellipseMode(CORNERS);
  ellipse(50, 50, 100, 100);
  }
  ```
  
  ##### Tela:
  
  ![ellipseMode](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/ellipseMode/ellipseMode.png)
  
  ______
  
  
#### recMode()
Essa função funciona de forma similar ao ```ellipseMode()```. Tendo como parâmetros:
- ***CORNER  e CORNERS:***  Pegam o terceiro e quarto parâmetros do ```rect()``` para indicar o canto oposto ao cantor principal, ou seja, o oposto ao que fica situado no canto superior esquerdo.
- ***CENTER:*** Este parâmetro pega o primeiro e segundo parâmetro de ```rect()``` para indicar o centro do retângulo e usa o terceiro e quarto para indicar a largura e a altura.

##### Exemplo:
```java
void setup(){
  size(200, 200);

}

void draw(){
  noStroke();
  rectMode(CORNER);
  fill(126);
  rect(40, 40, 100, 100);
  rectMode(CENTER);
  fill(255);
  rect(40, 40, 100, 100);
  rectMode(CORNERS);
  fill(0);
  rect(40, 40, 100, 100); 
}
```

##### Tela:

![recMode](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/recMode/recMode.png)


______


#### Vétices:

 As formas primitivas aprendidas anteriormente oferecem grandes possibilidades, mas futuramente você pode ser desafiado a desenhar formas mais complexas, para o isso podemos utilizar outras opções fornecidas pelo processing como vertex, que consiste na posição definida pela coordenada de x e pela coordenada de y. Cada par de coordenada corresponde a uma “curva” da figura.</br>
Para desenhar uma forma utilizando ```vertex()```, primeiramente devemos iniciar com  a função ```beginShape()``` e finalizá-la com a função ```endShape()```, a função ```vertex()``` vem  no meio das duas. As funções ```beginShape()```  e ```endShape()``` devem sempre vir em pares. A função ```vertex()``` necessita de dois parâmetros , as coordenadas de x e y respectivamente: ```vertex(x, y)```.

Por definição, todas as formas criadas com ```vertex()``` são preenchidas com a cor branca e todos os pontos são interligados por uma linha preta com exceção dos do primeiro e do último, para fechar uma forma com ```vertex()``` basta colocar a constante *CLOSE* como parâmetro da função ```endShape()```.

 
 #### Exemplo:
 ```java
 
void setup(){
  size(200, 200);
}

void draw(){
  beginShape();
  vertex(30, 180);
  vertex(180, 30);
  endShape();
}
```
##### Na Tela:
![Vertex](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Vertex/vertex_line/vertex.png)

##### Exemplo de Triângulo com vertex():
```java
void setup(){
  size(200, 200);
}

void draw(){
  beginShape();
  vertex(30, 180); // vértice 1 do triângulo
  vertex(180, 30);  // vértice 2 do triângulo
  vertex(30, 30);  // vértice 3 do triângulo
  endShape();
}
```
##### Na Tela:
![vertexTrianglo](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Vertex/vertex_triagle/triagulo.png)

______


##### Exemplo de Quadrilátero com vertex():
```java
void setup(){
  size(200, 200);
}

void draw(){
  beginShape();
  vertex(30, 180);
  vertex(180, 30);
  vertex(30, 30);
  vertex(30, 30);
  vertex(20, 100);
  endShape(); 
}

```
##### Na Tela:
![vertexQuadrilátero](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Vertex/vertex_quad/quadrilatero.png)


_____

#### CURVAS

A função ```vertex()``` funciona perfeitamente bem para criar formas com linhas retas, mas se você quiser trabalhar com curvas, deverá utilizar as funções ```curveVertex()``` e ```bezierVertex()```, elas conectam pontos com curvas. Estas funções podem funcionar entre ```beginShape()``` e ```endShape()``` apenas quando ```beginShape()``` não tem parâmetros.

#### curveVertex(): 
Essa função é utilizada para indicar uma seŕie de pontos que se conectam com uma curva ela tem dois parâmetros que indicam o ponto da coordenada x e o ponto da coordenada y do vértice.```curveVertex(x, y)```.

O primeiro e último ```curveVertex()``` servem para guiar o início e fim da curva, são pontos de controle, sendo assim são necessárias pelos menos quatro ocorrências dessa função para desenhar uma curva entre o segundo e terceiro.

##### Exemplo:
```java

void setup(){
  size(200, 200);
}

void draw(){
  smooth();
  noFill();
  beginShape();
  curveVertex(100, 180); // pontos de controle inicial
  curveVertex(50, 140);
  curveVertex(130, 130);
  curveVertex(140, 180);
  curveVertex(20, 80); // pontos de controle final
  endShape();
 
}
```

#### bezierVertex()

Essa função deve ser usada com a função ```vertex()```, ainda que entre as funções ```beginshape()``` e ```endShape()```. A linha é desenhada entre o ponto definido pelo ```vertex()``` e o ponto definido pelo x e y colocados como parâmetros de ```bezierVertex()```. Os primeiros quatro parâmetros da função controlam os pontos que definem a forma da curva.

##### Exemplo:
```java
void setup(){
  size(200, 200);
}

void draw(){
 
  noFill();
  beginShape();
  vertex(132, 120);
  bezierVertex(80, 5, 40, 75, 30, 75);
  bezierVertex(10, 5, 40, 5, 30, 75);
  endShape();
}
```



:house: [HOME](https://github.com/Evaldo-comp/Processing)



  
  



  
  






