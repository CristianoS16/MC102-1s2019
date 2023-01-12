# Cristiano Sampaio Pinheiro RA:256352
# Esse programa deve verifica qual a melhor escolha de compra para as açoes de 4 empresas ao longo de "a" dias, no entando existem restrições, não pode haver mais de uma empresa na carteira de açoes, nao e possivel comprar a mesma ação mais de uma vez, não é possivel fazer operações vendidas(vender antes de comprar)

#Função para receber os valores das açoes de cada empresa em cada dia e montar uma lista com esses dados:
def dados(a):
    x = []
    for i in range(3):
        for j in range(a):
            g = float(input())
            x.append(g)
        return x

#Função para calcular o lucro obtido com uma determinada operação:
def lucroE(a,b):
    c = b-a
    return c

a = int(input())	#Numero de dias analisados
lucrot = 0			#Lucro total obtido

E1 = dados(a)  		#Lista para armazenar dados da empresa 1
E2 = dados(a)  		#Lista para armazenar dados da empresa 2
E3 = dados(a)  		#Lista para armazenar dados da empresa 3
E4 = dados(a)  		#Lista para armazenar dados da empresa 4

#Bloco de for(s) para criar todas as combinações possiveis de comprar e venda das açoes dessas 4 empresas
for c1 in range(a):
    for v1 in range(a):
        for c2 in range(a):
            for v2 in range(a):
                for c3 in range(a):
                    for v3 in range(a):
                        for c4 in range(a):
                            for v4 in range(a):
                                if v1 >= c1 and v2 >= c2 and v3 >= c3 and v4 >= c4:             #Gatante a venda somente apos a compra ou no mesmo dia, resultanto em lucro 0
                                    if not c1<=c2<v1 and not c1<=c3<v1 and not c1<=c4<v1 and not c2<=c1<v2 and not c2<=c3<v2 and not c2<=c4<v2 and not c3<=c1<v3 and not c3<=c2<v3 and not c3<=c4<v3 and not c4<=c1<v4 and not c4<=c2<v4 and not c4<=c3<v4:		#Não permite compra uma empresa enquanto esta com outra na carteira de açoes 
                                        l = E1[v1] - E1[c1] + E2[v2] - E2[c2] + E3[v3] - E3[c3] + E4[v4] - E4[c4]			#Calcula o lucro com a combinação de compra e venda das 4 empresas
                                        if l > lucrot:				#Compara os lucros visando guardar o maior obtido
                                           lucrot = l
                                           d = []
                                           d.append(c1);d.append(v1);d.append(c2);d.append(v2);d.append(c3); d.append(v3);d.append(c4);d.append(v4)		#Lista para armazenar a combinação de comprar e venda das 4 empresas que resulta no maior lucro ate o momento
if lucrot == 0:					#Verifica se houve algum lucro
    print("Lucro: %.2f" % (lucrot))
else:							#Havendo lucro imprime qual o dia de comprar, dia de venda e lucro obtido com uma determinada empresa
    if d[0]!=d[1]:
        lE1 = lucroE(E1[d[0]], E1[d[1]])
        print("acao %d: compra %d, venda %d, lucro %.2f" % (1, d[0]+1, d[1]+1, lE1))
    if d[2]!=d[3]:
        lE2 = lucroE(E2[d[2]], E2[d[3]])
        print("acao %d: compra %d, venda %d, lucro %.2f" % (2, d[2]+1, d[3]+1, lE2))
    if d[4]!=d[5]:
        lE3 = lucroE(E3[d[4]], E3[d[5]])
        print("acao %d: compra %d, venda %d, lucro %.2f" % (3, d[4]+1, d[5]+1, lE3))
    if d[6]!=d[7]:
        lE4 = lucroE(E4[d[6]], E4[d[7]])
        print("acao %d: compra %d, venda %d, lucro %.2f" % (4, d[6]+1, d[7]+1, lE4))
    print("Lucro: %.2f" % (lucrot))
