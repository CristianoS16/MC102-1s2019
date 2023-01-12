#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.

def atualizaTabela(tabela, jogo):
    j = jogo.split()
    #Altera os parametros que depente da vitoria de um determinado jogador:
    if j[1] > j[3]:     #Para quando o primeiro jogador ganhar a partida
        for i in range(len(tabela)):
            if tabela[i][0] == j[0]:    #Localiza a a lista que armazana os dados do ganhador e contabiliza a vitoria além de somar os 3 pontos
                tabela[i][1] += 3
                tabela[i][2] += 1
                break
    elif j[1] < j[3]:  #Para quando o segundo jogador ganhar a partida
        for i in range(len(tabela)):
            if tabela[i][0] == j[4]:    #Localiza a a lista que armazana os dados do ganhador e contabiliza a vitoria além de somar os 3 pontos
                tabela[i][1] += 3
                tabela[i][2] += 1
                break
    elif j[1] == j[3]:  #Para quando a partida empatar
        for i in range(len(tabela)):
            if tabela[i][0] == j[0] or tabela[i][0] == j[4]:    #Localiza a lista dos dados dos dois jogadores e adicionar 1 ponto
                tabela[i][1] += 1
    #Altera os parametros que nao dependem de quem ganhou a partida:
    for k in range(len(tabela)):            #Contabiliza o saldo de gols e os gols pros para cada jogador
        if tabela[k][0] == j[0]:
            tabela[k][3] += (int(j[1])-int(j[3]))
            tabela[k][4] += int(j[1])
        if tabela[k][0] == j[4]:
            tabela[k][3] += (int(j[3])-int(j[1]))
            tabela[k][4] += int(j[3])
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    for a in range(1,5):           #Percorre a lista de dados de cada time comparando os dados de mesma posição procurando o maior
        if time1[a] > time2[a]:
            return 1
        if time2[a] > time1[a]:
            return -1
    return 0
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    for b in range(len(tabela)-1):      #Percorre a lista sempre levando as sublista que tem os maiores parametros iniciais para o inicio
        for c in range(len(tabela)-1):
            if comparaTimes(tabela[c],tabela[c+1]) == -1:
                tabela[c], tabela[c+1] = tabela[c+1], tabela[c]
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for d in range(len(tabela)):    #Para imprimir os dados de cada time individualmente
        l = str(tabela[d]).strip('[]')  #Transforma lista em string ja removendo os '[]'
        l = l.replace('\'', '')         #Remove as aspas da string inicial
        print (l)
#*******************************************************************************
