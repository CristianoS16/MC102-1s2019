#Cristiano Sampaio Pinheiro RA:256352
#Esse programa deve implementar algumas funções que realizam operações em conjuntos numericos, tais como:
# Pertence, Continência, Adição, Subtração, União, Interseção, Diferença e União Dinjunta
#Tais funções seram usadas em uma main presente em um arquivo separado já fornecida
#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj:         #Verifica se existe "num" nesse conjunto, retorna True se sim e False se não
        return True
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    for i in range(len(conj1)):     #Percorre o conjunto 1 verificando se seus elementos estao no conjunto 2
        if conj1[i] not in conj2:   #Caso haja algum elemento de 1 que não esta em 2, o conjunto não esta contindo, então retorna False
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if num not in conj:     #Verifica se o elemento já não pertence ao conjunto, para não haver elementos repetidos
        conj.append(num)    #Caso o elemento não pertença ao conjunto ele e adicionado

def subtracao(conj, num):
    if num in conj:         #Verifica se o elemento pertence ao vetor
        conj.remove(num)    #Caso o elemento pertença ao conjunto ele e removido

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    conjfinal = list(conj1 + conj2)     #Cria uma variavel conjfinal contenco a soma dos dois conjuntos
    for i in conj1:                     #Verifica quais elementos pertencem aos dois conjudos e portanto estão repetidos
        if i in conj2:
            conjfinal.remove(i)         #Remove elementos repetidos do conjfinal
    return conjfinal

def intersecao(conj1, conj2):
    int = []                            #Cria uma lista vazia que será preenchida com os elementos pertencentes aos dois conjuntos
    for i in conj1:
        if i in conj2: #Verifica se o elemeto de um conjunto esta presente no outro
            int.append(i)                       #Quando o elemento esta presente nos 2 conjuntos ele e adicionado a lista int(interceção)
    return int

def diferenca(conj1, conj2):
    l = list(conj1)     #Cria uma copia do primeiro conjunto
    for i in conj1:
        if i in conj2:  #Quando um elemento do primeiro conjunto pertence também ao segundo ele é removido
            l.remove(i)
    return l

def uniao_disjunta(conj1, conj2):
    AB = diferenca(conj1,conj2)     #Guarda os elementos de 1 que não estão em 2
    BA = diferenca(conj2,conj1)     #Guarda os elementos de 2 que não estão em 1
    unid = uniao(AB,BA)             #Faz a união dos elemento anteriores
    return unid
