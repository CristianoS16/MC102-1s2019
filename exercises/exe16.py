#Recebe 10 inteiro, cria uma lista e dá a media desses numeros
x = []
acm = 0
for i in range(10):
    x.insert(i, float(input()))
a = x[0]
for i in range(10):
    acm = acm + x[i]
    i = i + 1
print ("A media é:", acm/10)
