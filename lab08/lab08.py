# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve contabilizar os danos recebido por dois jogadores em uma luta do Street Fighter, levando com conta os combos de golpes, e no final apresentar o ganhador.

Ryu = 2000   #Vida inicial de Ruy
Ken = 2000   #Vida inicial de Ken
Kv  = 0    #Rounds vencidos por Ken
Rv  = 0    #Rounds vencidos por Ryu

a = int(input())   #Ler o dano do golpe inicial  

#Função para verificar se o nomero é triangular
def ntri(a):
	cont = 0
	i = 1
	while i < abs(a):        #Acumuladora com a soma de 1 até n, n<a, usada para verificar se o número é triangular
		cont = cont + i
		i = i + 1
		if cont == abs(a):   #Golpe combo, dobro do dano. Pois o numero é triangular
			a = 2*a  
			break            #Sai do laço quando encontra a soma que comprova a triangularidade do numero
	return  a			 #Retorna o novo valor de a

#Função para verificar se o numero é perfeito 
def nper(a):
	cont = 0
	i = 1
	while i < (abs(a)+1)/2:		#Procura divisores do numeros e os aculmula
		if abs(a)%i == 0: 
			cont = cont + i
		i = i + 1
	if cont == abs(a): 			#Comprova se o a soma dos divisores e igual ao numero
		a = 3*a			        #Golpe combo, triplo do dano. Pois a é perfeito
	return a 				#Retorna o novo valor de a
#Verifica se o primeiro golpe deve ser multiplicado
b = a
a = nper(b)
if a == b:
     a = ntri(b)

	
#inicia primeiro round:
while Ryu > 0 and Ken > 0:   #Verifica se ainda resta vida para os lutadores
    acm = 0 	
    if a < 0:          #Danos em Ryu
        while a < 0 and (acm*-1) < Ryu:   #Acumula golpes simultaneos
           acm = acm + a
           a = int(input())
           b = a
           a = nper(b)			#Verifica se o golpe deve ser multiplicado
           if a == b:			#Se o numero nao for perfeito, então é verificado se ele é triangular, se for perfeito prevalece o a = ax3
               a = ntri(b)

          
				   
    elif a > 0:        #Danos em Ken
        while a > 0 and acm < Ken:	  #Aculmula golpes simultaneos
           acm = acm + a
           a = int(input())
           b = a
           a = nper(b)			#Verifica se o golpe deve ser multiplicado
           if a == b:
               a = ntri(b)

           
    if acm < 0:		     #Desconta dano e imprime dados 
        R = Ryu
        Ryu = Ryu + acm
        print("Ryu:", R, "-", acm*-1, "=", Ryu)
    elif acm > 0:   	     #Desconta dano e imprime dados
        K = Ken
        Ken = Ken - acm
        print("Ken:", K, "-", acm, "=", Ken)
    

#Contabiliza rounds ganhos + reset a vida dos lutadores:
if Ken <= 0:
   Rv = Rv + 1
   Ryu = 2000
   Ken = 2000
   
if Ryu <= 0:
    Kv = Kv + 1
    Ryu = 2000
    Ken = 2000
    

#Inicia segundo round 
while Ryu > 0 and Ken > 0:   #Verifica se ainda resta vida para os lutadores
    acm = 0 	
    if a < 0:       #Danos em Ryu
        while a < 0 and (acm*-1) < Ryu:   #Acumula golpes simultaneos
           acm = acm + a
           if (-1*acm) < Ryu: 	
               a = int(input())
               b = a
               a = nper(b)		#Verifica se o golpe deve ser multiplicado
               if a == b:
                    a = ntri(b)
    elif a > 0:     #Danos em Ken
        while a > 0 and acm < Ken:  #Aculmula golpes simultaneos
           acm = acm + a
           if acm < Ken: 	
               a = int(input())
               b = a
               a = nper(b)		#Verifica se o golpe deve ser multiplicado
               if a == b:
                    a = ntri(b)

    if acm < 0:		     #Desconta dano e imprime dados
        R = Ryu
        Ryu = Ryu + acm
        print("Ryu:", R, "-", acm*-1, "=", Ryu)
    elif acm > 0:   	     #Desconta dano e imprime dados
        K = Ken
        Ken = Ken - acm
        print("Ken:", K, "-", acm, "=", Ken)
    

#Contabiliza rounds ganhos + reset na vida dos lutadores:
if Ken <= 0:
   Rv = Rv + 1
   Ryu = 2000
   Ken = 2000
   
if Ryu <= 0:
   Kv = Kv + 1
   Ryu = 2000
   Ken = 2000

#Compara rounds ganhos e imprime o vencedor:
if Kv == Rv:
      print("empatou")
if Kv > Rv:
      print("Ken venceu")
if Kv < Rv:
      print("Ryu venceu")
