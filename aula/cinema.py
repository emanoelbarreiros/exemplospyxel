pessoas = int(input("Quantas pessoas desejam ir ao cinema? "))

idadesObtidas = 0
valorASerPago = 0
while idadesObtidas < pessoas:
    idade = int(input("Digite idade: "))

    if idade>= 3 and idade < 12:
        valorASerPago += 10
    elif idade >= 12:
        valorASerPago += 20

    idadesObtidas += 1

print("Valor total a ser pago: R$ %d,00" % valorASerPago)