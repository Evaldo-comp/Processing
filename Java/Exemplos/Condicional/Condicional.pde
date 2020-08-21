
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
  saveFrame("condicional-#####.png");
}
