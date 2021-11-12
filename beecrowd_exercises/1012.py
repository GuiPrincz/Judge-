'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''
val = map(float,input().split())

pa, pb, pc = val

triangulo = ((pa*pc)/2)

circulo = (3.14159 * pc ** 2)

trapezio = (((pa + pb)*pc)/2)

quadrado = (pb**2)

retangulo = (pa * pb)

print("TRIANGULO: %.3f"%triangulo+"\nCIRCULO: %.3f"%circulo+"\nTRAPEZIO: %.3f"%trapezio+"\nQUADRADO: %.3f"%quadrado+"\nRETANGULO: %.3f"%retangulo)