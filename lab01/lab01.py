#Cristiano Samapaio Pinheiro RA: 256352
#O programa deve calcula quanto um passageiro terá que pagar para uma determinada viagem, baseado em um valor inicial fixo mais a taxa por cada unidade de distancia percorrida.
vi = int(input()) #Recebe o valor da taxa fixa
xi = int(input()) #Recebe o valor de X inicial 
yi = int(input()) #Recebe o valor de Y inicial 
xf = int(input()) #Recebe o valor de X final 
yf = int(input()) #Recebe o valor de Y final
t  = int(input()) #Recebe o valor da taxa por unidade percorrida

d= (xf-xi)+(yf-yi) #Calcula a distancia percorrida 
v= vi + d*t #Calcula o valor final

print(v) #Inprime valor final 
