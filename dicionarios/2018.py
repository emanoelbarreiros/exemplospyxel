
def atualizarEstatistica(estatisticas, medalha, pais):
    if pais in estatisticas:
        medalhas = estatisticas[pais]
        medalhas[medalha] += 1
    else:
        medalhas = [0,0,0]
        medalhas[medalha] += 1
        estatisticas[pais] = medalhas

def calcularRankingMedalha(estatistica):
    return (estatistica[1], estatistica[0])

def calcularRankingNome(estatistica):
    return estatistica[0]

OURO = 0
PRATA = 1
BRONZE = 2
estatisticas = {}
try:
    entrada = []
    while True:
        evento = input()
        for i in range(3):
            entrada.append(input())

        paisOuro, paisPrata, paisBronze = entrada
        entrada = []

        atualizarEstatistica(estatisticas, OURO, paisOuro)
        atualizarEstatistica(estatisticas, PRATA, paisPrata)
        atualizarEstatistica(estatisticas, BRONZE, paisBronze)
        
except:
    pass

ranking = list(estatisticas.items())

ranking.sort(reverse=True, key=calcularRankingMedalha)

rankingFinal = {}
for entrada in ranking:
    medalhas = entrada[1]
    pais = entrada[0]
    if tuple(medalhas) in rankingFinal.keys():
        rankingFinal[tuple(medalhas)].append(pais)
    else:
        rankingFinal[tuple(medalhas)] = [pais]

for medalhas in rankingFinal:
    rankingFinal[medalhas].sort()

print("Quadro de Medalhas")
for medalhas,paises in rankingFinal.items():
    for pais in paises:
        print(f"{pais} {medalhas[0]} {medalhas[1]} {medalhas[2]}")