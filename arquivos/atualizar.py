import os.path

nome = input("Informe o nome do arquivo: ")

if os.path.isfile(nome):
    print("Existe um arquivo com o nome informado.")
    print("Segue o conteúdo do arquivo:")
    with open(nome, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
else:
    print("O arquivo especificado não existe. Ele será criado.")

print("Digite algo para adicionar ao conteúdo do arquivo.")
with open(nome, "a") as arquivo:
    entrada = input()
    while entrada != "":
        arquivo.write("\n" + entrada)
        entrada = input()

print("O texto foi salvo no arquivo.")