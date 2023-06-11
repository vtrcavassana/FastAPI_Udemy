# Importa as bibliotecas necessárias
from os import getenv
from fastapi import HTTPException
import httpx

# Recupera a chave de API do ambiente
APIKEY = getenv('ALPHAVANTAGE_APIKEY')

# Define a função assíncrona de conversão de moedas
async def conversorAsync(moeda: str, paraMoeda: str, preco: float):
    # Constrói a URL para a API de conversão de moedas
    urlAPI = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moeda}&to_currency={paraMoeda}&apikey={APIKEY}'

    try:
        # Cria uma sessão assíncrona e obtém a resposta da API
        async with httpx.AsyncClient() as sessao:
            resposta = await sessao.get(url=urlAPI)
            dadosDaAPI = resposta.json()
    except Exception as erro:
        # Se houver um erro durante a chamada à API, gera uma exceção
        raise HTTPException(status_code=400, detail=f'Deu esse erro: {erro}')
    
    # Verifica se a resposta da API contém a chave 'Realtime Currency Exchange Rate'
    if 'Realtime Currency Exchange Rate' not in dadosDaAPI:
        raise HTTPException(status_code=400, detail=f'Não existe parâmetro')
    
    # Obtém a taxa de câmbio atual da resposta da API
    precoCambio = float(dadosDaAPI['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    # Calcula o preço convertido usando a taxa de câmbio
    precoConvertido = preco * precoCambio

    # Retorna o preço convertido
    return precoConvertido
