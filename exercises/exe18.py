#Deve computar uma exponencial por meio de uma função e sem usar **

def exp(a,b):
    d = a
    i = 1
    if b == 0:
        return 1
    while i < b:
        a = a * d
        i += 1
    return a

a = int(input())
b = int(input())

c = exp(a,b)
print("Potencia é", c)

#programa para imprimir todas as potencias
#for j in range (2,11):
 #   for h in range (0,11):
  #      t = exp(j,h)
   #     print(t , end=" ")
    #print("")
