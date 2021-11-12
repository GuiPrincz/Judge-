'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
'''
valor = float(input())

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

m1 = troco // 1
troco = troco - (m1)

m50 = troco // 0.5
troco = troco - (m50*0.5)

m25 = troco // 0.25
troco = troco - (m25*0.25)

m10 = troco // 0.10
troco = troco - (m10*0.10)

m05 = troco // 0.05
troco = troco - (m05*0.05)

m01 = troco // 0.01

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(cem))
print("{:.0f} nota(s) de R$ 50.00".format(cinquenta))
print("{:.0f} nota(s) de R$ 20.00".format(vinte))
print("{:.0f} nota(s) de R$ 10.00".format(dez))
print("{:.0f} nota(s) de R$ 5.00".format(cinco))
print("{:.0f} nota(s) de R$ 2.00".format(dois))

print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1,00".format(m1))
print("{:.0f} moeda(s) de R$ 0.50".format(m50))
print("{:.0f} moeda(s) de R$ 0.25".format(m25))
print("{:.0f} moeda(s) de R$ 0.10".format(m10))
print("{:.0f} moeda(s) de R$ 0.05".format(m05))
print("{:.0f} moeda(s) de R$ 0.01".format(m01))