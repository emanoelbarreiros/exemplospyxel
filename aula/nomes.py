# nomes = ["João", "Fernando", "José"]

# for nome in nomes:
#     print("Olá", nome, "prazer em conhece-lo.")

nomes = ["João", "Ferreira", "Fernando", "Pereira", "José", "Silva", "Paolo", "Antony"]

for indice in range(0, len(nomes), 2):
    print("Olá", nomes[indice], nomes[indice + 1], "prazer em conhece-lo.")

#nomes.sort()
print(nomes)

novaLista = sorted(nomes)
print(novaLista)
print(nomes)