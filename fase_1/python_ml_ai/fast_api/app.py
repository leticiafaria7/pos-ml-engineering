from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# no terminal: alembic init alembic
# alterar arquivo alembic/env.py (configurações do repositório)
# no terminal: alembic revision --autogenerate -m "Criação das tabelas iniciais"
# no terminal: alembic upgrade head
# adicionar coluna de data de nascimento no arquivo models.py
# no terminal: alembic revision --autogenerate -m "comentário atualização"
# no terminal: alembic upgrade head

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# importa os modelos
import models

if __name__ == '__main__':
    app.run(debug = True)