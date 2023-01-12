#Cristiano Sampaio Pinheiro ra256352	
c = int(input())	#Capacidade do estacionamento
v = 1			#Guarda tamanho do veiculo
a = c			#Acumuladora do espaço do estacionamento	
while v != 0: 		#Faz leitura ate receber valor 0
	v = int(input())	#Leitura do tamanho do carro
	if v>0: 		#Verifica se o carro está entrando
		if v<=a:	#Verifica se o tem espaço para esse carro
			a = a - v	#Desnconta espaço oculpado por esse carro
			print("Seja bem-vindo! Capacidade restante:", a)   
		else:			#Para quando nao há espaço para esse carro
			print("Veiculo muito grande! Capacidade restante:", a)
	if v<0:			#Verifica se o carro esta saindo
			a = a - v	#Desconta espaço desoculpado por esse carro
			print("Volte sempre! Capacidade restante:", a)
#Que a força esteja conosco
