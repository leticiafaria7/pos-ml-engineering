from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

# title, version e description aparecem na doc/docs
# app é a aplicação principal, similar a Flask(__name__)
app = FastAPI(
    title = 'My FastAPI API',
    version = '1.0.0',
    description = 'API de Exemplo com FastAPI'
)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

security = HTTPBasic()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users and users[username] == password:
        return username
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'Credenciais inválidas',
        headers = {'WWW-Authenticate':'Basic'}
    )

# rotas declaradas via decorators @app.get(), @app.post(), etc
@app.get('/')
# async/await aproveita recursos assíncronos do python
async def home():
    return 'Hello, FastAPI!'

@app.get('/hello')
async def hello(username: str = Depends(verify_password)):
    return {'message':f'Hello, {username}!'}

# Lista de itens em memória para operações CRUD
items = [] # armazena itens como dicionários

class Item(BaseModel):
    name: str
    description: str = None
    price: float = None
    quantity: int = None

@app.get('/items')
async def get_items():
    return items

@app.post('/items', status_code = 201)
async def create_item(item: Item):
    items.append(item.dict())
    return item

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items):
        items[item_id].update(item.dict())
        return items[item_id]
    raise HTTPException(status_code = 404, detail = 'Item não encontrado')

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        return removed_item
    raise HTTPException(status_code = 404, detail = 'Item não encontrado')

# no termminal: uvicorn main:app --reload