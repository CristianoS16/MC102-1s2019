# verificar se um numero e perfeito 
a = int(input())
cont = 0
i = 1
while i < (a+1)/2:
	if a%i == 0: 
		cont = cont + i
	i = i + 1
if cont == a: 
	print (" a e perfeito" )

