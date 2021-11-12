'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''
hora = map(int, input().split())

h1, h2 = hora

if h2 > h1:
  hora = h2 - h1
  print ("O JOGO DUROU {} HORA(S)".format(hora))

else:
  hora = (24-h1)+h2
  print("O JOGO DUROU {} HORA(S)".format(hora))