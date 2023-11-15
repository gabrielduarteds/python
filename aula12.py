# > Dicionários

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Gabriel', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['altura'])

# Adicionando elementos em um dicionário

dicionario['analista'] = True

print(dicionario)

dicionario['altura'] = 1.80 # se já houver uma chave ele irá sobrescrever

# Iterando sobre um dicionário

for var in dicionario:
    print(var)

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('idade' in dicionario)