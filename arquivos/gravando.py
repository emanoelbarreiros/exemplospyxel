import os.path

nomeArquivo = input("Nome do arquivo: ")
print("Escreva linhas a serem escritas no arquivo.")
print("Pressione Enter com uma linha em branco para finalizar.")
print()
with open(nomeArquivo, 'w') as arquivo:
    entrada = input()
    while entrada != "":
        arquivo.write(entrada + '\n')
        entrada = input()

print()
print("Os dados foram salvos no arquivo.")

os.path.isfile('nomedoarquivo.txt')