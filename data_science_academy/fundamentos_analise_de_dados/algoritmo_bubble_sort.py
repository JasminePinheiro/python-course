# # Algoritmo Bubble Sort

# Primeira rodada (i = 0):
# n - i - 1 = 8 - 0 - 1 = 7
# O for j in range(0, 7) vai comparar os elementos com os índices de 0 a 6.
# Ele vai comparar todos os números da lista (exceto o último) e empurrar o maior número para o final.
# Comparações e trocas:

# Compare 6 e 3: Troque → [3, 6, 12, 7, 5, 3, 9, 1]
# Compare 6 e 12: Não troca.
# Compare 12 e 7: Troque → [3, 6, 7, 12, 5, 3, 9, 1]
# Compare 12 e 5: Troque → [3, 6, 7, 5, 12, 3, 9, 1]
# Compare 12 e 3: Troque → [3, 6, 7, 5, 3, 12, 9, 1]
# Compare 12 e 9: Troque → [3, 6, 7, 5, 3, 9, 12, 1]
# Compare 12 e 1: Troque → [3, 6, 7, 5, 3, 9, 1, 12]
# Agora o número 12 está na posição correta, no final da lista.


lista = [6, 3, 12, 7, 5, 3, 9, 1]


def bubble_sort(arr):

    n = len(arr)

    # Para cada elemento i do array
    for i in range(n):

        # Para cada elemento j do array
        for j in range(0, n - i - 1):  # 0, 8-0-1 = 7

            # Se elemento i for maior que elemento J
            if arr[j] > arr[j + i]:

                # Troque os elementos i e j
                arr[j], arr[j + i] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(lista))
