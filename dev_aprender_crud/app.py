# API é um conjunto de regras que permite que diferentes sistemas ou aplicações "conversem" e troquem informações entre si.
# Sugestões para produção - Nginx, Apache, Gunicorn 
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien'
        
    },
    {
        'id': 2,
        'titulo': 'A Cidade de Glass',
        'autor': 'Miguel de Cervantes'
    },
    {
        'id': 3,
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 4,
        'titulo': 'A Divina Comédia',
        'autor': 'Miguel de Cervantes'
    }
]

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (por ID)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
   livro_alterado = request.get_json() 
   for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
         
# Criar
@app.route('/livros',methods=['POST'])
def inclur_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Exclui
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)
            
app.run(port=5000,host='localhost',debug=True)
