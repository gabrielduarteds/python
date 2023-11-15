# > Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando listas 
lista = []
lista = list()
lista = [26, 'Gabriel', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices(fatiamento)

lista = [10, 'Gabriel', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4])
print(lista[-1]) #último elemento da lista

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:]) # pega a lista toda
print(lista[3:6:2]) # parecido com range

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

#2. Utilizando os índices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(i)
    

for i in range(len(lista)):
    print(lista[i])