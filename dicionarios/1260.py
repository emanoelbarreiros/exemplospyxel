n = int(input())

entradas = []

input()
for i in range(n):
    soma = 0
    dic = {}
    porc = {}

    while True:
        try:
            arvore = input()
        except:
            break
        if arvore == "":
            break
        cont = dic.get(arvore, 0)
        cont+=1
        dic[arvore] = cont
    for x in dic.values():
        soma +=x
    tree = list(dic)
    tree.sort()
    for y in tree:
        porc[y] = f"{y} {dic[y]/soma*100:.4f}"
    
    entradas.append(porc)
    
for i in range(len(entradas)):
    for p in entradas[i].values():
        print(f"{p}")
    if i != len(entradas) - 1:
        print()