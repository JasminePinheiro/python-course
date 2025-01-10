# Trabalhando com listas

lista_1 = ["arroz, frango, tomate, leite"]

print(type(lista_1))

print(lista_1)

lista_2 = [23, 100, "Cientista de Dados"]

# Criando listas alinhadas
lista_3 = [[1, 2, 3], [10, 15, 14], [20, 30, 40]]

print(lista_3)

first_list = lista_3[0]

second_list = lista_3[2]
print(first_list[0])

# Atribuindo à variavel 'A' o primeiro valor da primeira lista
a = lista_3[1][2]
b = lista_3[1][2] + 10
print(a)
print(b)

# Concatenando Listas
third_list = first_list + second_list

print(third_list)

# Operador in
lista_teste_op = [100, 2, -5, 3.4]
print(10 in lista_teste_op)  # return false

# Funções Built-in
lista_numeros = [10, 20, 40, -3.4]
len(lista_numeros)

lista_numeros.append(30)


print(lista_numeros)

new_lista = []

# Copiando os itens de uma lista para outra
for item in lista_numeros:
    new_lista.append(item)

print(new_lista)

cidades = ["Recife", "Manaus", "Salvador"]
cidades.append(["Fortaleza", "Palmas"])  # Cria uma nova lista dentro da lista
print(cidades)
cidades.extend(["Fortaleza", "Palmas"])  # Acrescenta valores a lista existente
print(cidades)

cidades.index("Recife")

cidades.insert(2, 10)
# cidades.pop(1)  # remove de um indice
cidades.remove("Fortaleza")
cidades.remove(cidades[4])
print(cidades)
