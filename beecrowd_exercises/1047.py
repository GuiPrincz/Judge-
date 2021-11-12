'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
'''
hora = map(int, input().split())

h1, m1, h2, m2 = hora

if h2 > h1:
  hora = h2 - h1
  if m2 > m1:
    minuto = m2 -m1
  else:
    minuto = (60-m1)+m2
  print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))

else:
  hora = (24-h1)+h2
  if m2 > m1:
    minuto = m2 - m1
  else:
    minuto = (60-m1)+m2
  print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))