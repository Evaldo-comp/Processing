//Desenha um ponto, mas utiliza random()para gerar pontos em partes aleatórias da tela

void setup(){
  size(200, 200); // define o tamanho da tela
}

void draw(){
  fill(random(255), random(255), random(255));//gera cores aleatóras
  point(random(width), random(height));//define a localização randômica
}
