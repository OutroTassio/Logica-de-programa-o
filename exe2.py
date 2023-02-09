###
# Fazer algoritimo que calcula a quantidade de lata de tinta, e o custo para pintar tanques cilíndricos
# ###

H = float(input("Altura: "))
R = float(input("Raio: "))
area = (3.14 * (R ** 2)) + (2 * 3.14 * R * H)
litro = area / 3
quantidade = litro / 5
custo = quantidade * 50.00
print(custo, quantidade)
