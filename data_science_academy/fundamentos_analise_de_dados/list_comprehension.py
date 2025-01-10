# Usando o List comprehension e Dict comprehension

# imprimindo os valores de 0 a 9
print([x for x in range(10)])

lista_numerica = [x for x in range(10)]
print(lista_numerica)

lista_numerica = [x for x in range(10) if x<5]
print(lista_numerica)


lista_frutas = ['banana', 'maça', 'perâ', 'melancia', 'cereja']

nova_lista = []

# percorrendo a lista do jeito tradicional
for fruta in lista_frutas:
    if "m" in fruta:
        nova_lista.append(fruta)
        
print(nova_lista) 

nova_lista = [fruta for fruta in lista_frutas if 'm' in fruta]

print(nova_lista)

# Dict comprehension

dicionario = {'a': 1, 'b': 2, 'c': 3}

novo_dicionario = {chave: valor for chave, valor in dicionario.items()}
print(novo_dicionario)
novo_dicionario = {chave: valor for chave, valor in dicionario.items() if valor > 1}
print(novo_dicionario)


# Dicionario de aluno e notas
dict_alunos = {'Jasmine':10, 'Ana':9, 'Beatriz':5, 'Carlos':8}

dict_alunos_status = {k:('Aprovado' if v > 7 else 'Reprovado') for(k,v) in dict_alunos.items()}

print(dict_alunos_status)