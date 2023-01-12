#jogos da mega-sena em que os numeros variam entre par é inpar
for d1 in range(2, 61):
 for d2 in range(d1+1, 61):
  for d3 in range(d2+2, 61):
   for d4 in range(d3+1, 61):
    for d5 in range(d4+1, 61):
     for d6 in range(d5+1, 61):
      if d1%2==0 and d2%2!=0 and d3%2==0 and d4%2!=0 and  d5%2==0 and d6%2!=0:
        print(d1,d2,d3,d4,d5,d6)