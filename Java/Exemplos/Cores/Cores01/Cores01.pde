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
