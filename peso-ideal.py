###Tendo como dados de entrada o sexo de uma pessoa, construa um algoritimo que calcule o peso ideal, utilizando a seguinte formula:
# *Para homens: (72,7 * h) - 58;
# *para mulheres: (62,1 *h) - 44.###

h = float(input('Altura: '))
sexo = str(input('Sexo: ')).lower()
if 'm' in sexo:
    sexo = 'masculino'
elif 'f' in sexo:
    sexo = 'feminino'
else:
    print('O valor de sexo não é válido')

if sexo == 'masculino':
    pesoIdeal = (72.7 * h) - 58
    print(f'Você é homem e seu peso ideal é {pesoIdeal}')
elif sexo == 'feminino':
    pesoIdeal = (62.1 * h) - 44.7
    print(f'Você é mulher e seu peso ideal é {pesoIdeal}')
