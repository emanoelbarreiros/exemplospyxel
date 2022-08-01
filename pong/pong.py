import pyxel
import random
import math

JOGANDO = 1
VITORIA = 2

class Pong:
    def __init__(self):
        pyxel.init(150, 100, title="Pong", fps=30)
        pyxel.load("pong.pyxres")
        self.altura = 20
        self.largura = 5
        self.esquerda_x = 5
        self.esquerda_y = pyxel.height/2 - self.altura/2
        self.bola_x = pyxel.width/2
        self.bola_y = pyxel.height/2
        self.vel_x = 4
        self.vel_y = 2
        self.pontos_1 = 0
        self.pontos_2 = 0
        self.vel_linear = 3
        self.modo = JOGANDO
        self.vitorioso = 0
        self.ponto_vitoria = 2
        self.direita_x = pyxel.width - (5 + self.largura)
        self.direita_y = pyxel.height/2 - self.altura/2
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        if self.modo == JOGANDO:
            if pyxel.btn(pyxel.KEY_A):
                self.esquerda_y -= 5
                if self.esquerda_y < 0:
                    self.esquerda_y = 0

            if pyxel.btn(pyxel.KEY_Z):
                self.esquerda_y += 5
                if self.esquerda_y > pyxel.height - self.altura:
                    self.esquerda_y = pyxel.height - self.altura

            if pyxel.btn(pyxel.KEY_UP):
                self.direita_y -= 5
                if self.direita_y < 0:
                    self.direita_y = 0

            if pyxel.btn(pyxel.KEY_DOWN):
                self.direita_y += 5
                if self.direita_y > pyxel.height - self.altura:
                    self.direita_y = pyxel.height - self.altura

            # movimentar a bola
            self.bola_x += self.vel_x
            self.bola_y += self.vel_y
            #parede superior
            if self.bola_y <= 0:
                self.bola_y = 0
                self.vel_y = -self.vel_y
                pyxel.play(0,0)

            #parede inferior
            if self.bola_y >= pyxel.height - 8:
                self.bola_y = pyxel.height - 8
                self.vel_y = -self.vel_y
                pyxel.play(0,0)

            #parede esquerda
            if self.bola_x <= 0:
                self.pontos_2 += 1
                self.bola_x = pyxel.width / 2
                self.bola_y = pyxel.height / 2
                angulo = random.randint(20, 60)
                self.vel_x = round(self.vel_linear * math.cos(math.radians(angulo)))
                direcao = random.choice([-1,1])
                self.vel_y = direcao * round(self.vel_linear * math.sin(math.radians(angulo)))
                pyxel.play(0,0)

            #parede direita
            if self.bola_x >= pyxel.width - 8:
                self.pontos_1 += 1
                self.bola_x = pyxel.width / 2
                self.bola_y = pyxel.height / 2
                angulo = random.randint(20, 60)
                self.vel_x = -round(self.vel_linear * math.cos(math.radians(angulo)))
                direcao = random.choice([-1,1])
                self.vel_y = direcao * round(self.vel_linear * math.sin(math.radians(angulo)))
                pyxel.play(0,0)

            #checando colisao com a plataforma esquerda
            if self.detectar_colisao(self.esquerda_x, self.esquerda_y, self.largura, self.altura, self.bola_x, self.bola_y, 8, 8):
                self.vel_x = -self.vel_x
                self.bola_x = self.esquerda_x + self.largura
                pyxel.play(0,0)

            #checando colisao com a plataforma direita
            if self.detectar_colisao(self.direita_x, self.direita_y, self.largura, self.altura, self.bola_x, self.bola_y, 8, 8):
                self.vel_x = -self.vel_x
                self.bola_x = self.direita_x - 8
                pyxel.play(0,0)

            # checar a condicao de vitoria
            if self.pontos_1 == self.ponto_vitoria:
                self.vitorioso = 1
                self.modo = VITORIA
            if self.pontos_2 == self.ponto_vitoria:
                self.vitorioso = 2
                self.modo = VITORIA

    def desenhar(self):
        pyxel.cls(0)
        pyxel.rect(self.esquerda_x, self.esquerda_y, self.largura, self.altura, 7)
        pyxel.rect(self.direita_x, self.direita_y, self.largura, self.altura, 7)
        pyxel.blt(self.bola_x, self.bola_y, 0, 8, 0, 8, 8, 0)
        pyxel.text(pyxel.width/2 - 8, 5, str(self.pontos_1), 7)
        pyxel.text(pyxel.width/2 + 5, 5, str(self.pontos_2), 7)
        if self.modo == VITORIA:
            pyxel.text(pyxel.width/2 - 40, pyxel.height/2 - 20, "VITORIA DO JOGADOR " + str(self.vitorioso), 7)

    @staticmethod
    def detectar_colisao(x1, y1, l1, a1, x2, y2, l2, a2):
        if x1 < x2 + l2 and x1 + l1 > x2 and y1 < y2 + a2 and y1 + a1 > y2:
            return True
        else:
            return False

Pong()