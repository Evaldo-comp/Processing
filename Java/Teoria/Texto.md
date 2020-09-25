### TEXTO

#### Caracteres:
O tipo de dado *char*, guarda símbolos tipográficos como A, d, 5 e $. O nome char é a abreviação de character, esse tipo de dado se diferencia dos outros tipos tipográficos por estar entre aspas simples ' '. A atribuição de variáveis do tipo char acontece da mesma forma como acontece com outros tipos de dados:
```java
char a = ‘n’;
char b = b;
```
A declaração seguintes cria uma variável do tipo char, atribui um valor a ela e em seguida printa esse valor no console.
```java
void setup(){
  size(300, 300);
}

void draw(){
  char genero = 'M';
  print(genero);
}
```

Alguns caracteres tem um número correspondente na tabela ASCII. Por exemplo A é 65, B é 66, C é 67 e etc. Você pode descobrir qual o número de um determinado caracteres utilizando a função ```println()```:<br/>
```java
void setup(){
  size(300, 300);
}

void draw(){
  char letra = 'M';
  println(letra);
  int n = letra;
  println(n);
}
```

______

#### Strings:<br/>
As strings guardam um conjunto de palavras, entre aspas duplas " QWERTY", uma String é diferente de tipos como int , float porque a String é um  objeto, um tipo de dado composto  que contem múltiplas funções.
```java

String a = “Exemplo”;
String b = “b”;
```

______

#### Dados Primitivos e Objetos:

Quando uma variável é criada, seu tipo de dado é especificado, se a variável precisa guardar um valor numérico, o tipo de dado usado será *int*, ou *float* . Se o dado for um caractere ou um conjunto de caracteres, devemos utilizar respectivamente dados do tipo char ou String,  valores True ou False, são armazenados em variáveis do tipo booleano, uma imagem é guardada numa variável *PImage*, um tipo de letra, ou seja, fontes, são guardadas em variáveis *PFont*. Algumas vezes será necessário converter um valor para um tipo de variável diferente.

Dados do tipo *int* , *float* e *booleano* são chamados de tipos de dados primitivos porque eles armazenam um único elemento. Os tipos *String*, *PImage* e *PFont* são diferentes, estes são considerados objetos. Objetos são usualmente compostos por vários tipos de dados primitivos(ou outros objetos).

#### Conversão de Dados:

Algumas conversões são automáticas e outras precisam ser realizadas explicitamente com funções. Conversões automáticas são realizadas entre tipos de dados compatíveis, como por exemplo um *int* pode automaticamente ser convertido para um *float*, mas um *float* não pode ser convertido automaticamente para um *int*.

```java
float f = 12.6;
int i = 127;
f = i; //converte 127 para 127.0
i = f; // erro 
```
*Como vou saber se um determinado tipo de dado é compatível com outro ou quando eles necessitam de uma conversão explícita?*<br/>
Converções que envolvem perda de informação, deve ser explícitas. Quando convertemos *int* para *float* não há perda de informação, quando convertemos *float* para *int*, o número após a casa decimal é perdido, sendo necessário então uma <b>Conversão Explícita</b>. As funções para conversão explícita são:<br/>
 - boolean()
 - byte()
 - char()
 - float()
 - int()
 - str()
 
 Cada função é utilizada para converter algum tipo de dado para o tipo de dado que dá nome a função.
 
 ```java
 int i = 0;
boolean b = boolean(i);
int n = 12;
b = boolean(n);
String s = "false";
b = boolean(s)
```

A função ```byte( )```, converte outros tipos de dados para uma representação em byte que pode ser um número entre <b>-128</b> e <b>127</b>.

```java

float f = 12.4;
byte b = byte(f);
char c = 'C';
b = byte(c);
```
A função ```char(  )```, converte outros tipos de dados para a sua respectiva representação  em char.<br/>
```java

int i = 65;
char c = char(i);
```

A função ```str( )``` ,converte um tipo de dado para sua respectiva representação em String.</br>
```java
int i = 4;
String s = str(i);
boolean b = true;
s = str(b); 
```

______

#### Objetos:

Variáveis criados com ```PImage```, ```PFont``` e ```String``` são tipos de objetos. Variáveis escritas em um objeto são chamadas <b>fields</b>, e funções escritas num objeto são chamadas de <b>métodos</b>. Fields e Métodos são acessados com o operador ponto entre  o nome do objeto e o nome do elemento ou função dentro do objeto.

Um tipo de dado ```PImage``` tem dois fields que guardam a largura e altura da imagem, chamados apropriadamente de *width* e *height*:</br>
```java

PImage img = loadImage("ohio.jpg"); // Load a 320 x 240 pixel image
int w = img.width;
// Assign 320 to w
int h = img.height; // Assign 240 to h
println(w); // Prints "320"
println(h); // Prints "240"
```

A String inclui métodos para examinar caracteres individualmente  convertendo para caixa alta ou caixa baixa ou até mesmo comparando duas Strings como podemos  observar no exemplo:
```java

String s1 = "Player Piano";
String s2 = "P";
println(s1.length()); // Prints "12"
println(s2.length()); // Prints "1"
```
Os métodos  ```startsWidth( )``` e ```endsWidth( )``` testa se uma string começa ou termina com a string usada como parâmetro.</br>
```java

String s1 = "Slaughterhouse Five";
println(s1.startsWith("S"));
// Prints "true"
println(s1.startsWith("Five")); // Prints "false"
println(s1.endsWith("Five"));
// Prints "true"
```
O método ```charAt( )``` é usado para ler um único caractere dentro de uma string. Esse método tem um parâmetro que define o índice do caractere a ser retornado:
```java
tring s = 'Evaldo"
println(s.charAt(0)); // imprime 'E'
println(s.charAt(3)); // imprime 'l'
println(s.charAt(5)); // imprime 'o'
```
O método ```toCharArrray( )``` cria um array com caracteres de uma string. </br>
```java

String s = "Evaldo";
char [] c= s.toCharArray();
println(c[0]); // imprime "E"
println(c[']); // imprime "v"
```
O método ```substring( )``` retorna uma nova string que parte de uma string original . Quando o método é usado com um parâmetro, a string é lida de uma posição coletada do parâmetro até o fim da string. Quando dois parâmetros são usados a String entre os dois parâmetros é retornada.
```java

String s = "Giallo";
println(s.substring(2));
// Prints "allo"
println(s.substring(4));
// Prints "lo"
println(s.substring(1, 4)); // Prints "ial"
println(s.substring(0, s.length()-1)); // Prints "Giall"
```
O método ```toLowerCase( )``` retorna uma cópia das strings com todos os caracteres em caixa baixa, o método ```toUpperCase( )``` faz o mesmo, mas retorna uma cópia em caixa alta.
```java

String s = "Nero";
println(s.toLowerCase());// Prints "nero"
println(s.toUpperCase());// Prints "NERO"
```
É possível comparar se duas Strings possuem os mesmos caracteres utilizando o método ```equals( )```.
```java
String s1 = "Bianco";
String s2 = "Bianco";
String s3 = "Nero";
println(s1.equals(s2));
println(s1.equals(s3));
// Prints "true"
// Prints "false"
```

















