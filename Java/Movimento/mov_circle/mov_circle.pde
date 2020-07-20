int circleX;
int cor = 255;
void setup(){
  size(640, 360);
  circleX = 50;
}

void draw(){
  background(50);
  fill(random(cor), cor % random(cor), cor* random(cor));
  ellipse(circleX+=3.6 , 180, 24, 24);
  
  //Verifica se o circulo chegou na borda
  if(circleX > width){
    ellipse(width--, 180, 24, 24);  //movimenta o circulo na direção contrária 
    }
  
 fill(random(cor),random(cor), random(cor));
 ellipse(random((circleX)), random(height), 24, 24);
}
