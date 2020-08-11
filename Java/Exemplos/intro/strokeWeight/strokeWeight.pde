void setup(){
  size(100, 100);
}

void draw(){
  smooth();
  line(20, 20, 80, 20);
  strokeWeight(6);
  line(20, 40, 80, 40);
  strokeWeight(18);
  line(20, 70, 80, 70);
  save("expessura.png");
 
}
