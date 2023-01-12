#Verifica se os numeros digitados então em ordem, usando variavel contadora 
cont = int(input("Número de numeros a serem digitados: "))
ant = int(input())
i = 0
a = 0
n = 0
while a<cont-1:
	n = int(input())
	if ant > n:
		i = i + 1
		a = a + 1		
		ant = n
	else:
		a = a + 1
		ant = n
if i != 0:
	print("fora de ordem")
else: 
	print("sequencia ordenada")
