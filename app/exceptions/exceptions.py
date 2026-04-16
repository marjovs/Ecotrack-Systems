class ValueErrorConsumo(Exception):
    def __init__(self, consumo):
        super().__init__(f"O consumo {consumo} não pode ser negativo.")


class ValueErrorMeta(Exception):
    def __init__(self, meta):
        super().__init__(f"A meta {meta} deve ser maior que zero.")