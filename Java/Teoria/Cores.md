### CORES

No Procesing as cores são definidas através dos Parâmetros inseridos em funções como  ```background( )```, ```fill( )```, e ```stroke( )```.
```java
background(valor RGB1, valor RGB2, valor RGB2)
```.

Por definição:
- <b>Valor do parâmetro 1:</b> componente de cor vermelha
- <b>Valor do parâmetro 2:</b> Componente verde
- <b>Valor do parâmetro 3:</b> componente azul
Um quarto valor define transparência, mas não é usado em todas as funções, algumas que aceitam o quarto parâmetro é ```fill()``` e ```stroke()```.

##### Exemplo:
```java

void setup(){
  size(200, 200);
}
void draw(){
  background(0);
  int x = 10;
  noStroke();
  for (int i = 51; i <= 255; i +=20){
    fill(100, 220, 100, i);
    rect(x, 10, 180, 150);
    x+= 20;
  }
}
```
##### Tela:<br>
![Cores1](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Cores/Cores01/cores01.png)

Algumas cores podem ser criadas sobrepondo formas, as cores criadas vão depender das cores de preenchimento destas formas e da ordem em que elas estão sendo sobrepostas.

##### Exemplo:
```java

void setup(){
  size(200, 200);
}

void draw(){
  background(0);
  noStroke();
  smooth();
  fill(242, 204, 47, 160);
  ellipse(100, 150, 100, 100);
 
  fill(174, 221, 60, 160);
  ellipse(140, 90, 100, 100);
 
  fill(116, 193, 206, 160);
  ellipse(70, 70, 100, 100);
  }

```
##### Tela:<br>
![Cores2](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Cores/Cores02/cores02.png)

#### A cor como um tipo de dado


Os dados de tipo cor são usados para guardar cores em um programa, e a função ```color()``` é usada para atribuir uma variável cor. A função ```color()``` pode criar valores cinzas, cinza com transparência, valores referentes a cores e transparência.

##### Exemplo: 
- color(gray)
- color(gray, alpha)
- color(value1, value2, value3)
- color(value1, value2, value3, alpha)

Os parâmetros da função ```color( )``` definem uma cor. O parâmetro gray usado sozinho ou com alpha, define tons que vão do branco ao preto. O parâmetro alpha define transparência com valores variando de 0 (transparente) para 255 (opaco).

As variáveis do tipo  cor são definidas da mesma forma que os dados primitivos do tipo int float e etc.

##### Exemplo
```java
cor c1 = color(51); // Cria cinza
cor c2 = color(51, 204); // Cria cinza com transparência
cor c3 = color(51, 102, 153); // azul
cor c4 = color(51, 102, 153, 51); // Cria azul com transparências
```
Após a variável cor ser definida como no exemplo acima, ela pode ser utilizada como parâmetros para funções como ```background( )```, ```fill( )``` e etc.

##### Exemplo:
```java

void setup(){
  size(200, 200);
}

void draw(){
  background(0);
  color verde = color(13, 157, 21);
  color amarelo = color(247, 241, 37);
  color azul = color(82, 115, 232);
 
  fill(verde);
  rect(10, 30, 180, 150);
 
  fill(amarelo);
  quad(10, 110, 100, 30, 190, 110, 100, 180);
 
  fill(azul);
  ellipse(100, 105, 100, 100);
 
  }

```
##### Tela:<br>
![Cores3](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Cores/Cores03/cores03.png)

#### RGB e HSB
Processing usa modelo de cor <b>RGB</b> como padrão, mas a especificação <b>HSB</b> pode ser usada para definir cor tomando como base, valor de matiz, saturação e brilho.
Os valore para matiz que  vão de 0 a 360, são os graus em torno da roda de cores.

Os valores  para saturação e brilho que vão  de 0 a 100, são porcentagens.

#### colorMode()
A função ```colorMode( )``` define o espaço de cores para um programa.

- colorMode(mode)
- colorMoe(mode, range)
- colorMode(mode, range1, range2, range3)

O parâmetro mod, define o modelo de cor que o processing irá utiliza , <b>RGB</b>, <b>HSB</b>.

#### HEXADECIMAL

Esse modelo é mais utilizada por designers e desenvolvedores web , o hexadecimal é apenas o modelo <b>RGB</b> escrito na base hexadecimal

O range indica a variação dos valores.

- colorMode(RGB, 1.0); // Atribui uma variação de vermelho, verde e azul de 0.0 a 1.0

Se for colocado apenas um valor no range, o início é por padrão 0

:house:[HOME](https://github.com/Evaldo-comp/Processing) 







