/* Exemplo de laço for
*Exemplo by https://processing.org/reference/for.html
*/

void setup(){
  size(400, 400);
}

void draw(){
  for (int i = 0; i < 300; i = i + 10  ){
    line(30, i, 370, i); 
    save("for.png");
  }
}
