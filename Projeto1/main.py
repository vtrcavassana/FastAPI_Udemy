from fastapi import FastAPI
from routes import roteador

app = FastAPI()
app.include_router(router=roteador)

@app.get('/')
def home():
    return 'AQUI FOI!'