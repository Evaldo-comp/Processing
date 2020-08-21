### Condicionais
As estruturas condicionais fazem uso de operadores relacionais e lógicos para retornar true ou False, essa estrutura controla o fluxo do 
programa ajudando a fazer decisões.

***Operadores Relacionais***
   
   ```
   ->  Maior que
   >= Maior ou igual a 
   < Menor que
   <= Menor ou igual a
   == igual
   != Diferente
  ```
***Operadores Lógicos***
```
  - || ou
  - && And
  - ! Not
  ```
  ***Estrutura de uma Condicional***
  
  ```if (teste){
    instrução
}
```

***Exemplo:***
```java

// Muda a forma desenhada dependendo da posição do mouse

void setup(){
  size(200, 200);
}

void draw(){
  background(0);
  int x = mouseX;
  if (x < 150){
    ellipse(width/2, height/2, 100, 100);
  }else if (x > 150){
    rect(width/2, height/2, 100, 100);
  }
  ```
  
  ***Tela***
  
  ![Condicioanl](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Condicional/cond.gif)
  
  


