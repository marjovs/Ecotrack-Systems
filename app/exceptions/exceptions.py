class ValueErrorConsumo(Exception):
    def __init__(self, consumo):
        super().__init__(f"O consumo {consumo} não pode ser negativo.")

class ValueErrorMeta(Exception):
    def __init__(self, meta):
        super().__init__(f"A meta {meta} deve ser maior que zero.")

class UserNotFoundError(Exception):
    ''''Exceção representativa para usuário não encontrado'''
    def __init__(self, username):
        super().__init__(f'O usuário {username} não foi encontrado.')

class PasswordLengthError(Exception):
    def __init__(self, password):
        super().__init__(f'A senha {password} deve conter no mínimo 8 caracteres.')