from app.models.models import Usuario
from app.database.database import SessionLocal

class UsuarioService:
    session = SessionLocal()

    @classmethod
    def create(cls, data):
        usuario_existente = cls.session.query(Usuario).filter_by(email=data["email"]).first()
        
        if usuario_existente:
            return {"erro": "Email já cadastrado"}

        usuario = Usuario(**data)
        cls.session.add(usuario)
        cls.session.commit()

        return {"mensagem": "Usuário criado com sucesso!"}

    @classmethod
    def find_all(cls):
        usuarios = cls.session.query(Usuario).all()
        return [u.to_dict() for u in usuarios]

    @classmethod
    def find_by_id(cls, usuario_id):
        usuario = cls.session.query(Usuario).get(usuario_id)

        if not usuario:
            return {"erro": "Usuário não encontrado"}

        return usuario.to_dict()

    @classmethod
    def delete(cls, usuario_id):
        usuario = cls.session.query(Usuario).get(usuario_id)

        if not usuario:
            return {"erro": "Usuário não encontrado"}

        cls.session.delete(usuario)
        cls.session.commit()

        return {"mensagem": "Usuário deletado com sucesso"}

    @classmethod
    def login(cls, email, senha):
        usuario = cls.session.query(Usuario).filter_by(email=email).first()

        if not usuario or usuario.senha != senha:
            return {"erro": "Email ou senha inválidos"}

        return {
            "mensagem": "Login realizado com sucesso",
            "usuario": usuario.to_dict()
        }