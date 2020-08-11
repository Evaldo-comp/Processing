float x =0.0;

void setup(){
  size(400, 400);
}

void draw(){
  x =0;
  while(x < width){
    line(x, 0, x, height);
    x+=20.0;
  }


}
