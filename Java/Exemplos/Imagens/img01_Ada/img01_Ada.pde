void setup(){
  size(400, 400);
}

void draw(){
    PImage img = loadImage("ada.jpg");
    for (int i = 0; i<400; i++){
        image(img, random(i), random(i), 60, 60);
        
 }
 save("img01.png");
}
