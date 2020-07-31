/* Demonstração de ordem de apresentação na tela
*
*
* by @evaldo
*/

void setup(){
  size(400, 400);
}

void draw(){
  line(0,height,  width, 0); // Primeira linha, abaixo de todas as formas posteriores
  rect(150, 150, 100, 100);// Desenhado primeiro que a ellipse fica por trás da mesma
  ellipse(160, 160, 90, 90); // Fica a frente do retângulo
  line(30,height,  width, 30); // Última linha, acima de todas as formas anteriores
}
