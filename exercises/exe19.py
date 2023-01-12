# Consulta o fatorial de um numero recebido/ Entreda todos os fatoriais de 1 a 20

def fatorial(a):
    i = 1
    s = 1
    while i < a + 1:
        s = s * i
        i = i + 1
    return s

b = fatorial(int(input()))
print("O fatorial do numero é = ", b)

for j in range (1,20):
    c = fatorial(j)
    print (c , end=" ")
