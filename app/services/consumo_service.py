from app.models.models import Consumo, Setor
from app.database.database import SessionLocal
from app.validations.validations import validar_consumo

class ConsumoService:
    session = SessionLocal()

    @classmethod
    def create(cls, data):
        validar_consumo(data["consumo_mensal"])

        consumo = Consumo(**data)
        cls.session.add(consumo)
        cls.session.commit()

        return "Consumo registrado com sucesso!"

    @classmethod
    def find_all(cls):
        consumos = cls.session.query(Consumo).all()

        result = []
        for c in consumos:
            setor = cls.session.query(Setor).get(c.setor_id)

            status = "Dentro da meta"
            if c.consumo_mensal > setor.meta_sustentavel:
                status = "Acima da meta"

            result.append({
                "setor": setor.nome,
                "consumo": c.consumo_mensal,
                "meta": setor.meta_sustentavel,
                "status": status
            })

        return result

    @classmethod
    def relatorio_geral(cls):
        return cls.find_all()

    @classmethod
    def acima_meta(cls):
        consumos = cls.session.query(Consumo).all()
        result = []

        for c in consumos:
            setor = cls.session.query(Setor).get(c.setor_id)

            if c.consumo_mensal > setor.meta_sustentavel:
                result.append({
                    "setor": setor.nome,
                    "consumo": c.consumo_mensal,
                    "meta": setor.meta_sustentavel
                })

        return result

    @classmethod
    def estatisticas(cls):
        consumos = cls.session.query(Consumo).all()

        total = sum(c.consumo_mensal for c in consumos)
        media = total / len(consumos) if consumos else 0

        return {
            "total": total,
            "media": media
        }