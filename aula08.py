
"""for var in range(10): # range com 1 parâmetro = 0 - 9
    print(var)"""

"""for var in range(1, 11): # range com 2 parâmetros = 1 - 10. Sempre menor que o segundo parâmetro
    print(var)"""

"""for var in range(1, 12, 3): # range com 3 parâmetros. "Pula" a contagem pelo terceiro parâmetro
    print(var)"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(soma/3)

