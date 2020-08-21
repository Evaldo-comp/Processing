### Repetições com FOR

Laços de repetição são usados para tornar a escrita de trechos de código repetitivos mais conciso, simples e de fácil leitura, 
não só melhorando o desempenho do código mas tabmeḿ facilitando a manutenção e leitura do mesmo.

***Estrutura***
```
for (inicio; teste; atualização){
    declaração;
}
```

***Exemplo***
```java
/* Exemplo de laço for
*Exemplo by https://processing.org/reference/for.html
*/

void setup(){
  size(200, 200);
}

void draw(){
  for (int i = 10; i < 180; i = i + 10  ){
    line(30, i, 180, i);
  }

}
```

:house:[HOME](https://github.com/Evaldo-comp/Processing/blob/master/README.md)
