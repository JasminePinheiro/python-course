lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [1,3, 4, 6, 8]


# Loop externo 
for elemento_lista1 in lista1:
    # Loop interno
    for elemento_lista2 in lista2:
        if elemento_lista1 == elemento_lista2:
            print(f"Elemento {elemento_lista1} encontrado em ambas listas.")
            break
        
# Some os numeros pares da primeira lista com os números pare da segunda lista
soma = 0;

for elemento_lista1 in (lista1, lista2):
   for num in elemento_lista1:
       if num % 2 == 0:
            soma += num
print("A soma de todos os números pares é %s" %soma)

# Loop em matrizes
matrizes = [[43, 23, 43],[100, 203, 73],[20, 21, 30]]
maior_numero = 0
for linha in matrizes:
    for num in linha:
        if num > maior_numero:
            maior_numero = num
print("Maior numero é %d" %maior_numero)


# Listando as chaves 
dict = {'k1':'Python','k2':'R', 'k3': 'JavaScript'}
for item in dict:
    print(item)
    
    
# Loop While
valor = 0

while valor < 10:
    print(valor)
    valor += 1
    
# PASS BREAK E CONTINUE
    
primos = []
eh_primo = 0

for num in range(2, 31):
    eh_primo = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
          eh_primo = False
          break
        i += 1
      
    if eh_primo:
        primos.append(num)
print(primos)

# o último número é exclusivo nesse caso abaixo vamos imprimir os números de 50 a 100
# imprimindo os números pares
for i in range(50, 101, 2):
    print(i)