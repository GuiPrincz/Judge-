'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
'''
num = map(float,input().split())

cod, qnt = num

if cod == 1:
  cod = qnt * 4
  print("Total: R$ {:.2f}".format(cod))

elif cod == 2:
  cod = qnt * 4.5
  print("Total: R$ {:.2f}".format(cod))

elif cod == 3:
  cod = qnt * 5
  print("Total: R$ {:.2f}".format(cod))

elif cod == 4:
  cod = qnt * 2
  print("Total: R$ {:.2f}".format(cod))

else:
  cod = qnt * 1.5
  print("Total: R$ {:.2f}".format(cod))