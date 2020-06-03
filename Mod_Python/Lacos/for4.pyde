def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5 + i * 5, 5+ i * 5)
        label = "{}: {}, {}".format(i, x, y)
        fill(0)
        text(label, x + 15, y)
