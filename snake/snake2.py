import pyxel
import random

PARADO = 0
CIMA = 1
BAIXO = 2
DIREITA = 3
ESQUERDA = 4

CAB_ESQUERDA = (8,0)
CAB_DIREITA = (0,8)
CAB_BAIXO = (16,8)
CAB_CIMA = (8,8)
CORPO_V = (24,0)
CORPO_H = (16,0)
CURVA_BAIXO_DIR = (24,8)
CURVA_BAIXO_ESQ = (32,0)
CURVA_CIMA_DIR =  (32,8)
CURVA_CIMA_ESQ = (40,0)

class Segmento:
    def __init__(self, x, y, tipo=CORPO_H):
        self.x = x
        self.y = y
        self.tipo = tipo

    def __eq__(self, obj):
        return self.x == obj[0] and self.y == obj[1]

class Snake:
    def __init__(self):
        pyxel.init(160, 160, title="Snake", fps=60)
        self.cobra = [Segmento(64,96, CAB_DIREITA), Segmento(56, 96), Segmento(48, 96)]
        self.direcao = DIREITA
        self.novaDirecao = DIREITA
        self.direcaoAnterior = DIREITA
        self.comida_x = random.randrange(0, pyxel.width, 8)
        self.comida_y = random.randrange(0, pyxel.width, 8)
        self.engolida = []
        pyxel.load("snake2.pyxres")
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        # define a nova direcao da cobra
        if pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
            self.novaDirecao = DIREITA
        if pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
            self.novaDirecao = ESQUERDA
        if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
            self.novaDirecao = CIMA
        if pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
            self.novaDirecao = BAIXO

        if pyxel.frame_count % 15 == 0:
            self.direcaoAnterior = self.direcao
            self.direcao = self.novaDirecao
            cabeca = self.cobra[0]
            novaCabeca = None
            if self.direcao != PARADO:
                # aplica a direcao desejada pelo jogador
                if self.direcao == DIREITA:
                    novaCabeca = Segmento(cabeca.x + 8, cabeca.y, CAB_DIREITA)
                if self.direcao == ESQUERDA:
                    novaCabeca = Segmento(cabeca.x - 8, cabeca.y, CAB_ESQUERDA)
                if self.direcao == CIMA:
                    novaCabeca = Segmento(cabeca.x, cabeca.y - 8, CAB_CIMA)
                if self.direcao == BAIXO:
                    novaCabeca = Segmento(cabeca.x, cabeca.y + 8, CAB_BAIXO)

                #determina a forma do pescoço
                if self.direcao != self.direcaoAnterior:
                    if self.direcaoAnterior == CIMA:
                        if self.direcao == DIREITA:
                            cabeca.tipo = CURVA_BAIXO_DIR
                        if self.direcao == ESQUERDA:
                            cabeca.tipo = CURVA_BAIXO_ESQ
                    if self.direcaoAnterior == BAIXO:
                        if self.direcao == DIREITA:
                            cabeca.tipo = CURVA_CIMA_DIR
                        if self.direcao == ESQUERDA:
                            cabeca.tipo = CURVA_CIMA_ESQ
                    if self.direcaoAnterior == ESQUERDA:
                        if self.direcao == CIMA:
                            cabeca.tipo = CURVA_CIMA_DIR
                        if self.direcao == BAIXO:
                            cabeca.tipo = CURVA_BAIXO_DIR
                    if self.direcaoAnterior == DIREITA:
                        if self.direcao == CIMA:
                            cabeca.tipo = CURVA_CIMA_ESQ
                        if self.direcao == BAIXO:
                            cabeca.tipo = CURVA_BAIXO_ESQ
                else:
                    if self.direcao == ESQUERDA or self.direcao == DIREITA:
                        self.cobra[0].tipo = CORPO_H
                    else:
                        self.cobra[0].tipo = CORPO_V

                #checa se a cobra saiu pelas bordas
                if novaCabeca.x >= pyxel.width:
                    novaCabeca.x = 0
                if novaCabeca.x < 0:
                    novaCabeca.x = pyxel.width - 8
                if novaCabeca.y < 0:
                    novaCabeca.y = pyxel.height - 8
                if novaCabeca.y >= pyxel.height:
                    novaCabeca.y = 0

                #checar se a cobra passou por cima da comida
                if self.comida_x == novaCabeca.x and self.comida_y == novaCabeca.y:
                    self.engolida.append((self.comida_x, self.comida_y))                                                      
                    self.comida_x = random.randrange(0, pyxel.width, 8)
                    self.comida_y = random.randrange(0, pyxel.width, 8)      
                else:
                    self.cobra.pop()

                novoEngolida = []
                print(self.engolida)
                for engolida in self.engolida:
                    if self.ehCorpo(engolida):
                        novoEngolida.append(engolida)

                self.engolida = novoEngolida

                self.cobra.insert(0, novaCabeca)

    def ehCorpo(self, t):
        for seg in self.cobra:
            if seg.x == t[0] and seg.y == t[1]:
                return True
        
        return False
                

    def desenhar(self):
        pyxel.cls(11)

        for engolida in self.engolida:
            pyxel.circ(engolida[0], engolida[0], 3, 0)

        for seg in self.cobra:            
            pyxel.blt(seg.x, seg.y, 0, seg.tipo[0], seg.tipo[1], 8, 8, 7)
            #pyxel.rect(seg.x, seg.y, 8, 8, 0)
        
        pyxel.blt(self.comida_x, self.comida_y, 0, 40, 8, 8, 8, 0)

Snake()