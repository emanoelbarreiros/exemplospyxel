
valorASerPago = 0
while True:
    entrada = input("Digite idade: ")

    if entrada == "sair":
        break

    idade = int(entrada)

    if idade>= 3 and idade < 12:
        valorASerPago += 10
    elif idade >= 12:
        valorASerPago += 20

print("Valor total a ser pago: R$ %d,00" % valorASerPago)