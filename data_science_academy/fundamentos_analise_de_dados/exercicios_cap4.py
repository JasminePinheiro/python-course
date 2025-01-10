# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = [1, 2, 3, 4, 5]
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
nome = "Jasmine"
sobrenome = "Souza"

nome_completo = f'{nome} {sobrenome}'
nome_completo2 = 'Jasmine ' + 'Pinheiro'
print(nome_completo)
print(nome_completo2)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict1 = {}
print(dict1)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict2 = {"Jasmine":24, "Pamela":30, "Vanessa":50}
print(dict2)

# Exercício 7 - Adicione mais dois elemento ao dicionário criado no exercício anterior e imprima na tela
dict2.update({"Carla":40, "Sandra":90})
print(dict2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dict3 = {"Jasmine":24, "Numeros":[1,2], "Vanessa":50}
print(dict3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista

tupla2 = (2,1),
dict4 = {"Jasmine":22, "Marcos":14}

lista3 = ["Jasmine", tupla2, dict4, 5.6]
print(lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[:18])

teste = "Jasmine"
print(teste[1])