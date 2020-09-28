void setup(){
  size(400, 400);
}
void draw(){
  background(255);
PFont fonte; // declação da variável
fonte = loadFont("Z003-MediumItalic-48.vlw"); // carregando a fonte
fill(0);
textFont(fonte);
text("TREMOR", random(width), random(mouseY)); // Escreve na coordenada 0, 40 
if (mouseY == width/2)
      save("text.png");

}
