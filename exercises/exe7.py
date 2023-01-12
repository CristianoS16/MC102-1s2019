#Mostra a soma linha por linha dos numeros no intervalo [1,n], 
n = int(input())
i = 0
s = 0 

while i < n+1:
	s = s + i
	i = i + 1
	print("Soma dos numeros de 1 ate", i-1, "=", s) 
 
