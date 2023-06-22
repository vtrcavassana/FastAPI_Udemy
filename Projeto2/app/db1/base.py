# Importamos a função 'declarative_base' do módulo 'sqlalchemy.orm'.
# Esta função é usada para criar uma nova base declarativa: uma classe abstrata na qual nossos modelos de banco de dados serão baseados.
from sqlalchemy.orm import declarative_base

# Criamos a classe base chamada 'Base' usando a função 'declarative_base()'.
# Todos os modelos do banco de dados que criarmos a partir de agora devem herdar desta classe 'Base'.
# Isso permite que o SQLAlchemy saiba que eles são modelos e automaticamente mapeie as colunas nos nossos modelos para as colunas nas tabelas do banco de dados.
Base = declarative_base()