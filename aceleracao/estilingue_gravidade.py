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
        pyxel.mouse(True)
        self.bolas = []
        self.ponto_clique = None
        self.gravidade = 1
        self.coeficiente_restituicao = 0.9
        pyxel.run(self.update, self.draw)     

    def tratar_interacao_usuario(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.ponto_clique = (pyxel.mouse_x, pyxel.mouse_y)
        
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            delta_x = self.ponto_clique[0] - pyxel.mouse_x
            delta_y = self.ponto_clique[1] - pyxel.mouse_y
            bola = Bola(pyxel.mouse_x, pyxel.mouse_y, delta_x//3, delta_y//3)
            self.bolas.append(bola)
            self.ponto_clique = None   

    def update(self):
        self.tratar_interacao_usuario()

        for bola in self.bolas:
            bola.x += bola.velocidade_x
            bola.velocidade_y += self.gravidade
            bola.y += bola.velocidade_y            

            if bola.x + bola.raio >= pyxel.width:
                bola.x = pyxel.width - bola.raio - 1
                bola.velocidade_x = int(-bola.velocidade_x * self.coeficiente_restituicao)

            if bola.x - bola.raio <= 0:
                bola.x = bola.raio + 1
                bola.velocidade_x = int(-bola.velocidade_x * self.coeficiente_restituicao)

            if bola.y + bola.raio >= pyxel.height:
                bola.y = pyxel.height - bola.raio - 1
                bola.velocidade_y = int(-bola.velocidade_y * self.coeficiente_restituicao)            

            if bola.y - bola.raio <= 0:
                bola.y = bola.raio + 1
                bola.velocidade_y = int(-bola.velocidade_y * self.coeficiente_restituicao)

            if abs(bola.y + bola.raio - pyxel.height) < 2:
                bola.velocidade_x *= 0.9
        

    def draw(self):
        pyxel.cls(1)
        if self.ponto_clique is not None:
            pyxel.line(self.ponto_clique[0], self.ponto_clique[1], pyxel.mouse_x, pyxel.mouse_y, 7)
            pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 10, 10)
            pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, 10, 9)

        for bola in self.bolas:
            pyxel.circ(bola.x, bola.y, bola.raio, 10)
            pyxel.circb(bola.x, bola.y, bola.raio, 9)


Jogo()