'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
'''
n = int(input())
inn = 0
out = 0

for a in range(1, n+1):
  x = int(input())
  if 10 <= x <= 20:
    inn = inn + 1
  else:
    out = out +1

print("{} in".format(inn))
print("{} out".format(out))
  