# Importando a biblioteca fastapi que será utilizada para criar a API
from fastapi import APIRouter

# Iniciando o roteador da API, que será responsável por direcionar as requisições aos endpoints corretos
roteador = APIRouter()

# Rota que retorna uma string quando '/conversor' é acessada
# @roteador.get('/conversor')
# def conversor():
#     return 'Funcionou!'

# Path Parameter
# O parâmetro 'moeda' na rota indica que o valor será fornecido na URL.
# Por exemplo, se você acessar '/conversor/usd', o valor de 'moeda' será 'usd'.
@roteador.get('/conversor/{moeda}')
def conversor(moeda: str):
    return 'Funcionou!'
