def primo(x):
    divisores = []
    for v in range(1,x+1):
        if x % v == 0:
            divisores.append(v)

    #divisores = [v for v in range(1,x+1) if x % v == 0]

    return [1,x] == divisores

primos = [x for x in range(1,501) if primo(x)]

print(primos)
