class Algoritmo():
  def __init__(self, tipo_algo):
    self.tipo = tipo_algo
    print("Construtor chamado para criar um objeto desta classe")

algo = Algoritmo(tipo_algo= 'Teste')

print(algo.tipo)

# Os métodos sempre inclui o parâmetro self como o primeiro argumento que é usando para se referir ao objeto atual da classe 
# O método __init__ em Python é um método especial usado para inicializar um objeto quando ele é criado
class Circulo():
    
    pi = 3.14
    
    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5
    def __init__(self, raio = 5):
       self.raio = raio
    
    # calcula a área
    def area(self):
        return (self.raio * self.raio) + Circulo.pi
    
   # gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio
        
    # obter o raio do circulo    
    def getRaio(self):
        return self.raio
    

# criando o objeto circ, uma instâmcia da classe Circulo()
circ = Circulo()

print('A área igual a:', circ.area())

# Exemplo de polimorfismo -> Refere a habilidade de um objeto responder de diferentes forma a uma mesam mensagem
# Polimorfismo - Permite que diferentes classes tenham métodos com o mesmo nome, mas com implementações diferentes. 
# SuperClasse
# Ela permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse ou classe base). 

# Superclasse
class Veiculo:
    
    def __init__(self, marca, modulo):
       self.marca = marca
       self.modulo = modulo
       
    def acelerar(self):
        pass
    
    def frear(self):
        pass
    

# Subclasse
class Carro(Veiculo):
    
    def acelerar(self):
        print("O carro está acelerando")
        
    def frear(self):
        print("O carro está freando")
  
# Subclasse  
class Moto(Veiculo):
    
    def acelerar(self):
        print("O moto está acelerando")
        
    def frear(self):
        print("O moto está freando")
        
# Subclasse  
class Aviao(Veiculo):
    
    def acelerar(self):
        print("O aviao está acelerando")
        
    def frear(self):
        print("O aviao está freando")
    
    def decolar(self):
        print("O aviao está decolando")
        
        

# Cria objetos

lista_veiculos = [Carro("kkk", "ttt"), Moto("www", "ggg"), Aviao("ttt", "bla")]

for item in lista_veiculos:
    
    item.acelerar()
    
    item.frear()
    
    if isinstance(item, Aviao):
        item.decolar()
    
    print('---')