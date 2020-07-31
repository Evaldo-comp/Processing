void setup(){
  size(100, 100);
}

void draw(){
  smooth();
  strokeWeight(12);
  strokeCap(ROUND);
  line(20, 30, 80, 30);
  strokeCap(SQUARE);
  line(20, 50, 80, 50);
  strokeCap(PROJECT);
  line(20, 70, 80, 70);
  save("strokeCAP.png");
}
