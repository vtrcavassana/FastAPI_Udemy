# Importa a classe BaseModel do módulo pydantic. BaseModel é a classe base para todos os modelos Pydantic.
# Importa também Field e validator do módulo pydantic. Field é usado para definir metadados para campos do modelo e para adicionar validação.
# O decorator validator é usado para adicionar uma função de validação personalizada a um campo do modelo.
from pydantic import BaseModel, Field, validator 

# Importa List do módulo typing. Isso é usado para especificar um tipo de lista para a anotação de tipo.
from typing import List 

# Importa o módulo re. Este módulo fornece operações de correspondência de expressões regulares.
import re 

"""
Esta é uma string de documentação que fornece um exemplo de como os dados de entrada devem parecer.
{
    "paraMoedas": ['USD', 'GBP']
    "preco": 123
}
"""

# Define uma classe de modelo Pydantic para os dados de entrada.
class converterInput(BaseModel): 
    # Define um campo para as moedas para as quais a conversão deve ser realizada. Isso deve ser uma lista de strings.
    paraMoeda: List[str] 
    # Define um campo para o preço que deve ser maior que zero.
    preco: float = Field(gt=0) 

    # Define um validador para o campo paraMoeda. Isso é uma função que será chamada quando um valor for atribuído a paraMoeda.
    @validator('paraMoeda') 
    def validarParaMoeda(cls, valor): 
        # Para cada moeda na lista de moedas
        for moeda in valor: 
            # Se a moeda não corresponder ao padrão de expressão regular
            if not re.match('^[A-Z]{3}$', moeda): 
                # Levanta uma exceção com uma mensagem de erro
                raise ValueError(f'Moeda inválida {moeda}') 
        # Se todas as moedas forem válidas, retorna a lista de moedas
        return valor 

# Define uma classe de modelo Pydantic para os dados de saída.
class converterOutput(BaseModel): 
    # Define um campo para uma mensagem de status.
    mensagem: str 
    # Define um campo para os dados de saída. Isso deve ser uma lista de dicionários.
    dado: List[dict] 
