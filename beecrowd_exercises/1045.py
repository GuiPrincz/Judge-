'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO

se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO

se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO

se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO

se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO

se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
'''
valores = map(float, input().split())

a, b, c = valores

if ((a**2) == (b + c)):
  print("TRIANGULO RETANGULO")

if ((a**2) > (b**2) + (c**2)):
  print("TRIANGULO OBTUSANGULO")

if ((a**2) < (b**2) + (c**2)):
  print("TRIANGULO ACUTANGULO")

if (a==b==c):
  print("TRIANGULO EQUILATERO")

if (a==b !=c) or (b==c != a) or (a==c != b):
  print("TRIANGULO ISOSCELES")

if (a >= b +c):
    print("NAO FORMA TRIANGULO")