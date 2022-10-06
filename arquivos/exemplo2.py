pi = ""
with open("digitospi_grande.txt") as arquivo:
    for linha in arquivo:
        pi += linha.rstrip()

if ("04101984" in pi):
    print("Seu aniversario está no PI.")
else:
    print("Sem aniversário no PI.")