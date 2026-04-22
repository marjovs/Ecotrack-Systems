from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

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

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="setores")
    consumos = relationship("Consumo", back_populates="setor")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "meta_sustentavel": self.meta_sustentavel,
            "usuario_id": self.usuario_id
        }

class Consumo(Base):
    __tablename__ = "consumos"

    id = Column(Integer, primary_key=True)

    setor_id = Column(Integer, ForeignKey("setores.id"), nullable=False)

    consumo_mensal = Column(Float, nullable=False)

    data = Column(Date, nullable=False)

    setor = relationship("Setor", back_populates="consumos")

    def to_dict(self):
        return {
            "id": self.id,
            "setor_id": self.setor_id,
            "consumo_mensal": self.consumo_mensal,
            "data": self.data.isoformat() if self.data else None
        }