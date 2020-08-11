float x =0.0;
float y =0.0;

void setup(){
  size(400, 400);
}

void draw(){
  float d = dist(width/2,height/2,mouseX, mouseY);
  background(0);
  //stroke(random(255),random(255),random(255));
  strokeWeight(2);
  for(y =0;  y < height; y=y+20){
    for(x = 0; x< width;x+=20){
        fill((d+random(255)),(d+random(255)),(d+random(255)),(d+random(255)));
        rect(x, y, 20,20 );
      }
   
  }
  
  
  


}
