from functools import reduce

lista = [47, 11, 42, 13]
print(lista)

def soma(a,b):
    x = a + b
    return x

print(reduce(soma, lista))

lst = [47, 11, 42, 13]

print(reduce(lambda x,y: x+y, lst))
 
# Podemos atribuir a expressão lambda a uma variável
# Primeiro método
max_find2 = lambda a,b: a if (a > b) else b

# Segundo método
def maior_valor(a,b): 
    if a > b: 
        return a
    else:
        return b
# Retornando o maior valor da minha lista
print(reduce(max_find2, lst))

