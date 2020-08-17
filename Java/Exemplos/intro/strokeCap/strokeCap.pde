void setup(){
  size(200, 200);
}

void draw(){
  smooth();
  strokeWeight(12);
  strokeCap(ROUND);
  line(20, 30, 180, 30);
  strokeCap(SQUARE);
  line(20, 70, 180, 70);
  strokeCap(PROJECT);
  line(20, 110, 180, 110);
  
}
