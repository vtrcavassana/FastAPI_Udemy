# time é uma biblioteca para lidar com o tempo
from time import sleep

# Definindo uma classe chamada SyncBob
class SyncBob():
    # Método para "tostar", onde um delay de 10 segundos é adicionado
    # para simular o tempo necessário para tostar
    def tostar(self):
        sleep(10)
    
    # Método para "assar um hambúrguer", onde um delay de 5 segundos é adicionado
    # para simular o tempo necessário para assar o hambúrguer
    def assarHambugo(self):
        sleep(5)
    
    # Método para "fazer um lanche", que combina os métodos anteriores
    # Primeiro, o método "tostar" é chamado e, depois, o método "assar um hambúrguer"
    def fazerLanche(self):
        self.tostar()
        self.assarHambugo()

# Criação de uma instância da classe SyncBob
syncBob = SyncBob()
# Chamando o método "fazerLanche" na instância de SyncBob
syncBob.fazerLanche()
# time python comparacaoSyncAsync.py


import asyncio

# Definindo a classe AsyncBob
class AsyncBob:
    # Definindo o método tostar. A palavra-chave async indica que este é um método assíncrono,
    # o que significa que ele pode ser pausado e retomado.
    async def tostar(self):
        # asyncio.sleep é uma função que "dorme" por um certo número de segundos,
        # mas ao contrário de time.sleep, não bloqueia todo o programa.
        # O await significa que a execução da corotina será pausada até que asyncio.sleep termine.
        await asyncio.sleep(10)

    # Da mesma forma, assarHambugo é um método assíncrono que dorme por 5 segundos.
    async def assarHambugo(self):
        await asyncio.sleep(5)

    # fazerLanche é outro método assíncrono.
    async def fazerLanche(self):
        # asyncio.gather é uma função que recebe várias corotinas e retorna uma única corotina que executa todas elas em paralelo.
        # Então, tostar e assarHambugo serão executados ao mesmo tempo, não sequencialmente.
        await asyncio.gather(self.tostar(), self.assarHambugo())

# Definindo a função main como uma corotina assíncrona.
async def main():
    # Criando uma instância da classe AsyncBob.
    asyncBob = AsyncBob()
    # Chamando o método fazerLanche da instância. Por ser uma corotina, precisa ser chamada com await.
    await asyncBob.fazerLanche()

# asyncio.run é a maneira recomendada de executar a tarefa principal para programas assíncronos.
# Ele inicia o loop de eventos, executa a corotina passada e fecha o loop de eventos.
asyncio.run(main())