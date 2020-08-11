//Desenhando um triangulo
void setup(){
  size(200, 200);
}

void draw(){
  triangle(100, 0, width, height/2, 0, height/2);
  save("triangulo.png");
}
