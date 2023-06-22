# O módulo 'decouple' ajuda a separar as configurações de instância de seus códigos de projeto.
# A função 'config' lê a variável de ambiente ou um arquivo .env para obter o valor da configuração.
from decouple import config

# SQLAlchemy fornece uma API de alto nível para se conectar e fazer consultas em bancos de dados SQL.
# 'create_engine' é uma função do SQLAlchemy que permite criar uma instância de engine a partir de uma URL.
from sqlalchemy import create_engine

# sessionmaker é uma factory que produz classes de sessão vinculadas a um engine.
from sqlalchemy.orm import sessionmaker

# Usamos a função 'config' para ler a URL do banco de dados do nosso arquivo de configuração ou variável de ambiente.
dbURL = config('DB_URL')

# Usamos 'create_engine' para criar um engine que proporciona uma fonte de conectividade ao nosso banco de dados.
# A opção 'pool_pre_ping=True' é usada para testar a conexão com o banco de dados antes de cada conexão ser usada.
# Isso é útil para lidar com o problema comum dos bancos de dados encerrarem conexões inativas.
engine = create_engine(dbURL, pool_pre_ping=True)

# Aqui, chamamos 'sessionmaker()' sem argumentos para criar uma classe de sessão não vinculada.
# Ainda precisamos fornecer uma instância de 'engine' para criar uma sessão real.
Sessao = sessionmaker()
