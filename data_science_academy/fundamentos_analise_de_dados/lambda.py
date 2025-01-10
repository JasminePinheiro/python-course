def potencia(num):
    resultado = num ** 2
    return resultado

print(potencia(4))

def potencia(num):
   return num ** 2

print(potencia(4))

# simplificando para apenas uma linha de código

def potencia(num): return num ** 2

print(potencia(4))

# usando lambda para simplificar
potencia = lambda num: num ** 2

print(potencia(4))

# usando lambda com mais de uma expressão

potencia = lambda num: (num ** 2, num ** 3)

print(potencia(4))

# usando lambda com chave e valor

potencia = lambda num: {"quadrado": num ** 2, "cubo": num ** 3}

print(potencia(4))

# usando lambda como argumento de outra função

def calculadora(funcao, numero):
    return funcao(numero)

print(calculadora(lambda num: num ** 2, 4))

# usando lambda como função anônima

funcao_anonima = lambda num: num ** 2

print(funcao_anonima(4))

# usando lambda com boolean
Par = lambda x: x%2==0
print(Par(3))



first = lambda s: s[0] 
print(first("Jasmine"))

addNum = lambda x,y : x + y

print(addNum(3,5))