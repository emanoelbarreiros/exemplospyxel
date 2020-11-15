import pyxel
import math

class Colisao:
    def __init__(self):
        pyxel.init(200, 200)
        self.x_rect = 30
        self.y_rect = 30
        self.largura = 40
        self.altura = 40
        self.raio = 10
        self.colidiu = False
        pyxel.run(self.update, self.draw)

    def update(self):
        self.colidiu = self.detectar_colisao(self.x_rect, self.y_rect, self.largura, self.largura, pyxel.mouse_x, pyxel.mouse_y, self.raio)

    def draw(self):
        pyxel.cls(6)
        pyxel.rect(self.x_rect, self.y_rect, self.largura, self.altura, 5)
        
        cor = 15
        if self.colidiu:
            cor = 8
        
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, self.raio, cor)
        

    def detectar_colisao(self, x1, y1, l1, a1, x2, y2, r):
        teste_x = x2
        teste_y = y2
        if x2 < x1:
            teste_x = x1
        elif x2 > x1 + l1:
            teste_x = x1 + l1
        
        if y2 < y1:
            teste_y = y1
        elif y2 > y1 + a1:
            teste_y = y1 + a1

        dist_x = x2 - teste_x
        dist_y = y2 - teste_y
        distancia = math.sqrt(dist_x**2 + dist_y**2)

        if distancia <= r:
            return True

        return False

Colisao()