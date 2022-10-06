t = int(input())
traducoes = []
for v in range(t):
    frases = {}
    m, n = input().split()
    for x in range(int(m)):
        jap = input()
        trad = input()
        frases[jap]=trad
    for b in range(int(n)):
        texto = input().split()
        traducao = []
        for palavra in texto:
            traducao.append(frases.get(palavra, palavra))
        traducoes.append(" ".join(traducao))
    traducoes.append("")

for trad in traducoes:
    print(trad) 