from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    setores = relationship("Setor", back_populates="usuario")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }

class Setor(Base):
    __tablename__ = "setores"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    meta_sustentavel = Column(Float, nullable=False)

    consumos = relationship("Consumo", back_populates="setor")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "meta_sustentavel": self.meta_sustentavel
        }


class Consumo(Base):
    __tablename__ = "consumos"

    id = Column(Integer, primary_key=True)
    setor_id = Column(Integer, ForeignKey("setores.id"))
    consumo_mensal = Column(Float, nullable=False)
    data = Column(String, nullable=False)

    setor = relationship("Setor", back_populates="consumos")

    def to_dict(self):
        return {
            "id": self.id,
            "setor_id": self.setor_id,
            "consumo_mensal": self.consumo_mensal,
            "data": self.data
        }