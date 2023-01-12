#Cristiano Sampaio Pinheiro RA:256352
#Esse programa deve analisar a hierarquia de uma empresa, dado uma matriz onde os indices representam os funcionarios
import random
#Analisa os funcionarios subordinados e os subordinados dos subordinados . .  .
def hierarquia(n,k, mat,l):
    l.append(k)
    if not 1 in mat[k]:
        return k
    for i in range(n):
        if mat[k][i] == 1:
            hierarquia(n,i,mat,l)
#Função para particionar lista para o Quick-Sort
def parte(l,i,f):
    p = l[f]
    while i < f:
        while i < f and l[i] <= p:
            i = i + 1
        while i < f and l[f] > p:
            f = f - 1
        l[i], l[f] = l[f], l[i]
    return i
#Função para ordenar a lista usando o Quick-Sort
def ordena(l,i,f):
    if i < f:
        a = random.randint(i,f)     #Escolhe pivo randomicamente
        l[a], l[f] = l[f], l[a]
        p = parte(l,i,f)
        ordena(l,i,p-1)
        ordena(l,p,f)

mat = []
p = input()     #Recebe o numero de funcionarios e qual vai ser analisado
p = p.split()
p[0] = int(p[0])
p[1] = int(p[1])
l = []
#Ler a matriz dos funcionarios
for i in range(p[0]):
    mat.append(input())
    mat[i] = mat[i].split()
#Transforma posições em inteiros
for i in range(p[0]):
    for j in range(p[0]):
        mat[i][j] = int(mat[i][j])
#Acha a hierarquia e ordena os elementos a partir do segundo elemento
hierarquia(p[0],p[1],mat,l)
ordena(l,1,len(l)-1)
#Imprimeo resultado resolvendo problemas de espaço:
for i in range(len(l)):
    if l[i] == l[-1]:
        print(l[i])
    else:
        print(l[i], end=' ')
