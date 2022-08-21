class Complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)

    def __add__(self, outro):
        real = self.real + outro.real
        imag = self.imag + outro.imag
        return Complexo(real, imag)

    def __sub__(self, outro):
        real = self.real - outro.real
        imag = self.imag - outro.imag
        return Complexo(real, imag)

c = Complexo(2, 4) # 2 + 4i
j = Complexo(5, 2) # 5 + 2i

print(c)
print(j)

print(c + j)

novo2 = c - j + c
print(novo2)