import asyncio

async def soma(a,b):
    return a+b

# Criamos um outra função assíncrona 'exibeSoma'
# Funções assíncronas, SÓ PODEM EXECUTAR outras funções assíncronas
async def exibeSoma(a,b):
    # 'await' - indica que a função que será executada é assíncrona
    resultado = await soma(a,b)
    return resultado

# Criamos um 'Event Loop'
eventLoop = asyncio.new_event_loop()

# Atribuímos a variável 'resultado2' o resultado da função assíncrona 'exibeSoma'
# que dentro dela executa outra função assíncrona 'soma'
resultado2 = eventLoop.run_until_complete(exibeSoma(2,3))
print(f'SOMA = {resultado2}')