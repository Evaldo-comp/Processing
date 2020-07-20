### SOBRE PROCESSING:

## O que é? 
Processing é uma linguagem baseada em **Java**, desenvolvida em 2001  no **Instituto de Tecnologia de Massachusetts (MIT)**, por Casey Reas e Ben Fry, quando estudavam com John Maeda em um grupo de pesquisa sobre estética e computação. O processing com sua sintaxe simplificada permitiu que designers e engenheiros pudessem se aventurar na criação de gráficos e animações. O processing é gratuito e opensource, ou seja, você pode juntamente com a comunidade sugerir melhoras e ajudar na correção de erros.

------------


------------


## Hello World!
Para entendermos um pouco como funciona o processing, vamos executar esse ***[programa](https://github.com/Evaldo-comp/Processing/blob/master/Java/intro/helloworld/helloworld.pdehttp:// "programa") ***que é o equivalente ao nosso Hello World de cada dia.

No programa Hello World podemos notar 3 funções, *setup(  )*, *draw(  )* e *line(  )*, veremos com mais detalhes todas essa funções mais adiante, mas queria focar principalmente em duas delas: *setup(  )* e *draw(  )*. Em odo programa escrito em processing , você irá encontrar estas duas funções.
A função **setup(  )** inicializa o programa, é nela que vai o tamanho da tela, variáveis globais, e etc.
A função **draw(  )** é o passo a passo, é a execução do código, tudo que está dentro desta função é executada várias vezes por segundo na tela, diferente da setup que é executada apenas na inicialização.

------------


------------



## Provando a execução constante da função draw(  ):
Para entender como a função draw(  ) está em constante execução, utilize a função **frameRate(  )** para imprimir na tela a velocidade de frames que são executados por segundo. Por padrão o pŕocessing executa a função draw(  ) **60 vezes por segundo**, mas este valor pode ser modificado através da função frameRate(  ). 
Este ***[programa](https://github.com/Evaldo-comp/Processing/blob/master/Java/intro/frameRate/frameRate.pdehttp:// "programa")*** mostra no terminal quantos a velocidade em que os frames são executados
:fa-bell-o: OBS: Um programa em processing pode ser executado sem a função draw() mas não sem a função setup(  )


------------


------------

## A sintaxe:  
Assim como a língua portuguesa, as linguagens de programação possuem regras de sintaxe que devem ser obedecidas, caso contrário o código apresenta erros e não será entendida,o que pode impossibilitar sua execução, algumas regras básicas de sintaxe no processing.
- Todas as funções são seguidas de  parênteses (  ), dentro desses irão os parâmetros se essa função assim exigir, entenderemos melhor o funcionamento de funções mais adiante.
- Depois dos parênteses temos as { }, elas servem para delimitar um bloco.
- Ao fim de cada frase colocamos vírgula ou ponto, em processing é exigido a colocação de ; eles indicam que aquela linha de código acabou e pode passar para a próxima instrução.

------------


------------

## De volta ao ensino médio. Lembra do plano cartesiano?
A tela no processing é medida em pixels, quando executamos size(300, 300), estamos dizendo que queremos uma janela de 300 pixels de largura por 300 pixels de altura. cada cada pixel dentro dessa tela corresponde a uma coordenada que pode ser no eixo horizontal x ou vertical y. O ponto inicial desta coordenada fica no canto superior esquerdo, o eixo horizontal cresce para a direita e o vertical cresce para baixo, isso mesmo, o eixo y no processing cresce para baixo.
<br>
<br>
<br>
![Alt text](https://i.imgur.com/Mu8WcnR.png "Optional title")
