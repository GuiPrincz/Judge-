'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
'''
aux = 0

for x in range (1,7):
  val = float(input())
  if val > 0:
    aux = aux + 1

print("{} valores positivos".format(aux))
