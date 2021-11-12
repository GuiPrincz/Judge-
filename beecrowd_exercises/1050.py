'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado
'''

ddd = float(input())

if ddd == 61:
  x = "Brasilia"

elif ddd == 71:
  x = "Salvador"

elif ddd == 11:
  x = "Sao Paulo"

elif ddd == 21:
  x = "Rio de Janeiro"

elif ddd == 32:
  x = "Juiz de Fora"

elif ddd == 19:
  x = "Campinas"

elif ddd == 27:
  x = "Vitoria"

elif ddd == 31:
  x = "Belo Horizonte"

else:
  x = "DDD nao cadastrado"

print(x)