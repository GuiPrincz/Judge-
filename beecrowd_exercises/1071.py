'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
'''
x = int(input())
y = int(input())

if x > y:
  maior = x 

else:
  maior = y

if y < x:
  menor = y

else:
  menor = x

menor = menor + 1
soma = 0

while (menor < maior):
  if(menor % 2 != 0):
      soma= soma + menor
  menor= menor + 1
print(soma)

