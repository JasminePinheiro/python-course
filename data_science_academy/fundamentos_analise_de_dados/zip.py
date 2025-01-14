# Função Zip

def criarLista():
    lista = []
    for i in range(0, 30):
        lista.append(i)
    return lista

lista1 = criarLista()
lista2 = criarLista()

zip(lista1, lista2)

resultado = list(zip(lista1,lista2))
print(resultado)

# A função zip retorna a combinação se não tiver números iguais ela descarta
# Ex:
print(list(zip('ABC', 'YU')))

# Quando trabalhamos com dicionários a função zip só junta as chaves
# EX:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 7, '3': 8, 'f': 9}

print(list(zip(d1,d2)))

# Para pegar os valores
print('\n')
print(list(zip(d1, d2.values())))
