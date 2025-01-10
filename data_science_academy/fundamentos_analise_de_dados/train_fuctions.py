# *varTuple conseguimos passar qualquer quantidade de números

# def printVarInfo(args, *varTuple):
#     print("O parametro passado foi", args)
    
#     for item in varTuple:
#         print("Item da tupla:", item)
#     return

# printVarInfo(10, (10))

# # Funçoes Built-in (comandos pré-definidos em python)
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print(f"Você é maior de idade, você ${idade} anos")
# else:
#     print("Você é menor de idade")
    
    
# num1 = 13
# num1 = str(num1)
# print(f'{num1}')

# print(type(num1))

import math
def numPrimo(num):
    if(num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

print(numPrimo(7))