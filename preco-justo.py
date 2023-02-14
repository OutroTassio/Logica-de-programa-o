###
# Construa um algorítimo que, tendo como dados de entrada o preço de um produto e seu código de origem,
# mostre o preço justo de sua procedeência. Caso o código não seja nenhum dos especificados, o produto
# deve assumir como importa

product = str(input('Nome do produto: '))
price = float(input('preço do produto: '))
origin = int(input('Origem do produto: '))
if origin == 1:
    newOrigin = 'Sul'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin == 2:
    newOrigin = 'Norte'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin == 3:
    newOrigin = 'Leste'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin == 4:
    newOrigin = 'Oeste'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin in(7, 8, 9):
    newOrigin = 'Sudeste'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin in range(10, 21):
    newOrigin = 'Centro-Oeste'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
elif origin in(5, 6,) or origin in range(25, 31):
    newOrigin = 'Centro-Oeste'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')
else:
    newOrigin = 'Importado'
    print(f'O {product} custa RS {price} e a origem é {newOrigin}')