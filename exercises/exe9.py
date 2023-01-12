#Programa para calcular o mdc de dois numeros inteiros positivos
m = int(input())
n = int(input())
ant = 1

if m >= n:

  if n == 0:
    print("mdc = ", m)
  a = m%n
  while a != 0:
    ant = a
    a = n%a
  print(ant)
else:
  if m == 0:
   print("mdc = ", n)
  a = n % m
  while a != 0:
   ant = a
   a = n % a
  print(ant)

