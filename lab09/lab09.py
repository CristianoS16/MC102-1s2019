# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve gerar uma matriz quadrada, nas posiçõeo onde i é divisor de j ou j é divisor de i sera impresso "*", nas demais posições sera impreso "_"

n = int(input())	#Recebe a ordem da matriz
cont = 0		#Inicia uma contadora para contabilizar quantos "*" seram impressos

for i in range(1, n+1):				#Usado para as linhas da matriz 	
    for j in range(1, n+1):			#Usado para as colunas da matriz 
        d = 1
        if d < n+1:				#Condição para continuar em uma mesma linha 
            if i % j == 0 or j % i == 0:	#Condição para imprimir "*"	
                print("*", end='')
                d = d + 1
                cont = cont + 1
            else:				#Condição para imprimir "-"
                print("-", end='')
                d = d +1
    print("")					#Quebra linha, para iniciar a proxima
print (cont)					#Imprime o total de "*" presentes na matriz
