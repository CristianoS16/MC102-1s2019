#!/usr/bin/env python3

import math

# Laboratorio 17 - Banco de Dados Geografico
# Nome: Cristiano Sampaio Pinheiro
# RA: 256352

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados) 
#       cep: CEP desejado 
# 
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.   
#
def consulta_cidade_por_cep(cidades, cep):
    for i in range(len(cidades)):
        if cidades[i].inicioCEP < cep < cidades[i].fimCEP: #Verifica se o CEP procurado se encaixa no intervalo de alguma das cidades
            return i					#Retorna o indice da cidade caso o CEP procurado pertença a seu intervalo de CEPs
    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    ind = []		#Lista para guardar os indices
    cid = []		#Lista para guardar as cidades que estão dentro de determinado raio
    for i in range(len(cidades)):
        if distancia(cidades[cidadeReferencia].coordenadas, cidades[i].coordenadas) < raio: #Aquelas cidades que estão no raio são inseridas nas listas
            ind.append(i)
            cid.append(cidades[i])
#Ordena a lista de cidades e de indices de acordo com o raio usando bubble-sort
    for h in range(len(cid)-1):
        for j in range(len(cid)-1):
            if distancia(cidades[cidadeReferencia].coordenadas, cid[j].coordenadas) > distancia(cidades[cidadeReferencia].coordenadas, cid[j+1].coordenadas):
                ind[j], ind[j+1] = ind[j+1], ind[j]
                cid[j], cid[j+1] = cid[j+1], cid[j]
    return ind			#Retorna o indice das cidades que estão contidas naquele raio

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#          
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    city = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)	#Usa a função anterior para conseguir quais cidades estão contidas em um determinad raio
    acm = 0
    for i in city:	#Acumula o numero de habitantes das cidades retornadas pela função cidades por raio
        acm += cidades[i].numHabitantes
    return acm		#Retorna o resultado final da soma de habitantes

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    city = []			#Lista para guardar cidades pertencentes a um determinado raio
    ind = consulta_cidades_por_raio(cidades,cidadeReferencia,raio)
#Preenche a lista
    for i in ind:
        city.append(cidades[i])
#Ordena a lista de acordo com o numero de habitantes usando bubble-sort
    for i in range (len(city)-1):
        for j in range(len(city)-1):
            if city[j].numHabitantes > city[j+1].numHabitantes:
                city[j], city[j+1] = city[j+1], city[j]
    if len(city)%2 == 0:		#Calcula mediana para uma lista que contem um numero par de elementos
        a = (len(city)//2)-1
        b = a+1
        return (city[a].numHabitantes+city[b].numHabitantes)/2
    return city[((len(city)//2))].numHabitantes		#Mediana para lista com numero impar de elementos

