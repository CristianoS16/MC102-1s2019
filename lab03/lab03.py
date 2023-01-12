#Cristiano Sampaio Pinheiro ra256352	
d = float(input()) #Recebe o diametro do tanque
h = float(input()) #Recebe o comprimento do tanque 
a = float(input()) #Recebe demanda do posto A
b = float(input()) #Recebe demanda do posto B 
c = float(input()) #Recebe demanda do posto C

v = 3.14*(d/2)*(d/2)*h  #Calcula o volume de combustivel em m²
l = v*1000              #Converte de m² para litros

if l > a:	        #Compara combustivel disponivel com o requerido pelo posto A
	print("posto A foi reabastecido")
	l = l-a         #Desconta o combustivel deixado em A	
else:			#Combustivel disponivel não é suficiente para o posto A	
	print("posto A nao foi reabastecido")	  
if l > b:		#Compara combustivel disponivel com o requerido pelo posto B
	print("posto B foi reabastecido")	
	l = l-b		#Desconta combustivel deixado em B
else:	        	#Combustivel disponivel não é suficiente para o posto B
	print("posto B nao foi reabastecido")
if l > c:		#Compara combustivel disponivel com o requerido pelo posto C
	print("posto C foi reabastecido")
	l = l-c		#Desconta combustivel deixado em C
else:			#Combustivel disponivel não é suficiente para o posto C
	print("posto C nao foi reabastecido")
#Que a força esteja com João
