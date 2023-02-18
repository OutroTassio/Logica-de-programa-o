###
# O IMC -Índice de Massa Corporal - é um critério da  Organização Mundial da Saúde
# para indicar a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura)².
# Elabore um algoritimo que oeia o peso e a altura  de um adulto e mostre sua condição.###

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura)**2
if imc < 18.5:
    print(f'Você está abaixo do peso ({imc:.2f})');
elif imc <= 25:
    print(f'Você está no peso ideal ({imc:.2f})')
elif imc <= 30:
    print(f'Você está acima do peso ({imc:.2f})')
else:
    print(f'Você está Obeso ({imc:.2f})')