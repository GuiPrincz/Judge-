'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	         Percentual de Reajuste
0 - 400.00               15%
400.01 - 800.00          12%
800.01 - 1200.00         10%
1200.01 - 2000.00         7%
Acima de 2000.00          4%


Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
'''
salario = float(input())

x = salario
aux = float

if salario <= 400.00:
  s = salario * 1.15
  aux = x * 0.15
  p = 15

if 400.01 <= salario <= 800.00:
  s = salario * 1.12
  aux = x * 0.12
  p = 12

if 800.01 <= salario <= 1200.00:
  s = salario * 1.10
  aux = x * 0.10
  p = 10

if 1200.01 <= salario <= 2000.00:
  s = salario * 1.07
  aux = x * 0.07
  p = 7

if salario > 2000.01:
  s = salario * 1.04
  aux = x * 0.04
  p = 4


print("Novo salario: {:.2f}".format(s))
print("Reajuste ganho: {:.2f}".format(aux))
print("Em percentual: {} %".format(p))