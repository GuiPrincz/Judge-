'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
'''
valor = int(input())

troco = valor

cem = troco//100
troco = troco - (cem * 100)
cinquenta = troco // 50
troco = troco - (cinquenta * 50)
vinte = troco // 20
troco = troco - (vinte * 20)
dez = troco // 10
troco = troco -(dez * 10)
cinco = troco // 5
troco = troco - (cinco * 5)
dois = troco // 2
troco = troco - (dois * 2)
um = troco // 1

print(valor)
print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinquenta))
print("{} nota(s) de R$ 20,00".format(vinte))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinco))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))