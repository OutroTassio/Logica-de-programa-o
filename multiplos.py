###
# Fazer um programa que leia 2 números inteiros, e dizer se um é multiplo do outro.
# Os múmeros devem ser digitados em qualquer ordem.###

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if (x % y == 0) or (y % x == 0):
    print('São multiplos')

else:
    print('Não são multiplos')
