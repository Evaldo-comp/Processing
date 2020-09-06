void setup(){
  size(200, 200);
}

void draw(){
  smooth();
  noFill();
  beginShape();
  curveVertex(100, 180); // pontos de controle inicial
  curveVertex(50, 140);
  curveVertex(130, 130);
  curveVertex(140, 180);
  curveVertex(20, 80); // pontos de controle final
  endShape();
}
