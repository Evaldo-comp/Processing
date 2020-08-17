### DESENHANDO COM ATRIBUTOS

Antes de falarmos dos atributos que podems er utilizados na construção das formas, primeiramente vamos conhcer algumas funções que manipulam cores dentro de um desenho no Processing.

### fill():
Essa função determina o preenchimento da forma, como parâmetro podemos incluir números referentes ao esquema de cores RGB,valores dentro de um range de 0 a 255. Não é obrigatório a inserção dos três parâmetros, podemos incluir apenas um tipo, como pode ser observado no exemplo que segue. Caso não queira preenchimento algum no seu desenho basta chamar a função ```noFill()```.

***Exemplo.***
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

***Tela***

![preenchimento](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/preenchimento/preenchimento.png)

______


#### stroke()
Essa função define a cor da borda da forma, caso não seja passado nenhum valor como parâmetro a cor padrão setada pelo processing será preta, e se você não quizer que a forma possua borda, basta chamar a função ```noStroke()```.

***Exemplo.***
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



***Tela***

![Borda](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/borda_stroke/rec_bord.png)


______


#### strokeWeight()
Através de um atributo númerico determina a espessura da linha

***Exemplo:***
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
***Tela:***

![Expessura](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeWeight/expessura.png)

______


#### strokeCap():
Recebe como parâmetro uma das três constantes(*ROUND, SQUARE ou PROJECT*). Esses atributos alteram a forma das pontas das linhas.
- ***ROUND:*** para pontas redondas
- ***SQUARE:***  para pontas quadradas
- ***PROJECT:*** é uma soma das duas anteriores.

***Exemplo:***
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
  
  ***Tela:***
  
  ![CAP](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeCap/strokeCAP.png)
  
  ______
  
  
#### strokeJoin()
Esse parâmetro determina como as bordas se conectam ao redor da forma. Essa função pode receber três parâmetros.

- ***BEVEL:*** -  Cantos quadrados
- ***MITER:*** -   Une linhas com cantos esse é o default 
- ***ROUND:*** - Cria um curva na conexão

***Exemplo:***
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
  
  ***Tela:***
  
  ![Join](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/strokeJoin/strokeJoin.png)
  
  
  ______
  
  
  
#### ellipseMode()
Como vimos anteriormente para desenhar uma elipse precisamos fornecer quatro parâmetros, os dois primeiros são referentes às coordenadas x e y, e os dois últimos são referentes a altura e largura da forma. Quando utilizamos o ```ellipseMode()```  nós alteramos a referência dos dois primeiros parâmetros dependendo do parâmetro que o ```ellipseMode()``` irá receber, cada parâmetro do ```ellipseMode()``` age de forma diferente sobre os parâmetros do ```ellipse()```.

- ***RADIUS:*** - Pega o primeiro e o segundo parâmetro do ```ellipse()``` para indicar o centro , o terceiro para setar o meio da largura e o quarto para setar o meio da altura.
- ***CORNER:*** -  Faz com que a ```ellipse()``` se comporte de forma semelhante ao retângulo, pega os dois primeiros parâmetros para posicionar no canto superior esquerdo do retângulo que circunscreve a ellipse, o terceiro e quarto servem para indicar normalmente a largura e altura.
- ***CORNERS:*** - Funciona de forma semelhante ao ```CORNER```, mas ele pega o terceiro e quarto parâmetro para setar o canto inferior esquerdo do retângulo.

***Exemplo:***
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
  
  ***Tela:***
  
  ![ellipseMode](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/intro/ellipseMode/ellipseMode.png)
  
  ______
  
  



  
  






