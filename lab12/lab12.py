# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve localizar palavras chaves dentro de um texto e a partir delas chegar a uma direção e a uma elevação do canhao para realizar um ataque a base inimiga

#Função para extrair a direção a partir da palavras chaves:
def dir(a):
	if "mercurio" in a:
		return "N"
	elif "venus" in a:
		return "NE"
	elif "terra" in a:
		return "L"
	elif "marte" in a:
		return "SE"
	elif "jupiter" in a:
		return "S"
	elif "saturno" in a:
		return "SO"
	elif "urano" in a:
		return "O"
	elif "netuno" in a:
		return 'NO'
	return 0

#Função para extrair a elevação do canhão a partir das palavras chaves:
def elev(a):
	if "verde" in a:
		return 30
	elif "amarelo" in a:
		return 45
	elif "vermelho" in a:
		return 60
	return 0

st = input()			#Recebe a mensagem codificada
st = st.lower()			#Transforma todos os caracteres em letras maiusculas
st = st.split()			#Transforma str em uma lista 
i = 0

for i in range (len(st)):	#Percorre a lista procurando alguma direção para o lançamento 
	if dir(st[i]) != 0:
		d = dir(st[i])
	#for j in range(i,len(st)):
		while i < len(st):			#Apos achar a direção percorre a partir daquele ponto procurando a elevação do canhão
			if elev(st[i]) != 0:
				e = elev(st[i])
				print (d,"-",e)
				break				#Achada a elevação volta a procurar por uma nova direção
			i += 1
#Que a força estaja comigo porque nao esta facil

	
	
