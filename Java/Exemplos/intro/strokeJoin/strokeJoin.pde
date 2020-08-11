void setup(){
  size(100, 100);

}

void draw(){
  smooth();
  strokeWeight(12);
  strokeJoin(BEVEL);
  rect(12, 33, 15, 33);
  strokeJoin(MITER);
  rect(42, 33, 15, 33);
  strokeJoin(ROUND);
  rect(72, 33, 15, 33);
  save("strokeJoin.png");


}
