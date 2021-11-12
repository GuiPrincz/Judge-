'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
'''
duração = int(input())

horas = (duração // 3600)
duração = duração - horas * 3600
minutos = (duração//60)
segundos = duração-minutos*60

print("{}:{}:{}".format(horas,minutos,segundos))
