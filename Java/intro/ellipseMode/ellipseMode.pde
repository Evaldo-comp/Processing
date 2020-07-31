void setup(){
  size(100, 100);

}

void draw(){
  smooth();
  noStroke();
  ellipseMode(RADIUS);
  fill(126);
  ellipse(33, 33, 60, 60);
  fill(255);
  ellipseMode(CORNER);
  ellipse(33, 33, 60, 60);
  fill(0);
  ellipseMode(CORNERS);
  ellipse(33, 33, 60, 60);
  save("ellipseMode.png");
}
