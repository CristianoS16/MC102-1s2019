#Recebe 10 inteiro, cria uma lista e dá a possição oculpada pelo maior numero
x = []
b = 0
for i in range(10):
    x.insert(i, int(input()))
a = x[0]
for i in range(10):
    y = x[i]
    if y > a:
        a = y
        b = i
print ("a possição do maior numero é:", x)
print (b)