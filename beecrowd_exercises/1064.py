'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
'''
aux = 0
media = 0

for x in range (1,7):
  val = float(input())
  if val > 0:
    aux = aux + 1
    media = media + val

print("{} valores positivos".format(aux))
print("{:.1f}".format(media/aux))