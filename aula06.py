# > Estruturas condicionais

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

"""
Imagine que você queira imprimir "Aprovado(a), caso o estudante tenha uma média 
superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.

"""

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Aprovado(a)')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado(a)')


presenca = float(input('Informe presença do estudante: '))

if media >= 7 and presenca >= 75:
    print('Aprovado(a)')
elif media >=5 and presenca >= 75:
    print('Recuperação')
else:
    print('Reprovado(a)')