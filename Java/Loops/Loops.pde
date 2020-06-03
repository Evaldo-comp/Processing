

/*void draw(){
    for(int x = 0; x <=150; x = x+10){ 
    line(x,0,x,150);
    }
}
*/
void draw(){

   background(#201A86);
   for(int c = 0; c<5;c++){
       rect(mouseX, mouseY+(c*15),10,10);
   
   }
}
