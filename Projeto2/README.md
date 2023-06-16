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