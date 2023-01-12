#Encontrar numeros triangulares 
a = int(input())
cont = 0
i = 1
while i < a:
	cont = cont + i
	i = i + 1
	if cont == a:
		print("a é triangular")   
		break
