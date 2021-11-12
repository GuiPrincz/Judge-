'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
'''
x,y,z=list(map(int,input().split()))

lista = [x,y,z]

lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print("")
print(x)
print(y)
print(z)