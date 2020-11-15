import pyxel

class Bola:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.raio = 10
        self.velocidade_x = vel_x
        self.velocidade_y = vel_y

class Jogo:
    def __init__(self):
        pyxel.init(200, 200)
        self.bolas = []
        pyxel.mouse(True)
        self.click_down = None
        pyxel.run(self.update, self.draw)        

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.click_down = (pyxel.mouse_x, pyxel.mouse_y)
        
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            delta_x = self.click_down[0] - pyxel.mouse_x
            delta_y = self.click_down[1] - pyxel.mouse_y
            bola = Bola(pyxel.mouse_x, pyxel.mouse_y, delta_x//8, delta_y//8)
            self.bolas.append(bola)
            self.click_down = None

        for bola in self.bolas:
            bola.x += bola.velocidade_x
            bola.y += bola.velocidade_y

            if bola.x + bola.raio >= pyxel.width:
                bola.x = pyxel.width - bola.raio - 1
                bola.velocidade_x = -bola.velocidade_x

            if bola.x - bola.raio <= 0:
                bola.x = bola.raio + 1
                bola.velocidade_x = -bola.velocidade_x

            if bola.y + bola.raio >= pyxel.height:
                bola.y = pyxel.height - bola.raio - 1
                bola.velocidade_y = -bola.velocidade_y

            if bola.y - bola.raio <= 0:
                bola.y = bola.raio + 1
                bola.velocidade_y = -bola.velocidade_y
        

    def draw(self):
        pyxel.cls(1)
        if self.click_down is not None:
            pyxel.line(self.click_down[0], self.click_down[1], pyxel.mouse_x, pyxel.mouse_y, 7)
            pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 10, 10)

        for bola in self.bolas:
            pyxel.circ(bola.x, bola.y, bola.raio, 10)


Jogo()