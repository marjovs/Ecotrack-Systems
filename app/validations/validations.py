from app.exceptions.exceptions import *

def validar_consumo(consumo: float):
    if consumo < 0:
        raise ValueErrorConsumo(consumo)


def validar_meta(meta: float):
    if meta <= 0:
        raise ValueErrorMeta(meta)