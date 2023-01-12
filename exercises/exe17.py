#Recebe 10 inteiro, cria uma lista e encontra numeros da lista que multiplicados resultem em c
x = []
d = False
for i in range(10):
    x.insert(i, float(input("lista de 10 numeros: ")))

c = int(input("Resultado procurado: "))

for i in range(10):
    for j in range(i,10):
        if x[i] * x[j] == c:
            print(x[i], "x", x[j], "=", c)
            d = True
if d == False:
    print("Não existem numeros na lista que multiplicados deem c")

