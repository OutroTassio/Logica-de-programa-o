#entrada de dados
nota1 = float(input("Nota : "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

#proocessamento

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"

#saída de dados

print(f'Média {media}, {situacao}')