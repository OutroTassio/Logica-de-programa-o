###
# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que da direito
# a 100 minutos de telefone. Cada minuto que exeder a franquia de 100 minutos
# custa R$ 2.00. Fazer um programa para ler a quantidade de minutos que uma pessoa
# consumiu, daí uma pessoa consumiu, daí mostrar o valor a ser pago.
# ###

valorPlano = 50
minutosPlano = 100
valorPagar = 0
minutosReais = int(input('Digite a quantidade de minutos: '))
if minutosReais <= 100:
    valorPagar = valorPlano
elif minutosReais > minutosPlano:
    minutosAdicionais = minutosReais - minutosPlano
    valorPagar = 2 * minutosAdicionais + valorPlano
print(f'Valor a pagar: R$ {valorPagar:.2f}')

