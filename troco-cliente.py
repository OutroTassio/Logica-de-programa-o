

produto = str(input('nome do produto: '))
preco = float(input(f'preço de {produto}: '))
quantidade = int(input(f'Quantidade de {produto}: '))
dinheiroRecebido = float(input('Dinheiro recebido: '))

totalReceber = preco * quantidade
troco = dinheiroRecebido - (preco * quantidade)

print('='* 25)
print(f'Produto: {produto}')
print(f'Unidades compradas: {quantidade}')
print(f'Dinheiro recebido: R${dinheiroRecebido:.2f}')
print('-' * 25)
print(f'Total á receber: {totalReceber:.2f}')
print(f'Troco: R${troco:.2f}')
