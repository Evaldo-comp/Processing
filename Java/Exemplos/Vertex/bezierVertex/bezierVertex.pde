void setup(){
  size(200, 200);
}

void draw(){
  
  noFill();
  beginShape();
  vertex(132, 120);
  bezierVertex(80, 5, 40, 75, 30, 75);
  bezierVertex(10, 5, 40, 5, 30, 75);
  endShape();
  
}
