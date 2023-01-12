#Cristiano Sampaio Pinheiro ra256352	

c1 = int(input()) #Recebe peso carga 1
c2 = int(input()) #Recebe peso carda 2
c3 = int(input()) #Recebe peso carga 3
c4 = int(input()) #Recebe peso carga 4

if   c1 + c2 == c3 + c4: 	#Compara a soma de 2 cargas com a soma de outras 2 cargas 
	print("sim")		#Foi possivel distribuir o peso!
elif c1 + c3 == c2 + c4:	#Compara a soma de 2 cargas com a soma de outras 2 cargas
	print("sim")		#Foi possivel distribuir o peso!
elif c1 + c4 == c2 + c3:	#Compara a soma de 2 cargas com a soma de outras 2 cargas	
	print("sim")		#Foi possivel distribuir o peso!
elif c2 + c3 == c1 + c4: 	#Compara a soma de 2 cargas com a soma de outras 2 cargas 
	print("sim")		#Foi possivel distribuir o peso!
elif c1 == c2 + c3 + c4:	#Compara 1 valor com a soma dos outros 3 valores 
	print("sim")		#Foi possivel distribuir o peso!
elif c2 == c1 + c3 + c4:	#Compara 1 valor com a soma dos outros 3 valores 
	print("sim")		#Foi possivel distribuir o peso!
elif c3 == c1 + c2 + c4:	#Compara 1 valor com a soma dos outros 3 valores 
	print("sim")		#Foi possivel distribuir o peso!
elif c4 == c1 + c2 + c3:	#Compara 1 valor com a soma dos outros 3 valores 
	print("sim")		#Foi possivel distribuir o peso!
else: 			        #Nenhum dos casos anteriores foi satisfeito
	print("nao")		#Nenhum foi possivel distribuir o peso!

#Que a força estaja conosco 

