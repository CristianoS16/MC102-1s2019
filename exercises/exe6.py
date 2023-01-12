#Imprimir divisores de n maiores que 2
a = int(input())
i = 0
d = 2	
while d<a:
	if a%d == 0:
		print(d)
	d = d+1
