void setup(){
  size(200, 200);

}

void draw(){
  smooth();
  noStroke();
  ellipseMode(RADIUS);
  fill(126);
  ellipse(50, 50, 100, 100);
  fill(255);
  ellipseMode(CORNER);
  ellipse(50, 50, 100, 100);
  fill(0);
  ellipseMode(CORNERS);
  ellipse(50, 50, 100, 100);
  
}
