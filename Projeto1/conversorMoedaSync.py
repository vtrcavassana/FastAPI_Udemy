# Importando as bibliotecas necessárias para este arquivo
import requests
from os import getenv
from fastapi import HTTPException

# APIKEY é definido usando uma variável de ambiente chamada 'ALPHAVANTAGE_APIKEY'
APIKEY = getenv('ALPHAVANTAGE_APIKEY')

# Esta função é responsável pela conversão de moedas
def conversorSync(moeda: str, paraMoeda: str, preco: str):
    """
    Função para converter o preço de uma moeda para outra usando uma API externa.

    Parâmetros:
    - moeda: str -> A moeda de origem.
    - paraMoeda: str -> A moeda de destino.
    - preco: str -> O preço a ser convertido.

    Retorna:
    - float: O preço convertido.
    """

    # A urlAPI é construída usando a chave API, a moeda de origem e a moeda de destino
    urlAPI = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moeda}&to_currency={paraMoeda}&apikey={APIKEY}'

    # Um pedido GET é enviado para a API. Se ocorrer algum erro, uma exceção é lançada
    try:
        resposta = requests.get(url=urlAPI)
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f'Deu esse erro: {erro}')
    
    # Os dados recebidos são convertidos para JSON
    dadosDaAPI = resposta.json()

    # Se a chave 'Realtime Currency Exchange Rate' não estiver presente nos dados, uma exceção é lançada
    if 'Realtime Currency Exchange Rate' not in dadosDaAPI:
        raise HTTPException(status_code=400, detail=f'Moeda {paraMoeda} não existe!')
    
    # O preço de câmbio é extraído dos dados
    precoCambio = float(dadosDaAPI['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    # O preço é então convertido usando o preço de câmbio
    precoConvertido = preco * precoCambio

    # Finalmente, o preço convertido é retornado
    return precoConvertido