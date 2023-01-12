#Cristiano Sampaio Pinheiro RA:256352
#Esse programa deve a partir de uma matriz dada verificar qual o resultado da interação entre humanos e zumbis no decorrer de cada dia.

#Função para acrescentar 2 colunas e 2 linhas(primeira e ultima) nulas na matriz(usando dica do enunciado)
def zeros(m,l,c):
    for a in range(l):
        m[a].insert(0,0)                    #Acrescenta 0 a posição inicial de cada sublista(linha)
        m[a].append(0)                      #Acrescenta 0 a posição final de cada sublista(linha)
    m.insert(0,[0 for b in range(c+2)])     #Acrescenta uma linha nula a posição inicial da matriz
    m.append([0 for d in range(c+2)])       #Acrescenta uma linha nula a posição final da matriz

#Função que verifica o caso quando a posição analisada esta vazia(0)
def vazio(m,i,j):
    a = 0
    vizinhos = [m[(i-1)][(j-1)], m[(i-1)][j], m[(i-1)][(j+1)], m[i][(j-1)], m[i][(j+1)], m[(i+1)][(j-1)], m[(i+1)][j], m[(i+1)][(j+1)]]
    for b in range(len(vizinhos)):
        if vizinhos[b] == 1:                #Contabiliza os humanos vizinhos dessa posição para verificar se haverar um novo humano no dia seguinte
            a = a + 1
    if a == 2:                              #Se essa posição possui exatamente 2 vizinhos humanos no dia seguinte havera um humano nela
        return 1
    return 0

#função para verificar o caso quando a posição analisada e oculpada por um humano(1)
def humano(m,i,j):
    a = 0
    vizinhos = [m[(i - 1)][(j - 1)], m[(i - 1)][j], m[(i - 1)][(j + 1)], m[i][(j - 1)], m[i][(j + 1)], m[(i + 1)][(j - 1)], m[(i + 1)][j], m[(i + 1)][(j + 1)]]
    if 2 in vizinhos:                       #Se esse humano possui 1 ou mais vizinho zumbi ele se torna zumbi no dia seguinte
        return 2
    return 1

#função para verificar o caso quando a posição analisada e oculpada por um zumbi(2)
def zumbi(m,i,j):
    a = 0
    vizinhos = [m[(i-1)][(j-1)], m[(i-1)][j], m[(i-1)][(j+1)], m[i][(j-1)], m[i][(j+1)], m[(i+1)][(j-1)], m[(i+1)][j], m[(i+1)][(j+1)]]
    for b in range(len(vizinhos)):
        if vizinhos[b] == 1:                #Contabiliza quantos humanos são vizinhos desse zumbi
            a += 1
            if a >= 2:                      #Se esse zumbi possui mais de 2 humanos vizinhos ele se e morto, posição fica vazia(0) no sia seguinte
                return 0
    if not 1 in vizinhos:                   #Se esse zumbi não possui nenhum vizinho humano ele morre de fome, posiçõa fica vazia(0) no dia seguinte
        return 0
    return 2

ordem = input()             #Recebe o numero de linhas e colunas da matriz
dias = int(input())         #Recebe o numero de dias que sera realizada a simulação
m = []                      #Matriz para receber os dados
n = []                      #Matriz auxiliar
ordem = ordem.split()
l = int(ordem[0])                #Numero de linhas da matriz
c = int(ordem[1])                #Numero de colunas da matriz

for a in range (l):
    m.append(input().split())       #Recebe as linhas da matriz e já organiza a matriz
    for b in range(c):
        m[a][b] = int(m[a][b])      #transforma as strings lidas em inteiros para possibilitar a manipulação numerica

zeros(m,l,c)                        #Acrescenta linhas e colunas nulas a matriz

#Faz uma copia de m(matriz principal) em n(matriz auxiliar)
for k in range (l+2):
    n.append(list(m[k]))

#percorre os elementos da matriz em cada dia, faz a analise em m(matriz principal) e modifica n(matriz auxiliar)
for d in range(1 ,dias+2):
    print("iteracao", d-1)                #Imprime qual interação foi feita
    for h in range(1,l+1):                #Imprime a matriz apos essa interação
        for y in range(1,c+1):
            print(m[h][y], end="")
        print()
    for i in range(1,l+1):                #Percorre as linhas
        for j in range(1,c+1):            #Percorre os elementos de cada linha
            if m[i][j] == 0:              #Quando analisamos um vazio
                n[i][j] = vazio(m, i, j)
            elif m[i][j] == 1:            #Quando analisamos um humano
                n[i][j] = humano(m, i, j)
            elif m[i][j] == 2:            #Quando analizamos um zumbi
                n[i][j] = zumbi(m, i, j)
    #Atualiza a matriz principal(m) para a proxima interação
    for i in range(l+2):
        m[i] = list(n[i])
