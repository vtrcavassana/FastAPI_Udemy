# Importando a biblioteca fastapi que será utilizada para criar a API
from fastapi import APIRouter, Query, Path
from conversorMoedaSync import conversorSync
from conversorMoedaAsync import conversorAsync
from asyncio import gather

# Iniciando o roteador da API, que será responsável por direcionar as requisições aos endpoints corretos
roteador = APIRouter()

# O método a seguir é um exemplo de endpoint de rota. Ele foi comentado por não estar sendo usado no momento
# Rota que retorna uma string quando '/conversor' é acessada
# @roteador.get('/conversor')
# def conversor():
#     return 'Funcionou!'

# Outro exemplo de endpoint de rota, também comentado. Esse usa um parâmetro do caminho chamado 'moeda'
# Path Parameter
# O parâmetro 'moeda' na rota indica que o valor será fornecido na URL.
# Por exemplo, se você acessar '/conversor/usd', o valor de 'moeda' será 'usd'.
# @roteador.get('/conversor/{moeda}')
# def conversor(moeda: str):
#     return 'Funcionou!'

# Este é um exemplo de endpoint de rota que usa parâmetros de consulta. Também foi comentado
# Query Parameter
# Aqui, 'paraMoeda' e 'price' são parâmetros de consulta que são passados na URL e usados na função 'conversor'.
# Por exemplo, 'conversor/?paraMoeda=USD,EUR,GBP&price=8.88'
# @roteador.get('/conversor/{moeda}')
# def conversor(moeda: str, paraMoeda: str, preco: float):
#     return 'Funcinou!!'

# Rota SÍNCRONA
# Ele aceita três parâmetros: 'moeda', 'paraMoeda' e 'preco'
@roteador.get('/conversor/sync/{moeda}')
def syncConversor(moeda: str, paraMoeda: str, preco: float):
    """
    Rota para converter o preço de uma moeda para várias moedas de destino.

    Parâmetros:
    - moeda: str -> A moeda de origem.
    - paraMoeda: str -> As moedas de destino separadas por vírgulas.
    - preco: float -> O preço a ser convertido.

    Retorna:
    - dict: Um dicionário com o nome de cada moeda de destino e o preço convertido correspondente.
    """
    # Separa as moedas de destino em uma lista
    paraMoeda = paraMoeda.split(',')

    # Dicionário para armazenar os resultados da conversão
    resultados = {}

    for cadaMoeda in paraMoeda:
        # Chama a função conversorSync para converter o preço para cada moeda de destino
        resposta = conversorSync(moeda=moeda, paraMoeda=cadaMoeda, preco=preco)
        # Armazena o resultado no dicionário
        resultados[cadaMoeda] = resposta

    # Retorna o dicionário com os resultados da conversão
    return resultados

@roteador.get('/conversor/async/{moeda}')
# Validação de Path e Query
async def asyncConversor(moeda: str = Path(tamMax = 3, regex = '^[A-Z]{3}$'), paraMoeda: str = Query(regex = '^[A-Z]{3}(,[A-Z{3}])*$'), preco: float = Query(gt=0)):
    """
    Esta é uma função assíncrona chamada asyncConversor que aceita três parâmetros.

    Parâmetros:
    - moeda: str -> Este parâmetro representa a moeda de origem. Ele deve ser uma string de exatamente 3 letras maiúsculas.
                     Isso é garantido usando o argumento `regex` que define uma expressão regular para validar a entrada.
                     Além disso, o tamanho máximo da string é definido como 3 usando `tamMax`.

    - paraMoeda: str -> Este parâmetro representa as moedas de destino. Deve ser uma ou mais strings de 3 letras maiúsculas,
                         separadas por vírgulas. O argumento `regex` é usado para validar a entrada.

    - preco: float -> Este parâmetro representa o preço a ser convertido. Deve ser um número flutuante maior que zero,
                      conforme garantido pelo argumento `gt` (greater than) no Query, que estabelece esta condição de validação.

    Retorna:
    - dict: Um dicionário com o nome de cada moeda de destino e o preço convertido correspondente.
    """

    # Separa as moedas de destino em uma lista
    paraMoeda = paraMoeda.split(',')

    # Dicionário para armazenar os resultados da conversão
    resultados = {}

    # Array para armazenar as corotinas
    corotinas = []

    for cadaMoeda in paraMoeda:
        # Chama a função conversorAsync para converter o preço para cada moeda de destino
        corotina = conversorAsync(moeda=moeda, paraMoeda=cadaMoeda, preco=preco)
        corotinas.append(corotina)

    # Executa todas as corotinas simultaneamente
    respostas = await gather(*corotinas)

    for cadaMoeda, resposta in zip(paraMoeda, respostas):
        # Armazena o resultado no dicionário
        resultados[cadaMoeda] = resposta

    # Retorna o dicionário com os resultados da conversão
    return resultados
