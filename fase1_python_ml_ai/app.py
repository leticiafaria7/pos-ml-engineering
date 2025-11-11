from flask import Flask, jsonify, request

# cria a instância (aplicativo)
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

items = []

# 1º passo CRUD (Read - GET)
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# 2º passo CRUD (Create - POST)
@app.route('/items', methods = ['POST'])
def create_item():
    data = request.get_json() # envia json no corpo, armazena em itens de forma in-memory, retorna o objeto recém criado
    items.append(data)
    return jsonify(data), 201 # status de created

# 3º passo CRUD (Update - PUT)
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    data = request.get_json()
    if 0 <= item_id < len(items): # ver se o item_id está em um intervalo válido
        items[item_id].update(data)
        return jsonify(items[item_id])
    return jsonify({'error': 'Item not found'}), 404

# 4º passo CRUD (Delete - DELETE)
@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_items(item_id):
    if 0 <= item_id < len(items):
        removed = items.pop(item_id)
        return jsonify(removed)
    return jsonify({'error': 'Item not found'}), 404

# para rodar localmente
if __name__ == '__main__':
    app.run(debug = True) # facilita testes e mostra erros no navegador