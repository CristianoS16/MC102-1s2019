#Cristiano Sampaio Pinheiro ra256352	
#Programa para indicar se é possivel fugir antes do escudo parar de funcionar.
t = int(input())	#Tempo de escudo restante 
c = int(input())	#Quantidade de combustivel necessaria para entra em dobra 
f = input()		#Fluxo de combustivel ou antimateria a cada segundo
s = 0			#Acumuladora da soma do fluxo de combustivel 
a = 0			#Guarda valor inteiro dos numeros lidos em f
l = f.split()		#Lista de valores lidos em str

for i in range(len(l)):		#Repete para o numero de elementos da lista, lido por lin 		
	a = int(l[i])		#converte o numero da possição i para inteiro
	s = s + a		#Acumula o a soma do fluxo de combustivel 
	if s>=c:		#Analisa se o combustivel será o bastante para fugir 
		print("sim")	
		print(i+1)	#Soma 1 para mostra o momento da fuga
		break		#Sai do laço, pois a fuga foi possivel 
	else: 
		i+1		#Soma 1 para continuar com o laço
		
if s<c:				#Analisa que a nave foi destruida
	print("nao")
	print(t+1)		#instante que a nave e destruida, 1 instante apos o escudo parar 
#Vida longa e prospera
#Que a força esteja conosco
