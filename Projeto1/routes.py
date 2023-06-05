from fastapi import APIRouter

roteador = APIRouter()

@roteador.get('/conversor')
def conversor():
    return 'Funcionou!'