'''
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
1 x N = N 2 x N = 2N ... 10 x N = 10N
'''
num = int(input())
aux = 1

while aux <= 10:
  print(aux," x ",num," = ",num*aux)
  aux = aux + 1