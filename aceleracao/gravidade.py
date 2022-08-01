import pyxel

class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 10
        self.velocidade = 0

class Jogo:
    def __init__(self):
        pyxel.init(200, 200)
        self.gravidade = 1
        self.bolas = []
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            bola = Bola(pyxel.mouse_x, pyxel.mouse_y)
            self.bolas.append(bola)

        for bola in self.bolas:
            bola.velocidade += self.gravidade
            bola.y += bola.velocidade
            if bola.y + bola.raio >= pyxel.height:
                bola.y = pyxel.height - bola.raio - 1
                bola.velocidade = -bola.velocidade

    def draw(self):
        pyxel.cls(1)
        for bola in self.bolas:
            pyxel.circ(bola.x, bola.y, bola.raio, 8)

Jogo()