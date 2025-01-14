# # abrindo o arquivo para leitura
arq1 = open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt', 'r')

type(arq1)

print(arq1.read())

# Retorna a quantidade de caracteres
print(arq1.tell())

# Retorna o inicio do arquivo
# print(arq1.seek(1,0))

# Lendo os primeiros 5 caracteres
print(arq1.read(5))

# Abrindo arquivo para gravação
arq2 = open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo2.txt', 'w')

# Gravando arquivo
arq2.write("Oiee Jasmine2")

arq2.close()

arq2 = open(r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\arquivo2.txt', 'r')

print(arq2.read())

# Acrescentando contéudo
arq2 = open(r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\arquivo2.txt', 'a')

arq2.write("\nTeste Jasmine")

arq2.close()

arq2 = open(r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\arquivo2.txt', 'r')

print(arq2.read())

# arquivo csv contando o número de linhas

arq3 = open(r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\salarios.csv', 'r')

data = arq3.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0 
for row in full_data:
    count += 1
    
print(count)

# contando o numero de colunas
arq4 = open(r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\salarios.csv', 'r')
data = arq4.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
    
count = 0

for column in first_row:
    count = count + 1

print(count)

# Importando um Dataset com Pandas
import pandas as pd

arquivo = (r'C:\Users\Jasmine\Documents\python-course\data_science_academy\fundamentos_analise_de_dados\salarios.csv')

df = pd.read_csv(arquivo)

df.head()

print(df.head())


# Importando o módulo os
import os

# Criando o arquivo
texto = 'Jasmine kkkk'
arquivo2 = open(os.path.join('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt'), 'w')

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo2.write(palavra + ' ')
    
# Fechando o arquivo
arquivo2.close()

# Lendo o arquivo
arquivo2 = open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt', 'r')
conteudo = arquivo2.read()
arquivo2.close()

print(conteudo)

# Usando a expressão 'with'
# com a expressa with o método close é executado automáticamente
# é extremamente importante fechar os arquivos para evitar que o arquivo fique interrompido 

with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt', 'r') as arquivo2:
    conteudo = arquivo2.read()
    
print(len(conteudo))
texto = "Aprender é uma jornada contínua, cheia de descobertas. Cada pequeno passo nos aproxima de grandes conquistas."

with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt', 'w') as arquivo2:
    arquivo2.write(texto[:19])
    arquivo2.write('\n')
    arquivo2.write(texto[27:34])
    
arquivo2 = open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\arquivo.txt', 'r')
conteudo = arquivo2.read()
arquivo2.close()

print(conteudo)

# Lendo arquivos csv
import csv

with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\numeros.csv', 'w') as numeros:
    
    # cria o objeto de gravação
    writer = csv.writer(numeros)
    
    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('1', '2', '3'))


with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\numeros.csv', 'r', encoding='utf8', newline='\r\n') as numeros:
    leitor = csv.reader(numeros)
    for x in leitor:
        print(x)


with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\numeros.csv', 'r', encoding='utf8', newline='\r\n') as numeros:
    leitor = csv.reader(numeros)
    dados = list(leitor)
    

print(dados)     

for linha in dados[:1]:
    print(linha)
    

# Importando arquivo Json
import json

# Exemplo de dicionário em Python
dados_pessoa = {
    "nome": "Maria",
    "idade": 28,
    "profissao": "Engenheira",
    "cidade": "São Paulo",
    "hobbies": ["ler", "viajar", "cozinhar"]
}

# Convertendo dicionário para um objeto json
json.dumps(dados_pessoa)

# Criando um arquivo json
with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dado.json', 'w') as file:
    file.write(json.dumps(dados_pessoa))
    
# Leitura de arquivo Json
with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dado.json', 'r') as file:
    text = file.read()
    data = json.loads(text)
    
print(data['nome'])

# Imprimindo um arquivo da web
from urllib.request import urlopen

response = urlopen("https://jsonplaceholder.typicode.com/users").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print('Nome:', dados['name'])
print('Email:', dados['email'])
print('Endereço:', dados['address']['street'])

arquivo_fonte = 'C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dado.json'
arquivo_destino = 'C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dados.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
     outfile.write(text)
     
# Método 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())


# Leitura do arquivo txt
with open('C:\\Users\\Jasmine\\Documents\\python-course\\data_science_academy\\fundamentos_analise_de_dados\\dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)    
    
print(dados)