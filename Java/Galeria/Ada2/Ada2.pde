void setup(){
  size(400, 400);
}

void draw(){
   background(255);
    PImage img = loadImage("ada.jpg");
    tint(102, 100, 20,102);
    for (int i = 0; i<400; i++){
        image(img, 10, 10, 10, 10);
         tint(random(102), random(100), 20,102);
        image(img, random(10), 10,random(width), random(height));
        
 }
}
