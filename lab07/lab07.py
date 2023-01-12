# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve contabilizar os danos recebido por dois jogadores em uma luta do Street Fighter e no final apresentar o ganhador.

Ryu = 50   #Vida inicial de Ruy
Ken = 50   #Vida inicial de Ken
Kv  = 0    #Rounds vencidos por Ken
Rv  = 0    #Rounds vencidos por Ryu
a = int(input())   #Ler o dano do golpe inicial  

#inicia primeiro round:
while Ryu > 0 and Ken > 0:   #Verifica se ainda resta vida para os lutadores
    acm = 0 	
    if a < 0:          #Danos em Ryu
        while a < 0 and (acm*-1) < Ryu:   #Acumula golpes simultaneos
           acm = acm + a
           a = int(input())
    elif a > 0:        #Danos em Ken
        while a > 0 and acm < Ken:	  #Aculmula golpes simultaneos
           acm = acm + a
           a = int(input())
           
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
   Ryu = 50
   Ken = 50
   
if Ryu <= 0:
    Kv = Kv + 1
    Ryu = 50
    Ken = 50
    

#Inicia segundo round 
while Ryu > 0 and Ken > 0:   #Verifica se ainda resta vida para os lutadores
    acm = 0 	
    if a < 0:       #Danos em Ryu
        while a < 0 and (acm*-1) < Ryu:   #Acumula golpes simultaneos
           acm = acm + a
           if (-1*acm) < Ryu: 	
               a = int(input())
    elif a > 0:     #Danos em Ken
        while a > 0 and acm < Ken:  #Aculmula golpes simultaneos
           acm = acm + a
           if acm < Ken: 	
               a = int(input())

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
   Ryu = 50
   Ken = 50
   
if Ryu <= 0:
   Kv = Kv + 1
   Ryu = 50
   Ken = 50

#Compara rounds ganhos e imprime o vencedor:
if Kv == Rv:
      print("empatou")
if Kv > Rv:
      print("Ken venceu")
if Kv < Rv:
      print("Ryu venceu")
