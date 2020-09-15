void setup(){
  size(400, 400);
}

void draw(){
  // background(0,0,0);
    PImage img = loadImage("ada.jpg");
    //tint(random(102), random(100), random(20),random(102));
       for (int i = 0; i < 255; i++){
       tint(i, random(i), random(255),random(102));
       }
        image(img, random(255), random(255),200, 200);
        
 
}
