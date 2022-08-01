import pyxel
import random

PARADO = 0
CIMA = 1
BAIXO = 2
DIREITA = 3
ESQUERDA = 4

class Segmento:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.cobra = [Segmento(64,96), Segmento(56, 96), Segmento(48, 96)]
        self.direcao = DIREITA
        pyxel.init(160, 160, title="Snake", fps=60)
        self.comida_x = random.randrange(0, pyxel.width, 8)
        self.comida_y = random.randrange(0, pyxel.width, 8)
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        # define a nova direcao da cobra
        if pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
            self.direcao = DIREITA
        if pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
            self.direcao = ESQUERDA
        if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
            self.direcao = CIMA
        if pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
            self.direcao = BAIXO

        if pyxel.frame_count % 15 == 0:
            cabeca = self.cobra[0]
            novaCabeca = None
            # aplica a direcao desejada pelo jogador
            if self.direcao == DIREITA:
                novaCabeca = Segmento(cabeca.x + 8, cabeca.y)
            if self.direcao == ESQUERDA:
                novaCabeca = Segmento(cabeca.x - 8, cabeca.y)
            if self.direcao == CIMA:
                novaCabeca = Segmento(cabeca.x, cabeca.y - 8)
            if self.direcao == BAIXO:
                novaCabeca = Segmento(cabeca.x, cabeca.y + 8)
            if self.direcao == PARADO:
                novaCabeca = cabeca

            #checa se a cobra saiu pelas bordas
            if novaCabeca.x > (pyxel.width - 8):
                novaCabeca.x = 0
            if novaCabeca.x < 0:
                novaCabeca.x = pyxel.width - 8
            if novaCabeca.y < 0:
                novaCabeca.y = pyxel.height - 8
            if novaCabeca.y > (pyxel.height - 8):
                novaCabeca.y = 0

            self.cobra.pop()
            self.cobra.insert(0, novaCabeca)

            #checar se a cobra passou por cima da comida
            if self.comida_x == novaCabeca.x and self.comida_y == novaCabeca.y:
                self.comida_x = random.randrange(0, pyxel.width, 8)
                self.comida_y = random.randrange(0, pyxel.width, 8)

    def desenhar(self):
        pyxel.cls(11)
        for seg in self.cobra:
            pyxel.rect(seg.x, seg.y, 8, 8, 0)
        pyxel.rect(self.comida_x, self.comida_y, 8, 8, 8)

Snake()