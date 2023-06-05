# Importando as bibliotecas necessárias
from fastapi import FastAPI
from routes import roteador

# Iniciando a aplicação FastAPI
app = FastAPI()

# Incluindo o roteador na aplicação principal
app.include_router(router=roteador)

# Rota padrão que retorna uma string quando a URL base é acessada
@app.get('/')
def home():
    return 'AQUI FOI!'
