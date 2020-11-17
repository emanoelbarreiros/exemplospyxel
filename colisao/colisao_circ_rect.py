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
        self.x_prox = -1
        self.y_prox = -1
        pyxel.run(self.update, self.draw)

    def update(self):
        self.colidiu, self.x_prox, self.y_prox = self.detectar_colisao(self.x_rect, self.y_rect, self.largura, self.largura, pyxel.mouse_x, pyxel.mouse_y, self.raio)

    def draw(self):
        pyxel.cls(6)
        pyxel.rect(self.x_rect, self.y_rect, self.largura, self.altura, 5)
        
        cor = 15
        cor_ponto = 8
        if self.colidiu:
            cor = 8
            cor_ponto = 10
        
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, self.raio, cor)
        pyxel.circ(self.x_prox, self.y_prox, 1, cor_ponto)
        

    def detectar_colisao(self, x1, y1, l1, a1, x2, y2, r):
        x_ponto = x2
        y_ponto = y2
        if x2 < x1:
            x_ponto = x1
        elif x2 > x1 + l1:
            x_ponto = x1 + l1
        
        if y2 < y1:
            y_ponto = y1
        elif y2 > y1 + a1:
            y_ponto = y1 + a1

        dist_x = x2 - x_ponto
        dist_y = y2 - y_ponto
        distancia = math.sqrt(dist_x**2 + dist_y**2)

        if distancia <= r:
            return True, x_ponto, y_ponto

        return False, x_ponto, y_ponto

Colisao()