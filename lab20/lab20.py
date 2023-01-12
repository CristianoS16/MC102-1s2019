#!/usr/bin/env python3

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku


# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario

# Função para encontra posições vazias(0) da matriz:
def posiçao(mat):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                return i, j
    return False  # Retorna falso quando não encontrar mais posições, ou seja quando o Sudoku estiver resolvido

# Função para identificar a qual bloco pertence a posição que esta sendo analisada e retorna os numeros já presentes naquele bloco
def bloco(mat, i, j):
    l = []
    if i // 3 == 0 and j // 3 == 0:  # Para o Bloco 1
        for i in range(0, 3):
            for j in range(0, 3):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 0 and j // 3 == 1:  # Para o Bloco 2
        for i in range(0, 3):
            for j in range(3, 6):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 0 and j // 3 == 2:  # Para o Bloco 3
        for i in range(0, 3):
            for j in range(6, 9):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 1 and j // 3 == 0:  # Para o Bloco 4
        for i in range(3, 6):
            for j in range(0, 3):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 1 and j // 3 == 1:  # Para o Bloco 5
        for i in range(3, 6):
            for j in range(3, 6):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 1 and j // 3 == 2:  # Para o Bloco 6
        for i in range(3, 6):
            for j in range(6, 9):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 2 and j // 3 == 0:  # Para o Bloco 7
        for i in range(6, 9):
            for j in range(0, 3):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 2 and j // 3 == 1:  # Para o Bloco 8
        for i in range(6, 9):
            for j in range(3, 6):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    elif i // 3 == 2 and j // 3 == 2:  # Para o Bloco 9
        for i in range(6, 9):
            for j in range(6, 9):
                if mat[i][j] != 0:
                    l.append(mat[i][j])
    return l

#Função para guardar os valores de uma dada coluna
def coluna(resposta,j):
    l = []
    for a in range(9):
        if resposta[a][j] != 0:
            l.append(resposta[a][j])
    return l

# Função para encontrar os possiveis valores que podem preencherem uma posição vazia sem fugir das regras do Sudoku
def possiveis(resposta, i, j):
    l = [a for a in range(1, 10)]  # lista que guarda os possiveis valores que a posição[i][j] pode assumir
    b = bloco(resposta, i, j)
    c = coluna(resposta, j)
    # Elimina da lista valores que não são possiveis:
    for k in range(9):
        for x in l:
            if x in c:
                l.remove(x)
            elif x in b:
                l.remove(x)
            elif x in resposta[i]:
                l.remove(x)
    return l

# Função recursiva para solucionar o jogo:
def resolve(resposta):
    p = posiçao(resposta)
    if p == False:      #Quando não haver mais posições vazias o joog foi solucionado, então retorna True
        return True
    else:
        pos = possiveis(resposta, p[0], p[1])       #Cria a lista de possiveis valores para aquela posição
        #Troca o 0 por alguma das posibilidades e chama a função novamente, caso ela retorne True o jogo foi solucionado e essa tbm retorna True para anterior e assim por diante, caso contrário, testa os outros valores
        for a in pos:
            resposta[p[0]][p[1]] = a
            if resolve(resposta) != True:
                resposta[p[0]][p[1]] = 0
            else:
                return True
    # Implementar a funcao e trocar o valor de retorno
    print_sudoku(resposta)
    return False
