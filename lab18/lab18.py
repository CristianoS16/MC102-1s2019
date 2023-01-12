#Cristiano Sampaio Pinheiro, RA:256352
#Esse programa deve receber uma imagem em preto e branco juntamete com uma matriz, fazendo uma convolução entre a matriz que representa a imagem com a recebida será aplicado um filtro na imagem

#Função que realiaz a convolução das matrizes:
def convoluçao(m,i,j, matn, d):
    conv = (m[(i-1)][(j-1)]*matn[0][0] + m[(i-1)][j]*matn[0][1] + m[(i-1)][(j+1)]*matn[0][2] + m[i][(j-1)]*matn[1][0] + m[i][j]*matn[1][1] + m[i][(j+1)]*matn[1][2] + m[(i+1)][(j-1)]*matn[2][0] + m[(i+1)][j]*matn[2][1] + m[(i+1)][(j+1)]*matn[2][2]) /d
    #Gerencia limites dos pixels 
    if conv < 0:
        return 0
    elif conv > 255:
        return 255
    return int(conv)
#Abre os dois arquivos para leitura recebendo o titulo deles pelo terminal(usando sys)
import sys
arq1 = open(sys.argv[1], "r")
arq2 = open(sys.argv[2], "r")

matn = []		#Matriz para guardar matriz nucleo
img = []		#Matriz para guardar imagem
matf = []		#Matriz para guardar a nova imagem gerada pela convolução

#Ler o arquivo linha por linha e guarda na matriz nucleo:
while True:
	i = arq2.readline()
	if i=="":
		arq2.close()
		break 
	matn.append(i.split())
#Transforma D em inteiro e já o retira da matriz, deixando-a no formato 3x3
d =int(matn[0][0])
del matn[0]
#Transforma os elementos da matriz de str para int, possibilitando operações
for i in range(3):
	for j in range(3):
		matn[i][j] = int(matn[i][j])
#Ler o arquivo linha por linha e guarda na matriz imagem:
while True:
	j = arq1.readline()
	if j=="":
		arq1.close()
		break 
	img.append(j.split())
#Adiciona as linhas iniciais de informações a matriz que armazenará a imagem final e elimina essas informações da matiz imagem, deixando-a no formato mxn
for i in range(3):
	matf.append(img[0])
	del img[0]
#Transforma os elementos da matriz de str para int, possibilitando operações
for i in range (int(matf[1][1])):
	for j in range(int(matf[1][0])):
		img[i][j] = int(img[i][j])
#Cria uma copia da matriz imagem na matf, para possibilitar ler a matriz imagem e modificar a matf
for i in range(len(img)):
	matf.append(list(img[i]))
#Realiza a convolução
for i in range(1,int(matf[1][1])-1):
	for j in range(1,int(matf[1][0])-1):
		aux = convoluçao(img,i,j,matn,d)
		matf[i+3][j] = aux
#Transforma os elementos da matriz de int para str, para permitir usar o join
for i in range (3,int(matf[1][1])+3):
	for j in range(int(matf[1][0])):		
		matf[i][j] = str(matf[i][j])
#Adiciona quebras de linhas ao fim de cada linha da matriz, apos isso transforma toda a matriz em uma lista, onde cada linha da antiga matriz e um elemento
for i in range(len(matf)):
	if i>2:						#If para gerenciar espaços no final de cada linha do arquivo gerado
		if i != len(matf)-1:	#Para não quebrar linha na ultima linha da matriz
			matf[i].append(" \n")
		else: 
			matf[i].append(' ')
		matf[i] = " ".join(matf[i])
	else: 						#Para os primeiros paramentros onde o \n não pode ser adicionado na lista, pois gera um maldito espaço entre ele e o ultimo elemento, assim e melhor adicina-lo como parte da str do ultimo elemento
		matf[i][-1] = matf[i][-1]+("\n")
		matf[i] = " ".join(matf[i])
#Transforma essa "lista simples" em str
matf = "".join(matf)
#Imprime o resultado
print(matf)
