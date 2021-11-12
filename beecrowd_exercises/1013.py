'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
'''
maior = map(float,input().split())

a, b, c = maior

formula = ((a + b) + abs(a-b))/2

formula2 = ((formula + c) + abs(formula - c))/2

print("%.0f eh o maior"%formula2)