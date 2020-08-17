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





