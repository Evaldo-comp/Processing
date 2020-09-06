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
