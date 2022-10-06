saida = []
while True:
    entrada = input()
    if entrada.strip() == "0 0 0":
        break

    p,a,r = entrada.split()

    perolas = []
    respostas = {}

    for i in range(int(p)):
        perola = input()
        perolas.append(perola)

    for i in range(int(a)):
        nome = input()
        if nome not in respostas:
            respostas[nome] = []
            for q in range(int(r)):
                resposta = input()
                respostas[nome].append(resposta)
        else:
            for q in range(int(r)):
                input()

    contagem = {}
    for nome,l in respostas.items():
        cont = 0
        for resposta in l:
            if resposta in perolas:
                cont += 1
        contagem[nome] = cont

    maior = sorted(list(contagem.values()))[-1]

    nomes = []
    for k,v in contagem.items():
        if v == maior:
            nomes.append(k)

    nomes.sort()
    saida.append(", ".join(nomes))

for s in saida:
    print(s)