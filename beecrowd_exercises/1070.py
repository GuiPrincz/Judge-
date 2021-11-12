'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
'''
num = int(input())

impares = (x for x in range(num,num+12)if x %2 !=0)
for x in impares:
    print(x)
