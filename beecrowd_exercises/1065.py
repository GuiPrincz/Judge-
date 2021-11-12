'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
'''
aux = 0

for x in range (1,6):
  val = float(input())
  if val % 2 == 0:
    aux = aux + 1

print("{} valores pares".format(aux))