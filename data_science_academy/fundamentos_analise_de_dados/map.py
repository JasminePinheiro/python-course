# Módulo é uma arquivo (script)
# Pacote é um conjunto de módulos

def potencia(x):
    return x ** 2

numeros = [1,2,3,4,5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

# Função que retornar a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatura = [0, 22.5, 40, 100]

# Aplicandoa função a cada elemento da lista de temperatura
map(fahrenheit, temperatura)

# Mostrar as temperaturae convertidas em Fahrenheit
list(map(fahrenheit, temperatura))

for temp in map(fahrenheit, temperatura):
    print(temp)
    
# Convertendo para Celsius
map(celsius, temperatura)

list(map(celsius, temperatura))

for temp in map(celsius, temperatura):
    print(temp)

print('\n\n\n')
print('Usando a função lambda')
map(lambda x: (5.0/9)*(x - 32), temperatura)
list(map(lambda x: (5.0/9)*(x - 32), temperatura))


# Somando duas listas 
a = [1,2,3,4]
b = [5,8,7,4]

print(list(map(lambda x,y:x+y, a, b)))

# Somando 3 listas 
a = [1,2,3,4]
b = [5,8,7,4]
c = [5,2,5,5]

print(list(map(lambda x,y,z:x+y+z, a, b,c)))

