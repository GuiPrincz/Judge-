'''
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
'''
n = int(input())
aux = 0

for x in range(2, n + 1, 2):
  print("{}^2 = {}".format(x,x**2))
    