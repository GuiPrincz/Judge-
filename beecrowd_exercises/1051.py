'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.



Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.
'''
sal = float(input())

if sal <= 2000:
  i = 0
  print("ISENTO")

if 2000 < sal <=3000:
  r8 = sal - 2000
  i = r8 / (8/100)

if 3000 < sal <= 4500:
  i8 = (8 / 100) * (1000.00)
  r18 = sal - 3000.00
  i = r18 * (18 / 100) + i8

if sal > 4500:
  i8 = (8 / 100) * (1000.00)
  i18 = (18 / 100) * (1500.00)
  r28 = sal - 4500.00
  i = i18 + i8 + r28 * (28 / 100)

if sal > 2000:
  print("R$ {:.2f}".format(i))