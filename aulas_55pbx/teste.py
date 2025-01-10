import requests
import json

# Nomes que vamos pesquisar
nomes = ["ANA", "MARIA", "JOAO"]

# Dicionário para armazenar as frequências
frequencias = {}

# Buscar a frequência de cada nome
for nome in nomes:
    # https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome} teste 

    url = f"https://servicodados.ibge.gov.br/api/v2/nome/nomes/{nome}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
       
        # Armazenar a frequência total
        frequencia_total = sum([periodo['freq'] for periodo in dados['nome']])
        frequencias[nome] = frequencia_total
    else:
        frequencias[nome] = 0  # Nome não encontrado

# Classificar os nomes pela frequência total em ordem decrescente
frequencias_classificadas = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)

# Criar a estrutura do JSON com todas as colocações
resultado = {"colocados": []}

# Adicionar todos os colocados com suas classificações
for i, (nome, frequencia) in enumerate(frequencias_classificadas, start=1):
    resultado["colocados"].append({
        "classificacao": i,
        "nome": nome,
        "frequencia": frequencia
    })

# Salvar os dados em um arquivo JSON
with open('frequencias_nomes.json', 'w') as json_file:
    json.dump(resultado, json_file, indent=4)

# Exibir os dados no console
print(json.dumps(resultado, indent=4))