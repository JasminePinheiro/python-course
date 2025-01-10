# São imutaveis
tupla1 = ("Geografia", 23, "Elefante", 9.8, "Python")
print(tupla1)
print(tupla1[1:])

# Usando a função list() para converter uma tupla para lista 
lista1 = []

lista1 = list(tupla1)

print(type(lista1))

lista1.append("Teste")
print(lista1)

# Usando a função tuple() para converter a lista em tupla
tupla2 = tuple(lista1)

print(type(tupla2))