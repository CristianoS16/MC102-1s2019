# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve receber dados da evolução de determinadas especies de pokemon, deles deve extrair
# o multiplicador de poder quando um pokemon de determinada especie evolui. Com esse multiplicador deve
# prever qual sera o poder de um novo pokemon dado após sua evolução

n = int(input())    #Recebe o n numero de especies comparadas
i = []              #Lista para guardar identificador da especie
PCa = []            #Lista para guardar Poder de Combate Atual
PCf = []            #Lista para guardar Poder de combate futuro
mult = []           #Lista para guardar multiplicador de cada especie
div = []            #lista para guardar fator de divisão da media para obter o multiplicador
w = 1               #Recebe Pcas para calculo de PCf

#Função para verificar se a especie ja foi analizada antes
def iigual(i, a):
    for j in range(len(i)):
        if i[j] == a[0]:
            return j #Retorna a posição das lista onde os dados daquela especie estão armazenados
    return -1

#Função para entregar o multiplicador de cada especie
def mul(y,p):
    g = y/p
    return g

#Função para fazer o arredondamento para cima para entrega do valor final
def mint(k):
    o = int(k)
    d = k - o
    if d > 1/2:
        return round(k)
    elif d < 1/2:
        return round(k)+1

#Analisa as evoluções dadas e calcula o multiplicador para casa especie:
for a in range(n):  #Repete a ação para as n evoluções dadas para analise
    l = (input())  #Recebe a linha contendo o indentificador, PCa, PCf
    b = a
    a = [int(p) for p in l.split()]
    f = iigual(i, a)
    if b != 0:
        if f != -1:     #Caso a especie ja tenha sido analisada antes os dados são agrupados na mesma posição em todas as listas
            div[f] += 1 #Lissta que armazena o valor para realizar media entre os multiplicadores
            g = mul(a[2], a[1])
            mult[f] += g    #Soma o multiplicador desse caso aos demais para se calcular a media posteriormente

        else:           #Para quando a especie não foi analisada anteriormente, somente adicionas os dados
            i.append(a[0])
            PCa.append(a[1])
            PCf.append(a[2])
            div.append(1)
            g = mul(PCf[f], PCa[f])
            mult.append(g)
    else:                   #Somente para a primeira linha de analisa, quando as listas ainda estam vazias
        i.append(a[0])
        PCa.append(a[1])
        PCf.append(a[2])
        div.append(1)
        g = mul(PCf[b], PCa[b])
        mult.append(g)

#Calculo a media dos multiplicadores obtidos
for r in range(len(mult)):
    s = mul(mult[r], div[r])
    mult[r] = s

#Calcula o poder futuro para novos pokemons das especies ja analisadas:
while w != 0:
    f = input()         #Recebe a linha contendo identificador e PCa do novo pokemon
    k = [int(i) for i in f.split()]
    w = k[0] + k[1]
    for ab in range (len(i)):   #Busca o identificador na lista criada anteriormente
        if k[0] == i[ab]:
            gh = k[1]*mult[ab]  #Calcula poder futuro para essa especie
            gh = mint(gh)       #Realiza o arredondamento sempre para cima
            print(gh)

