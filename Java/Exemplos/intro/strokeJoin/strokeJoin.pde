void setup(){
  size(200, 200);

}

void draw(){
  smooth();
  strokeWeight(12);
  strokeJoin(BEVEL);
  rect(30, 33, 30, 66);
  strokeJoin(MITER);
  rect(90, 33, 30, 66);
  strokeJoin(ROUND);
  rect(150, 33, 30, 66);
  
}
