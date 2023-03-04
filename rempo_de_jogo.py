###
# Problema "tempo de jogo"
# Leia a hora inicial e hora final de um jogo. A seguir calcule a duração do jogo, sabendo
# que o mesmo pode começar em um dia e terminar em outro, tendo como duração mínima de
# 1 hora e máxima 24 horas###

hi = int(input('Hora inicial: '))
hf = int(input('Hora final: '))
duracao = 0
if hf > hi:
    duracao = hf - hi
else:
    duracao = 24 - hi + hf

print(f'O jogo durou {duracao} hora(s)')
