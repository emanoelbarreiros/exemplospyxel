import pyxel

posicaoX = 0

def atualizar():
    pass

def desenhar():
    pyxel.cls(0)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 8, 2)

pyxel.init(100, 100, title="teste", fps=30)
pyxel.run(atualizar, desenhar)