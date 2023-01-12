#imprime uma sequencia de numeros crescente por cada linha.
a = int(input("Digite o número de linhas: "))
b = 1
while b <= a:
    for s in range(1,b+1):
        print (s," ", end="")
    b= b+1
    print("")
