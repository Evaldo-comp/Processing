void setup(){
  size(300, 300);
}

void draw(){
  char letra = 'A';
  for (int i = 0; i < 26; i++){
    print(letra);
    letra++;
  }
  println('.');
}
