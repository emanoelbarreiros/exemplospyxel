idas = int(input())
catalogo = {}
for i in range(idas):
    qtdProdutos = int(input())
    for j in range(qtdProdutos):
        produto, preco = input().split()
        catalogo[produto] = float(preco)

    subtotal = 0
    qtdComprar = int(input())
    for k in range(qtdComprar):
        produto, qtd = input().split()
        subtotal += catalogo[produto] * int(qtd)

    print(f"R$ {subtotal:.2f}")
