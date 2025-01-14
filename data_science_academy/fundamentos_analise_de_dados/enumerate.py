def criar_lista():
    lista = []
    for i in range(0,6):
        lista.append(i)
    print(lista)
    
criar_lista()

seq = ['a', 'b', 'c']

enumerate(seq)

# A função enumerate retorna chave e valor
print(list(enumerate(seq)))

for indice, valor in enumerate(seq):
    print(indice, valor)
    
lista = ['Jasmine', 'Joyce', 'Iracema']

for i, item in enumerate(lista):
    print(i, item)
    
for i, item in enumerate('Data Science Academy'):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)
    
# Podemos passa no enmerate uma lista, tupla, dicionário...