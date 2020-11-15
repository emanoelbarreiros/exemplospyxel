import pyxel
from euclid3 import Point2, Vector2, Geometry
  

class Jogador:
    def __init__(self, posicao, velocidade):
        self.posicao = posicao
        self.velocidade_x = velocidade.x
        self.velocidade_y = velocidade.y
        self.velocidade_maxima = 2
        self.aceleracao = 1
        # +2 e +7 no bounding box pq estamos tentando criar um retangulo interno dentro do sprite
        self.offset_caixa_x = 2
        self.largura_sprite = 3
        self.offset_caixa_y = 0
        self.altura_sprite = 8
        self.tamanho_tile = 8
        self.tile = Vector2(int(self.posicao.x // self.tamanho_tile), int(self.posicao.y // self.tamanho_tile))
    
    def update(self):
        self.velocidade_y = min(self.velocidade_y + self.aceleracao, self.velocidade_maxima) 
        posicao_pretendida = self.posicao + Vector2(self.velocidade_x, self.velocidade_y)
        impedido = True
        while impedido:  
            impedido = False          
            tile_jogador_x, tile_jogador_y = self.obter_coordenada_tile(posicao_pretendida.x, posicao_pretendida.y)
            
            #tile direita            
            x_tile, y_tile = self.obter_x_y(tile_jogador_x + 1, tile_jogador_y)
            if self.eh_solido(x_tile, y_tile) and self.colidiu(posicao_pretendida.x + self.offset_caixa_x, 
                    posicao_pretendida.y + self.offset_caixa_y, self.largura_sprite, self.altura_sprite,x_tile, y_tile, self.tamanho_tile, self.tamanho_tile):
                posicao_pretendida += Vector2(-1, 0)
                impedido = True
                continue

            #tile esquerda
            x_tile, y_tile = self.obter_x_y(tile_jogador_x - 1, tile_jogador_y)
            if self.eh_solido(x_tile, y_tile) and self.colidiu(posicao_pretendida.x + self.offset_caixa_x, 
                    posicao_pretendida.y + self.offset_caixa_y, self.largura_sprite, self.altura_sprite,
                x_tile, y_tile, self.tamanho_tile, self.tamanho_tile):
                posicao_pretendida += Vector2(1, 0)
                impedido = True
                continue

            #tile superior
            x_tile, y_tile = self.obter_x_y(tile_jogador_x, tile_jogador_y - 1)
            if self.eh_solido(x_tile, y_tile) and self.colidiu(posicao_pretendida.x + self.offset_caixa_x, 
                    posicao_pretendida.y + self.offset_caixa_y, self.largura_sprite, self.altura_sprite,
                x_tile, y_tile, self.tamanho_tile, self.tamanho_tile):
                posicao_pretendida += Vector2(0, 1)
                impedido = True
                continue

            #tile inferior
            x_tile, y_tile = self.obter_x_y(tile_jogador_x, tile_jogador_y + 1)
            if self.eh_solido(x_tile, y_tile) and self.colidiu(posicao_pretendida.x + self.offset_caixa_x, 
                    posicao_pretendida.y + self.offset_caixa_y, self.largura_sprite, self.altura_sprite,
                x_tile, y_tile, self.tamanho_tile, self.tamanho_tile):
                posicao_pretendida += Vector2(0, -1)
                impedido = True
                continue
            
        self.posicao = posicao_pretendida


    def draw(self):        
        pyxel.blt(self.posicao.x, self.posicao.y, 0, 0, 8, 8, 8, 0)

    def colidiu(self, x1, y1, l1, a1, x2, y2, l2, a2):
        if x1 < x2 + l2 and x1 + l1 > x2 and y1 < y2 + a2 and y1 + a1 > y2:
            return True
        else:
            return False

    def obter_x_y(self, x_tile, y_tile):
        return (x_tile * self.tamanho_tile, y_tile * self.tamanho_tile)

    def obter_coordenada_tile(self, x, y):
        return (int(x // self.tamanho_tile), int(y // self.tamanho_tile))

    def eh_solido(self, x_tile, y_tile):
        return pyxel.tilemap(0).get(x_tile, y_tile) == 1


class Jogo:
    def __init__(self):
        pyxel.init(128,128)
        self.posicao = Vector2(0,0)
        pyxel.mouse(True)
        pyxel.load('mapa.pyxres')
        self.tipo_tile = None
        self.jogador = Jogador(Vector2(10,10), Vector2(0,1))
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.jogador.posicao += Vector2(-2, 0)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.jogador.posicao += Vector2(2, 0)        
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.jogador.velocidade_y = -10

        self.jogador.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        #self.jogador.draw()     
        if self.tipo_tile is not None:
            pyxel.text(0, 0, str(self.tipo_tile), 7)

        posicao_mouse = '(' + str(self.posicao.x) + ', ' + str(self.posicao.y) + ')'
        pyxel.text(0, 8, str(posicao_mouse), 7)
        self.jogador.draw()

Jogo()