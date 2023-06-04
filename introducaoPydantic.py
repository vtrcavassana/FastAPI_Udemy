from pydantic import BaseModel, validator

# Criando o modelo que deve ser criado
# quando inserir um novo Usuário
class Usuario(BaseModel):
    # Cada variável tem seu próprio TIPO (para validação)
    nome: str
    idade: int
    email: str

    # '@decorador' - Decorator é usado para criar funções personalizadas
    # Nesse caso '@validator' verifica o 'email' do usuário
    @validator('email')
    # 'cls' - É a classe que será recebida pela função
    # 'valor' - Le o valor que está na variável 'email'
    def validarEmail(cls, valor):
        if '@' not in valor:
            raise ValueError('Email Inválido')
        return valor

# Todos os campos estão inseridos de forma correta, BaseModel + validator respeitado - EXIBE
usuario1 = Usuario(nome = 'Vitu', idade = 30, email = 'vitu@email.com')
print(usuario1)

# Campo 'email' não possui '@', BaseModel foi respeitado, mas o validator não - EXIBE ERRO
usuario2 = Usuario(nome = 'Virtu', idade = 30, email = 'virtu@email.com')
print(usuario2)

# Campo 'idade' possui uma string, por mais que o validator foi respeitado, BaseModel não - EXIBE ERRO
usuario3 = Usuario(nome = 'Vitoca', idade = 'i', email = 'vitoca@email.com')
print(usuario3)