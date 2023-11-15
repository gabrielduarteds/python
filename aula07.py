numero_sorteado = 7

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns! Você acertou!')

# Contador incremental

contador = 0

while contador < 5:
    print(contador)
    contador= contador + 1
    