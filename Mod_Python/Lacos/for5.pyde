#primeiramente a execução de uma sequencia sem laço

size(480, 120)
strokeWeight(8)
line(20, 40, 80, 80)
line(80, 40, 140, 80)
line(140, 40, 200, 80)
line(200, 40, 260, 80)
line(260, 40, 320, 80)
line(320, 40, 380, 80)
line(380, 40, 440, 80) 

#O mesmo código acima, só que utiliznado um laço for

size(480, 120)
strokeWeight(8)
for i in range(20, 400, 60):
    line(i, 40, i + 60, 80)
