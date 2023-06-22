# 'sqlalchemy' fornece uma maneira de interagir com bancos de dados SQL e 'Column', 'Integer' e 'String' 
# são classes utilizadas para definir os tipos de dados e as colunas na tabela do banco de dados.
from sqlalchemy import Column, Integer, String

# Importamos a classe 'Base' do arquivo 'base.py' na pasta 'database'. 
# Esta classe é a base declarativa para todos os modelos do SQLAlchemy.
from app.db1.base import Base

# Definimos a classe 'Category', que herda de 'Base'. Esta classe representa uma tabela no banco de dados.
class Categoria(Base):
    # __tablename__ é um atributo especial que é usado pelo SQLAlchemy para saber o nome da tabela no banco de dados.
    __tablename__ = 'categorias'
    
    # Definimos as colunas da tabela. 
    # Cada atributo da classe representa uma coluna na tabela.
    # 'Column' é uma função que define as propriedades da coluna.
    # 'id' é a chave primária e é autoincrementável.
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    
    # 'name' é uma coluna que armazena strings e não pode ser nula.
    name = Column('nome', String, nullable=False)
    
    # 'slug' é uma coluna que armazena strings e não pode ser nula.
    slug = Column('slug', String, nullable=False)
