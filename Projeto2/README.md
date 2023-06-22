# Projeto 2

Este é o Projeto 2, um projeto que demonstra uma API básica usando FastAPI, PostgreSQL e Docker.

## Executando o Projeto

### Como rodar a aplicação localmente

Para rodar a aplicação localmente usando Uvicorn, você pode executar o seguinte comando no terminal:

```bash
uvicorn main:app --reload
```

### Usando Docker

Para executar todo o projeto usando Docker, você precisa ter o Docker e o Docker Compose instalados na sua máquina.

Você pode construir e executar todos os serviços usando o comando a seguir:

```sh
docker-compose up --build
```
## Serviços
Os seguintes serviços estão inclusos neste projeto:

### App
O serviço principal, que roda a aplicação FastAPI. O serviço pode ser acessado na porta 8000.

Para executar somente a aplicação:

```sh
docker-compose up app
```

### PostgreSQL
O banco de dados PostgreSQL. Este serviço pode ser acessado na porta 5432.

Para iniciar somente o serviço PostgreSQL:

```sh
docker-compose up postgres
```

### PgAdmin
O PgAdmin, uma interface gráfica para gerenciamento do PostgreSQL. Este serviço pode ser acessado na porta 5050.

Para iniciar somente o serviço PgAdmin:

```sh
docker-compose up pgadmin
```

### Executando migrações de banco de dados
Primeiro, você precisa inicializar o Alembic em seu projeto, se ainda não o fez. Isso irá criar o diretório de migrações do Alembic. Você pode fazer isso com o seguinte comando:

```sh
docker-compose run app sh -c 'alembic init migrations'
```

Isso garante que a pasta de migrações seja criada como "migrations", que é um nome comum para diretórios de migração de banco de dados em muitos frameworks e bibliotecas de ORM.

Para criar e aplicar migrações de banco de dados usando Alembic, você pode usar os seguintes comandos:

Esses comandos devem ser executados cada vez que você fizer uma mudança no seu modelo de banco de dados que necessite de uma migração.

Para gerar uma nova revisão de migração:

```sh
docker-compose run app sh -c 'alembic revision --autogenerate -m "sua mensagem de migração"'
```

Para aplicar as migrações ao banco de dados:

```sh
docker-compose run app sh -c 'alembic upgrade head'
```