# Projeto 1 - Conversor de preços em FastAPI

Este projeto consiste em uma aplicação FastAPI que serve como um conversor de preços entre diferentes moedas. Ele utiliza a API do Alphavantage para obter taxas de câmbio em tempo real.

## Recursos utilizados

- **FastAPI:** Este é um framework moderno e rápido (alta performance) para construção de APIs com Python 3.6+ baseado nos padrões para APIs HTTP, como: OpenAPI (anteriormente conhecido como Swagger) e JSON Schema.
- **Alphavantage API:** Este serviço de API é usado para obter as taxas de câmbio atuais.

## Como executar o projeto

Execute o comando abaixo no terminal para iniciar o servidor:

`uvicorn main:app --reload`