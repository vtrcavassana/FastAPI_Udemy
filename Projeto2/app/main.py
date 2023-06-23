from fastapi import FastAPI

# Instanciação da aplicação FastAPI
app = FastAPI()

# Endpoint para verificar se a aplicação está rodando corretamente
@app.get('/')
def healthCheck():
    return 'Hello World'