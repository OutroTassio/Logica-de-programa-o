# Algoritimo para descobrir se um triângulo é equilátero, isóscele ou escaleno

A = float(input('Valor de A'))
B = float(input('Valor de B'))
C =float(input('Valor de C'))

if (A < B + C) and (B < A + C) and (C < A + B):
    if A == B and A == C:
        print(f'A -> {A} B -> {B} e C -> {C}')
        print('Triângulo equilátero')
    elif (A == B) or (A == C) or (B == C):
        print(f'A -> {A} B -> {B} e C -> {C}')
        print('Triângulo isóscele')
    elif(A != B) or (A != C) or (B != C):
        print(f'A -> {A} B -> {B} e C -> {C}')
        print('Triangulo escaleno')
else: print('It´s not a triangle')
