#Cristiano Samapaio Pinheiro RA: 256352
#O programa deve calcular em quanto tempo deve ser acionada um micro explosivo que ira desviar a bomba para a base do imperio

h=  float(input()) #Recebe a altura da nave
vb= float(input()) #Recebe a velocidade de queda da bomba
d=  float(input()) #Recebe a distancia da base rebelte ate a base do imperio
T=  float(input()) #É a força de empuxo do micro explosivo, pode se considerado a velocidade horizontal da bomba


t=  h/vb #calcula o tempo de queda da bomba
t1= d/T  #calcula o tempo necessario para a bomba alcançar a base rebelde com uma velocida T horizontal

m= t-t1 #A diferença entre os tempos da o exato momento em que a bomba precisa ser acionada para ser desviada para a base do imperio 

print("%.3f" %m) #Imprime o tempo, em segundos, em que deverá ser acionado o micro explosivo 

#Que a força esteja conosco!
