'''
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
'''
n = int(input())
x = [""]

for a in range(1, n+1):
  x.append(int(input()))

for a in range(1, n+1):  
  if x[a] > 0:
    if x[a] % 2 == 0:
      print("EVEN POSITIVE")
    else:
      print("ODD POSITIVE")

  if x[a] < 0:
    if x[a] % 2 == 0:
      print("EVEN NEGATIVE")
    else:
      print("ODD NEGATIVE")

  if x[a]  == 0:
    print("NULL")