'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.
'''
par = 0
impar = 0
pos = 0
neg = 0


for x in range (1,6):
  val = float(input())

  if val % 2 == 0:
    par = par + 1  

  if val % 2 == 1:
    impar = impar + 1

  if val > 0:
    pos = pos + 1  

  if val < 0:
    neg = neg + 1

print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))