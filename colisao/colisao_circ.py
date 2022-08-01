import pyxel
import math

class Circulos:
    def __init__(self):
        pyxel.init(200, 200)
        self.x = 50
        self.y = 50
        self.raio1 = 20
        self.raio2 = 10
        self.colidiu = False
        pyxel.run(self.update, self.draw)

    def update(self):
        self.colidiu = self.detectar_colisao(self.x, self.y, self.raio1, pyxel.mouse_x, pyxel.mouse_y, self.raio2)

    def draw(self):
        pyxel.cls(6)
        pyxel.circ(self.x, self.y, self.raio1, 5)
        
        cor = 15
        if self.colidiu:
            cor = 8
        
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, self.raio2, cor)
        

    def detectar_colisao(self, x1, y1, r1, x2, y2, r2):
        distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if distancia <= r1 + r2:
            return True
        else:
            return False

Circulos()