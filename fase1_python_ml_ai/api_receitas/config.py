# configurações da aplicação
# mais configurações em: https://flask.palletsprojects.com/en/stable/config/

# class Config:
#     SECRET_KEY = 'sua_chave_secreta'
#     CACHE_TYPE = 'simple'
#     SWAGGER = {
#         'title': 'Catálogo de Receitas Gourmet',
#         'uiversion': 3
#     }
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = 'sua_chave_jwt_secreta'

# configurações de segurança
SECRET_KEY = 'sua_chave_secreta'
JWT_SECRET_KEY = 'sua_chave_jwt_secreta'

# caching básico
CACHE_TYPE = 'simple'

# título e versão da doc interativa
SWAGGER = {
    'title': 'Catálogo de Receitas Gourmet',
    'uiversion': 3
}

# definição do banco
SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'

# evitar warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False
