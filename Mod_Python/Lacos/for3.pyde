def setup():
    size(400, 400)
    pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
    for t in pontos:
        x, y = t
        ellipse(x, y, 15, 15)
