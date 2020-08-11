// OPERADORES LÓGICOS &&  || !

void setup(){
  size(400, 400);
}

void draw(){
  int a = 10;
  int b = 20;
  
  // teste com operador lógico &&, and, e
  if ((a < b)&&(b < 25)){  // ambas devem ser verdadeiras
    line(0, 0, 300, 300);
}
  // teste com operador lógico ||, or, ou
  if ((a < b)||(b < 25)){  // pelo menos uma deve ser verdadeira
      ellipse(0, 0, 300, 300);
  }
  // teste com operador lógico !, not, não
  if (!(a!=10)){          // A negação deve ser verdadeira
    rect(50, 50, 100, 100);
  }
  
}
