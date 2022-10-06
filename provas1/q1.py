while True:
    expr = input("Informe uma expressão numérica: ").split()

    op1 = float(expr[0])
    operador = expr[1]
    op2 = float(expr[2])

    resultado = "não calculado"
    if operador == "+":
        resultado = op1 + op2
    elif operador == "-":
        resultado = op1 - op2
    elif operador == "*":
        resultado = op1 * op2
    elif operador == "/":
        resultado = op1 / op2

    print(resultado)