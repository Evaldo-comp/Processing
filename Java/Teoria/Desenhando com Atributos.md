### DESENHANDO COM ATRIBUTOS

Antes de falarmos dos atributos que podems er utilizados na construção das formas, primeiramente vamos conhcer algumas funções que manipulam cores dentro de um desenho no Processing.

### fill():
Essa função determina o preenchimento da forma, como parâmetro podemos incluir números referentes ao esquema de cores RGB,valores dentro de um range de 0 a 255. Não é obrigatório 
ainserção dos três parâmetros, podemos incluir apenas um tipo, como pode ser observado no exemplo que segue.

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

