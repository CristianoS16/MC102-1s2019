t = float(input("Valor da transação = "))

if   t < 2500.00:
	a = t*0.017 + 30
	if a < 39:
		print("R$39.00")
	else:
		print("RS", a)
	
elif 2500.01 < t < 6250.00:
	print("R$", t*0.0066 + 56)
elif 6250.01 < t < 20000.00:
	print("R$", t*0.0034 + 76)
elif 20000.01 < t < 50000.00:
	print("R$", t*0.0022 + 100)
elif 50000.01 < t < 500000.00:
	print("R$", t*0.0011 + 155)
elif 500000.01 < t:
	print("R$", t*0.0009 + 255)


