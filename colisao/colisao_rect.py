import pyxel

class Retangulos:
    def __init__(self):
        pyxel.init(200, 200)
        self.x = 30
        self.y = 30
        self.largura = 40
        self.altura = 20
        self.colidiu = False
        pyxel.run(self.update, self.draw)

    def update(self):
        self.colidiu = self.detectar_colisao(self.x, self.y, self.largura, self.largura, pyxel.mouse_x, pyxel.mouse_y, self.largura, self.altura)

    def draw(self):
        pyxel.cls(6)
        pyxel.rect(self.x, self.y, self.largura, self.largura, 5)
        
        cor = 15
        if self.colidiu:
            cor = 8
        
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, self.largura, self.altura, cor)
        

    def detectar_colisao(self, x1, y1, l1, a1, x2, y2, l2, a2):
        if x1 < x2 + l2 and x1 + l1 > x2 and y1 < y2 + a2 and y1 + a1 > y2:
            return True
        else:
            return False

Retangulos()