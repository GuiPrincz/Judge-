'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
'''
distancia = int(input())
combustível = float(input())

consumo = distancia/combustível

print("%.3f km/l"%consumo)