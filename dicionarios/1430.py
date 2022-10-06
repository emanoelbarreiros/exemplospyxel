notas = {'W':1, 'H':0.5, 'Q':0.25, 'E':0.125, 'S':0.0625, 'T':0.03125, 'X':0.015625}

entrada = input()
while entrada != "*":
    compassos = entrada.split("/")[1:-1]

    qtdCompassosCorretos = 0

    for compasso in compassos:
        tempo = 0
        for letra in compasso:
            tempo += notas[letra]

        #aqui eu tenho o tempo do compasso
        if tempo == 1:
            qtdCompassosCorretos += 1

    print(qtdCompassosCorretos)

    entrada = input()