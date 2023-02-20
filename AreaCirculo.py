###
#  Fazer um programa para ler o valor de "r" do raio de um circulo, e depois mostrar
#  p valor da área do circulo com três casas decimais. A fórmula da área é : area = PI * r²###
from math import pi
r = float(input('Digite o valor do ráio: '))

area = pi * r ** 2

print(f'A área do circulo é {area:.3f}')
