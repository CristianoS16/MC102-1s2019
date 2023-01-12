#Cristiano Sampaio Pinheiro RA:256352
#Esse programa deve simular o sistema de gerenciamento de RAs da DAC. Ele deve ser capaz de:
#Imprimir os RAs dos alunos (ao receber 'p'),
#Ordenar os RAs de maneira crescente (ao receber 'c')
#Ordenar os RAs de maneira decrescente (ao receber 'd')
#Realizar uma busca binaria (ao receber 'b')
#Inserir um novo RA a lista (ao receber 'i')
#Remover um RA da lista (ao receber 'r')
#Encerar o programa (ao receber 's')

#Função para imprimir lista:
def p(l):
    for i in l:
        print(i , end=' ')
    if len(l) != 0:
        print()
#Função para ordenar de maneira crescente usando Selection-Sort:
def Ordemc(l):
    for i in range (len(l)-1):
        for i in range (len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
#Função para ordenar de maneira decrescente usando Selection-Sort:
def Ordemd(l):
    for i in range (len(l)-1):
        for i in range (len(l)-1):
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
#Função para realizar a Busca Binaria na lista:
def Buscab(l,p,o):
    indice = []
    i = 0
    f = len(l)-1
    while f >= i:
        m = (i+f)//2
        if p == l[m]:
            indice.append(m)
            return indice
        elif p > l[m] and o == 1:
            i = m+1
            indice.append(m)
        elif p < l[m] and o == 1:
            f = m-1
            indice.append(m)
        elif p < l[m] and o == 2:
            i = m+1
            indice.append(m)
        elif p > l[m] and o == 2:
            f = m-1
            indice.append(m)
    indice.append(-1)
    return indice

l = input()             #Recebe a lista de RAs como string
l = l.split()           #Transforma a string em uma lista
for i in range (len(l)):#Transforma os elementos da lista em inteiros
    l[i] = int(l[i])
ação = 0
ordenada = 0            #Guarda se a lista ja foi ordenada

while ação != 's':          #Ate que o usuario deseje sair(digitando s) essa laço executa as açoes solicitadas
    ação = input()          #Recebe a ação a ser feita na lista de RAs
    if ação == 's':
        break
    if ação == 'p':         #Imprime a lista
        p(l)
    elif ação == 'c':       #Ordena a listas de maneira crescente
        Ordemc(l)
        ordenada = 1        #Registra que a lista foi ordenada de maneira crescente
    elif ação == 'd':       #Ordena a lista de maneira decrescente
        Ordemd(l)
        ordenada = 2        #Registra que a lista foi ordenada de maneira crescente
    else:                   #Para as ações que são seguidas de parametros
        ação = ação.split()
        ação[1] = int(ação[1])
        if ação[0] == 'b':          #Para realizar busca binaria na lista
            if ordenada == 0:       #Para quando a lista não foi ordenada ainda
                print("Vetor nao ordenado!")
            else:                   #Para procurar o RA na lista, apos verificar que a lista esta ordenada.
                ind = Buscab(l,ação[1],ordenada)
                if ind[-1] == -1:
                    del ind[-1]
                    p(ind)
                    print("%d nao esta na lista!" % ação[1])
                else:
                    p(ind)
                    print("%d esta na posicao: %d" % (ação[1], ind[-1]))
        elif ação[0] == 'i':        #Para inserir um novo RA na lista
            if len(l) >= 150:       #Para quando a turma ja esta cheia
                print("Limite de vagas excedido!")
            elif ação[1] in l:      #Para quando o aluno ja esta matriculado
                print("Aluno ja matriculado na turma!")
            elif ordenada == 1:     #Para adicionar um novo aluno e permanecer com a lista ordenada de maneira crescente
                l.append(int(ação[1]))
                Ordemc(l)
            elif ordenada == 2:     #Para adicionar um novo aluno e permanecer com a lista ordenada de maneira decrescente
                l.append(int(ação[1]))
                Ordemd(l)
            else:                   #Para adicionar o novo aluno no final da lista
                l.append(int(ação[1]))
        elif ação[0] == 'r':        #Para remover um RA da lista
            if len(l) == 0:         #Para quando a turma esta vazia
                print("Nao ha alunos cadastrados na turma!")
            elif ação[1] not in l:    #Para quando tenta remover um aluno que nao esta presente na lista
                print("Aluno nao matriculado na turma!")
            else:                   #De fato remove o aluno quando ele esta presente na turma
                l.remove(ação[1])
