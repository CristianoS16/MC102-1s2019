#computar todas as somas de 4 algarismos que ressultam em um determinado s
s = int(input("Digite o resultado: "))
for x1 range(0,s+1):
  for x2 range (0, s -x1)
    for x3 range(0, s - x1 -x2)
      X4 = s - x1 -x2 -x3
      print(x1, "+", x2, "+", x3, "+", x4, "=", s)