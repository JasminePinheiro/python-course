class Algoritmo():
  def __init__(self, tipo_algo):
    self.tipo = tipo_algo
    print("Construtor chamado para criar um objeto desta classe")

algo = Algoritmo(tipo_algo= 'Teste')

print(algo.tipo)