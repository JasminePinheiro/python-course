def split_string_palavras(text):
    return text.split(' ')

texto = "Esta função será bastante útil"

print(split_string_palavras(texto))


# Fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)
        
split_string_letras(texto)        
