with open("digitospi.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


with open("digitospi.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.rstrip())