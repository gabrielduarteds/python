# > Métodos de Listas

lista = [1, 3, 12, 8, 2]

# append

print('Antes do append:', lista)

lista.append(4)

print('Depois do append:', lista)

# insert

lista.insert(0, 5)

print('Depois do insert:', lista)

# extend

lista2 = [6, 10, 9, 11]

lista.extend(lista2)

print('Depois do extend:', lista)

# pop

lista.pop()

print('Depois do pop:', lista)

lista.pop(0)

print('Depois do pop com índice:', lista)

# remove

lista.remove(3)

print('Depois do remove:', lista)

# count

print('Quantidade de números 2 na lista:', lista.count(2))

# index

print('Índice do elemento 12:', lista.index(12))

# sort

lista.sort(reverse=True)

print('Depois do sort:', lista)

# > Funções para listas

# len

print(len(lista))

# sum

print(sum(lista))

# max

print('Maior elemento da lista:', max(lista))

# min

print('Menor elemento da lista:', min(lista))