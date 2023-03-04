###
# Problema "temperatura"
# Fazer um algoritimo para converter a temperatura de Celsius para Fahrenheit
###

temperatura = str(input("Você vai digitar a temperatura em qual escala? (C / F) ")).lower()

if temperatura[0] in 'f':
    F = float(input('Digite a temperatura em Fahrenheit: '))
    C = 5 / 9 * (F - 32)
    print(f'A temperatura equivalente em Celsius: {C:.2f}')
elif temperatura[0] in 'c':
    C = float(input('Digite o valor em Celsius: '))
    F = 9 * C / 5 + 32
    print(print(f'A temperatura equivalente em Fahrenheit: {F:.2f}'))
