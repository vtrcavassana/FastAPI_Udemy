# Importando as bibliotecas necessárias
from fastapi import APIRouter

# Iniciando o roteador
roteador = APIRouter()

# Rota que retorna uma string quando '/conversor' é acessada
@roteador.get('/conversor')
def conversor():
    return 'Funcionou!'
