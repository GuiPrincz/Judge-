'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
'''
inicio = int(input())
hora1 = map(int,input().split())

fim = int(input())
hora2 = map(int,input().split())

h, m, s = hora1
h2, m2, s2 = hora2

inicio = inicio*24*60
fim = fim*24*60
h = h*60
h2 = h2*60

aux = ((fim-h2-m2)-(inicio+h+m))

dia = (aux/60)//24

print(dia)


