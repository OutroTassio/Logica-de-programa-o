###
# Fazer um programa para ler o nome de um funcionário, o valor que ele recebe por hora,
# e a quantidade de horas trabalhadas por ele. Ao final, mostrar o valor do pagamento do
# funcionário com uma mensagem explicativa, Ex: "O pagamento para Maria deve ser R$ 8000.00"###

nome = str(input('Nome: '))
valorHora = float(input(f'Valor da hora de {nome}: '))
horasTrablhadas = float(input(f'Horas trabalhadas por {nome}: '))

pagamento = horasTrablhadas * valorHora

print(f'O pagamento para {nome} é R${pagamento:.2f}')
