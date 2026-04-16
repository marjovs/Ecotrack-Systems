from app.models.models import *
from app.database.database import SessionLocal
from app.validations.validations import validar_meta

class SetorService:
    session = SessionLocal()

    @classmethod
    def create(cls, data):
        validar_meta(data["meta_sustentavel"])

        setor = Setor(**data)
        cls.session.add(setor)
        cls.session.commit()

        return "Setor cadastrado com sucesso!"
    
    @classmethod
    def relatorio_geral(cls):
        consumos = cls.session.query(Consumo).all() 

        result = []

        for c in consumos:
            setor = cls.session.query(Setor).where(Setor.id == c.setor_id).one()

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
    def find_all(cls):
        setores = cls.session.query(Setor).all()
        return [s.to_dict() for s in setores]

    @classmethod
    def find_by_id(cls, id):
        return cls.session.query(Setor).where(Setor.id == id).one()