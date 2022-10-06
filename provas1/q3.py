def resolve_equacao(c1, c2):
    x = -c1 / c2
    return x

def resolve_equacoes(lista):
    resultados = []

    for coefs in lista:
        x, y = coefs
        res = resolve_equacao(x, y)
        resultados.append(res)

    return resultados

res = resolve_equacoes([ [3, -2], [-4, 2], [10, 5] ])
print(res)
