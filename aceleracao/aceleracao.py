import pyxel
import euclid3 as eu

class Segmento:
    def __init__(self, x1, y1, x2, y2):
        self.linha = eu.LineSegment2(eu.Point2(x1, y1), eu.Point2(x2,y2))

    def pintar(self):
        pyxel.line(self.linha.p1.x, self.linha.p1.y, self.linha.p2.x, self.linha.p2.y, 8)
        
class Bola:
    def __init__(self, posicao, velocidade, aceleracao, coef_elastico = 0.9):
        self.raio = 10.0
        self.circulo = eu.Circle(eu.Point2(posicao.x, posicao.y), self.raio)
        self.posicao = posicao
        self.velocidade = velocidade
        self.aceleracao = aceleracao
        self.coef_elastico = coef_elastico
        self.permanecer = True

    def atualizar(self):
        self.velocidade += self.aceleracao
        self.posicao += self.velocidade
        self.checar_bordas()

    def checar_bordas(self):
        if self.posicao.x <= self.raio:
            self.posicao.x = 2*self.raio - self.posicao.x
            self.velocidade = self.velocidade.reflect(eu.Vector2(1,0)) * self.coef_elastico
        elif self.posicao.x > pyxel.width - self.raio:
            self.posicao.x = 2*(pyxel.width - self.raio) - self.posicao.x
            self.velocidade = self.velocidade.reflect(eu.Vector2(1,0)) * self.coef_elastico
        elif self.posicao.y <= self.raio:
            self.posicao.y = 2*self.raio - self.posicao.y
            self.velocidade = self.velocidade.reflect(eu.Vector2(0,1)) * self.coef_elastico
        elif self.posicao.y > pyxel.height + self.raio:
            self.permanecer = False

    def checar_colisao(self, objeto):
        if isinstance(objeto, Segmento):
            if self.posicao.distance(objeto.linha) <= self.raio:
                normal = self.posicao.connect(objeto.linha)
                vetor_normal = (normal.p1 - normal.p2).normalize()
                nova_posicao = normal.p2 + (vetor_normal * self.raio)
                self.posicao = eu.Point2(nova_posicao.x, nova_posicao.y)
                self.velocidade = self.velocidade.reflect(vetor_normal) * self.coef_elastico
        elif isinstance(objeto, Bola):
            if self.posicao.distance(objeto.posicao) <= self.raio + objeto.raio:
                diferenca = self.raio + objeto.raio - self.posicao.distance(objeto.posicao)
                vetor_colisao = self.posicao - objeto.posicao
                vetor_colisao.normalize()
                self.posicao = self.posicao + vetor_colisao*(diferenca/2)
                objeto.posicao = objeto.posicao - vetor_colisao*(diferenca/2)
                self.velocidade = self.velocidade.reflect(vetor_colisao) * self.coef_elastico
                objeto.velocidade = objeto.velocidade.reflect(vetor_colisao) * self.coef_elastico

    def pintar(self):
        pyxel.circb(self.posicao.x, self.posicao.y, self.raio, 0)

class Aplicacao:
    def __init__(self):
        pyxel.init(255, 255)
        pyxel.mouse(True)
        self.gravidade = eu.Vector2(0, 0.5)
        self.bolas = []
        self.segmentos = []
        self.segmentos.append(Segmento(10.0, 120.0, 140.0, 180.0))
        self.segmentos.append(Segmento(200.0, 120.0, 100.0, 90.0))
        self.segmentos.append(Segmento(240.0, 180.0, 160.0, 200.0))
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            bola = Bola(eu.Point2(pyxel.mouse_x, pyxel.mouse_y), eu.Vector2(0, 0), self.gravidade, 0.8)
            self.bolas.append(bola)

        for i, b in enumerate(self.bolas):
            b.atualizar()
            if b.permanecer:
                for s in self.segmentos:
                    b.checar_colisao(s)
                for b2 in self.bolas[i+1:]:
                    b.checar_colisao(b2)
            
        self.bolas = list(filter(lambda b: b.permanecer, self.bolas))

    def desenhar(self):
        pyxel.cls(7)
        for b in self.bolas:
            b.pintar()

        for s in self.segmentos:
            s.pintar()

Aplicacao()