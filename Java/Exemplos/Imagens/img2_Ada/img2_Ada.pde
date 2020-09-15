
void setup(){
  size(400, 400);
}

void draw(){
    PImage img = loadImage("ada-lovelace-20825279-1-402.jpg");
    tint(random(sin(255)), random(255), random(255),random(102));
    for (int i = 0; i<400; i++){
        image(img, random(i), random(i), 200, 200);
        
 }
}
