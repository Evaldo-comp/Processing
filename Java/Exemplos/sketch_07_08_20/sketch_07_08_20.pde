//Adaptado de @azaretto_r

float t,r,d,T;
void setup(){
  size(900,900);
  noStroke();
  colorMode(RGB);
}
void draw(){
  clear();
  t-=.0006; // tempo da animação. P + e o -, determina a direção do movimento
  for(d=30;d>10;d-=3)for(r=100;r<3000;r+=50){
    fill(r/4,d*3,215-d*2,255-d*1);
    circle(cos(r+t*d+d*.040)*350+450,sin(r+t*2+d*.04)*350+450,d/3);
   
  }
}
