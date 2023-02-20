###
# Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como
# o total de combustivel gasto por este carro e o preço da gasolina ao percorrer tal distâncoa. Seu programa deve
# mostrar o consumo médio do carro, com três casas decimais e o valor em dinheiro gasto.###

distance = float(input('Distância percorrida: '))
consumption = float(input('Litros de gasolina gastos: '))
gasPrice = float(input('Preço da gasolina: '))
autonomy = distance / consumption
moneySpent = gasPrice * consumption

print(f'O consumo médio do seu carro é de {autonomy:.3f}km/L')
print(f'Você gastou {moneySpent:.2f} para percorrer {distance}km')