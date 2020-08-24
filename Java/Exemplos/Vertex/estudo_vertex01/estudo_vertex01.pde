void setup(){
  size(400, 400);
}

void draw(){
  background(100);
    for (int i = 10,  j =2;i<=width && j< 100; i+=10, j++){
  //noStroke();  
  beginShape();
  frameRate(10);
  noFill();
  //fill(random(123), random(255), random(233));
  vertex(random(i), random(j));
  vertex(random(j), random(i));
  vertex(random(i), random(i));
  vertex(random(i), random(i));
  vertex(random(i), random(i));
  vertex(random(i), random(i));
  vertex(random(i), random(i));
 
  
  endShape(CLOSE);
    }
  
}
