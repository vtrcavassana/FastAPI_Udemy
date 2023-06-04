# 'asyncio' é uma biblioteca Python para lidar com assincronismo
import asyncio

# Criamos a função assíncrona 'soma'
# assíncronismo permite que diversas tarefas possam ser inciadas e gerenciadas
# ao mesmo tempo, é criada uma fila de execuções e ela será executada
# de forma que caso algum função demore pra ser finalizada, um outra mais rápida
# entrará em seu lugar pra ser executada, enquanto espera a anterior ser finalizada
async def soma(a,b):
    return a+b

# Como a variável que recebe a resposta da função assíncrona não está
# num 'Event Loop', ela ficará 'esperando' pra ser processada
resultado = soma(2,3)
print(resultado)

# Usando 'Event Loop' a mesma função assíncrona será atribuída a um evento
# que ficará executando ela até ser totalmente resolvida
eventLoop = asyncio.new_event_loop()
resultado2 = eventLoop.run_until_complete(resultado)
print(f'SOMA = {resultado2}')