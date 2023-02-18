###
# escrever um algoritimo que resolva uma equação de segundo grau###
import numpy as np
import matplotlib.pyplot as plt
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c ='))

if a != 0:
    eq = "Equação de segundo grau"
    delta = b**2 - 4 * a * c
    if delta < 0:
        print(f'Delta = {delta}')
        print('Não existem raizes reais!')
    elif delta == 0:
        x1 = -b/(2 * a)
        print(f'Delta = {delta}')
        print(f"x' = c'' = {x1}")
    else:
        x1 = (-b - (delta)**0.5) / (2 * a)
        x2 = (-b + (delta)**0.5) / (2 * a)
        print(f"x' = {x1}")
        print(f"x'' = {x2}")
else:
    print('O valor informado não é uma equação de segundo grau!')

x = np.linspace(-10, 10, 100)
y = a * x**2 + b * x + c
eq = "Equação de primeiro grau"

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")

plt.title(eq)
plt.show()
