from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger
import requests
from bs4 import BeautifulSoup

# cria a instância (aplicativo)
app = Flask(__name__)

# documentação
app.config['SWAGGER'] = {
    'title': 'My Flask API',
    'uiversion': 3
}

# instanciar para habilitar documentação
swagger = Swagger(app)

# autenticação
auth = HTTPBasicAuth()

users = {
    'user1': 'password1',
    'user2': 'password2'
}

# toda rota com @auth.login_required exigirá credenciais
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# hello world
@app.route('/')
def home():
    return "Hello, Flask!"

# rota com senha
@app.route('/hello', methods = ['GET'])
@auth.login_required
def hello():
    return jsonify({'message':'Hello World!'})

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

# -------------------------------------------------------------------------------------------- #
# Web Scraping
# -------------------------------------------------------------------------------------------- #

# obter o título
def get_title(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return jsonify({'title':title})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/scrape/title', methods = ['GET'])
@auth.login_required
def scrape_title():
    """
    Extract the title of a web page provided by the URL.
    ---
    security:
        - BasicAuth: []
    parameters:
        - name: url
          in: query
          type: string
          required: true
          description: URL of the web page
    responses:
        200:
            description: Web page title
    """
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    return get_title(url)

# para testar no postman: 
# GET http://127.0.0.1:5000/scrape/title?url=https://postech.fiap.com.br/curso/machine-learning-engineering
# Authorization > Auth Type: Basic Auth > user + password > Send

# obter o conteúdo
def get_content(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headers = []
        for header_tag in ['h1', 'h2', 'h3']:
            for header in soup.find_all(header_tag):
                headers.append(header.get_text(strip = True))

        paragraphs = [p.get_text(strip = True) for p in soup.find_all('p')]
        return jsonify({'headers':headers, 'paragraphs':paragraphs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/scrape/content', methods = ['GET'])
@auth.login_required
def scrape_content():
    """
    Extract headers and paragraphs from a web page provided by the URL.
    ---
    security:
        - BasicAuth: []
    parameters:
        - name: url
          in: query
          type: string
          required: true
          description: URL of the web page
    responses:
        200:
            description: Web page content
    """
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    return get_content(url)

# para rodar localmente
if __name__ == '__main__':
    app.run(debug = True) # facilita testes e mostra erros no navegador
