###
# Fazer um programa para ler uma duração de tempo em segundos, daí imprimit
# na tela esta duração no formato horas:minutos:segundos.
# ###
from math import floor
duracao = int(input('Digite a duração em segundos: '))

horas = duracao // 3600

resto = duracao % 3600

minutos = resto // 60

segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')