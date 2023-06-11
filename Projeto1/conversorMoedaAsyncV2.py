# Importa a função getenv do módulo os. getenv é usado para obter variáveis de ambiente do sistema.
from os import getenv 

# Importa a exceção HTTPException do módulo fastapi. HTTPException é uma exceção padrão que pode ser usada para retornar respostas HTTP.
from fastapi import HTTPException 

# Importa o módulo httpx. Este módulo é uma biblioteca HTTP/1.1 e HTTP/2 para Python.
import httpx 

# Obtém a chave da API do ambiente de execução
APIKEY = getenv('ALPHAVANTAGE_APIKEY') 

# Define uma função assíncrona chamada 'conversorAsyncV2'
async def conversorAsyncV2(moeda: str, paraMoeda: str, preco: float): 
    # Constrói a URL para o serviço de API que fornece as taxas de câmbio.
    urlAPI = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moeda}&to_currency={paraMoeda}&apikey={APIKEY}' 

    try: 
        # Cria um cliente assíncrono para fazer requisições HTTP
        async with httpx.AsyncClient() as sessao: 
            # Envia uma solicitação GET para a URL da API e aguarda a resposta.
            resposta = await sessao.get(url=urlAPI) 
            # Converte a resposta em formato JSON.
            dadosDaAPI = resposta.json() 
    except Exception as erro: 
        # Se houver algum erro durante a solicitação, ele será capturado e uma exceção HTTP será levantada.
        raise HTTPException(status_code=400, detail=f'Deu esse erro: {erro}') 

    try:
        # Tenta pegar a taxa de câmbio do JSON retornado e a converte para um número float.
        precoCambio = float(dadosDaAPI['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    except KeyError:
        # Se a chave 'Realtime Currency Exchange Rate' ou '5. Exchange Rate' não estiver presente, levanta uma exceção HTTP.
        raise HTTPException(status_code=400, detail='Chave não encontrada no JSON retornado pela API')

    # Calcula o preço convertido multiplicando o preço pela taxa de câmbio.
    precoConvertido = preco * precoCambio 

    # Retorna o preço convertido como um dicionário.
    return {paraMoeda: precoConvertido} 
