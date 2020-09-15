### IMAGENS
As dimensões de imagens digitais são medidas em unidades de pixels. Toda imagem digital tem uma profundidade de cor, essa profundidade indica o número de bits utilizados para guardar cada pixel. Se a profundidade de uma imagem é 1, cada pixel pode ter 1 ou 2 valores, por exemplo preto ou branco, se for 4, cada pixel pode ter de 1 a 16 valores e assim por diante. A profundidade pode afetar muito a visibilidade da imagem como podemos observar na imagem abaixo:

![Cores](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Imagens/colodepths.png)

>Fonte: Processing: A Programming Handbook for Visual Designers

Imagens digitais são compostas por números representando cores. O formato de arquivo  de uma imagem determina como os números são organizados no arquivo. Processing pode carregar imagens GIF, JPEG e PNG. Quando se utiliza imagens na internet, devemos ficar atentos a algumas informações quando a compreensão, por exemplo: Imagens no formato .GIF são indicadas para ilustrar gráficos simples com um número limitado de cores e transparência. Imagens em PNG têm a mesma utilidade dos GIFs mas possuem um range maior de cor e transparência, JPEG trabalha bem com fotos e costuma ter um tamanho menor do que PNG, isso porque imagens em JPG sacrificam a qualidade  para reduzir seu tamanho.

Processing pode carregar imagens, mostrar na tela e mudar seu tamanho, posição, opacidade e matiz. Há um tipo de dado para imagem chamado ```PImage```. Da mesma forma que números inteiros são guardados em variáveis do tipo **int** e valores  **False** e **True** são guardados em variáveis do tipo boolean, tipos de dados de imagem são guardados em variáveis do tipo ```PImage```.

#### Adicionando uma imagem:

Para adicionar uma imagem selecione Scketch no meu e clique em adicionar ficheiro, em seguida navegue pelo explorador de arquivos do sistema operacional, localize a imagem que quer add,  clique nela e posteriormente em open, pronto sua imagem foi adicionada ao folder, para ter certeza que ela está lá, basta  selecionar “Show Scketch folder” no menu Sketch.  Se a imagem estiver lá, você poderá carregá-la utilizando a função image():

![Adicionando imagens](https://github.com/Evaldo-comp/Processing/blob/master/Java/Exemplos/Imagens/addimg.png)


##### Carregando uma imagem:



