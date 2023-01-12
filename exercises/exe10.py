#Transforma um numero decimal em binario inteiro tipo int
n = int(input("Digite um numero:"))
acm = 1
s = 0
while n != 0 :
  digito = n%2
  s = acm*digito + s
  n = n//2
  acm= acm*10
print(s)
print (type(s))
