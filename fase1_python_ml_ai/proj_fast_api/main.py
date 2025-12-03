from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

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

# no termminal: uvicorn main:app --reload