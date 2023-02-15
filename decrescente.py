###
# Escreva um slgoritimo que leia 3 valores inteiros e diferentes e mostre-os em ordem decrescente.###

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2:
    n1, n2 = n2, n1
if n1 < n3:
    n1, n3 = n3, n1
if n2 < n3:
    n2, n3 = n3, n2
print(f'Os números digitados em ordem decrescente são: {n1}, {n2}, {n3}')
