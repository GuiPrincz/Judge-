'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
'''
i = 1
num = int(input())

while i <= num:
  if i % 2 != 0:
    print(i)
  i= i+1
  