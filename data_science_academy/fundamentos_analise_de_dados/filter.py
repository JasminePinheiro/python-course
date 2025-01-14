def verificaPar(num):
    if num % 2  == 0:
        return True
    else:
        return False

print(verificaPar(34))

def criaLista():
    lista = []
    for i in range(0, 20):
        lista.append(i)
    return lista
    
lista2 = criaLista()
print(lista2)

print('\n Imprimindo os numeros pares')
print(list(filter(verificaPar, lista2)))

print('\n Usando a funcao lambda')
print(list(filter(lambda x: x%2 == 0, lista2)))

# numeros maiores que 8
print(list(filter(lambda a: a > 8, lista2)))

