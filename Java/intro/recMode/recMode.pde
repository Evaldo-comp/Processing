void setup(){
  size(100, 100);

}

void draw(){
  noStroke();
  rectMode(CORNER);
  fill(126);
  rect(40, 40, 60, 60);
  rectMode(CENTER);
  fill(255);
  rect(40, 40, 60, 60);
  rectMode(CORNERS);
  fill(0);
  rect(40, 40, 60, 60);
  
}
