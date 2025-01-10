# Dicionário de lista

dict1 = {
    "chave1": 1234,
    "chave2": [11, 33, 44, 66],
    "chave3": ["picanha", "fraldinha", "alcatra"],
}

print(dict1["chave3"])

# Acessando um item da lista, dentro do dicionário
print(dict1["chave3"][0].upper())
print(dict1["chave3"][1].lower())

dict1["chave2"][0] -= 2

print(dict1)

# Criando dicionários alinhados
dict_aninhado = {
    "key1": {"Key2_aninhada": {"key3_aninhada": "Dict aninhado em python"}}
}
print(dict_aninhado)
