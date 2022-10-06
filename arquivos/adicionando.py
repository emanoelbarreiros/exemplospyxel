import os.path

print("Este programa lê o conteúdo de um arquivo e permite que texto seja adicionado.")
print("Pressione Enter com uma linha em branco para finalizar.")
print()
nomeArquivo = input("Nome do arquivo a ser aberto: ")

if os.path.isfile(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo abaixo:")
        print(conteudo)
else:
    print(f"O arquivo não existe. Um arquivo chamado {nomeArquivo} será criado.")
    print("Escreva abaixo o que você deseja incluir no arquivo.")

with open(nomeArquivo, 'a') as arquivo:
    entrada = input()
    while entrada != "":
        arquivo.write(entrada + '\n')
        entrada = input()

print()
print("Os dados foram salvos no arquivo.")