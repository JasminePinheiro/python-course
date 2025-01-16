import numpy as np

arr1 = np.array([2,4,5,4,7,8,9])
print(arr1)

print(arr1[1:4])
print(arr1 % 2 == 0) # retorna um boleando # saida[ True  True False  True False  True False]

mask = arr1 % 2 == 0

print(arr1[mask])

# Não é possível incluir elemento de outro tipo no numpy, diferente de uma lista convencional

try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida")
    

arr2 = np.array([2,4,5,4,7,8,9])

print(arr2.cumsum()) # vai somando a cada array

arr3 = np.arange(0, 50, 5) # o 50 é exclusivo por isso não aparece na lista função parecida com range

print(arr3)

# Manipulando Matrizes
arr4 = np.array([[1,2,3], [4,5,6], [2,9,10]]) # Criando matrizes
print(arr4)

# Não usando o numpy
arr5 = [[1,2,3], [4,5,6], [2,9,10]]
print(arr5)

# Indexação da matriz -> linha X coluna
print(arr4[2,1]) # saída 9

print(arr4[0:2,2]) # saída 3,6

print(arr4[1,]) # saída [4 5 6]

# Manipulando Objetos de 3 e 4 Dimensões
arr_3d = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ],
    [
        [25, 26, 27, 28],
        [29, 30, 31, 32],
        [33, 34, 35, 36]
    ]
])

print(arr_3d)

print(arr_3d.shape) # saída 3 elementos, 3 linhas, 4 colunas

print(arr_3d[0, 2, 1]) # 10

# Manipulando Arquivos com Numpy
import os
filename = os.path.join('C:\\Users\\Jasmine\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dataset.csv')

# Carregando um dataset para dentro de um array 
# Estou identificando apenas as colunas com números (0,1,2,3) o skiprows para tirar o cabeçalho
arr6 = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
print(arr6)

# Carragando apenas duas variáveis (colunas) do arquivo
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
import matplotlib.pyplot as plt
# separando as duas variáveis  (gerando gráficos)
plt.plot(var1, var2, 'o', markersize=6, color='red')
plt.show()