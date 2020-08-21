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
  save("for.jpg");
}
