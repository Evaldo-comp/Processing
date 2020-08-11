//imprime o frameRate no terminal

void setup(){
size(400,400);
frameRate(5);//sinaliza a quantidade de frames executados por segundo

}

void draw(){
line(0,0,400,400);
println(frameCount+ "*");//imprime no terminal  os frames
}
