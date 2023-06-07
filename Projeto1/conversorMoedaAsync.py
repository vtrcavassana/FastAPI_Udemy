import requests
from os import getenv
from fastapi import HTTPException
import asyncio
import httpx

APIKEY = getenv('ALPHAVANTAGE_APIKEY')

async def conversorAsync(moeda: str, paraMoeda: str, preco: float):
    urlAPI = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moeda}&to_currency={paraMoeda}&apikey={APIKEY}'

    try:
        async with httpx.AsyncClient() as sessao:
            resposta = await sessao.get(url=urlAPI)
            dadosDaAPI = resposta.json()
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f'Deu esse erro: {erro}')
    
    if 'Realtime Currency Exchange Rate' not in dadosDaAPI:
        raise HTTPException(status_code=400, detail=f'Deu esse erro aqui: {erro}')
    
    precoCambio = float(dadosDaAPI['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    precoConvertido = preco * precoCambio

    return precoConvertido