
/* aplicando borda a forma
*
*
* by @evaldo
*/

void setup(){
  size(300, 300);
}

void draw(){
  background(0); // Fundo preto
  fill(61, 242, 34); // Preenchimento da cor verde
  stroke(242, 46, 46); //Borda da cor vemelha
  rect(width/2, height/2, 100, 100);
  save("rec.jpg");
  
  
}
