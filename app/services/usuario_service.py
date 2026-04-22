from app.models.models import *
from app.database.database import SessionaLocal
from werkzeug.security import *
from app.exceptions.exceptions import *


class UsuarioService:

    session = SessionaLocal()

    @classmethod
    def create(cls, usuario: dict) -> str:
       
        usuario['password'] = generate_password_hash(usuario.get('password'))
        n_usuario = Usuario(**usuario)
        cls.session.add(n_usuario)
        cls.session.commit()
        return "Usuário cadastrado com sucesso!"
    
    @classmethod
    def login(cls, username: str, password: str) -> bool:

        usuario = cls.session.query(Usuario).where(Usuario.username == username).first()
        if not usuario:
            raise UserNotFoundError(username)
        elif check_password_hash(usuario.password, password):
            return True
        return False

    @classmethod
    def find_all(cls):
        session = SessionaLocal()

        usuarios = session.query(Usuario).all()
        session.close()

        return [u.to_dict() for u in usuarios]

    @classmethod
    def find_by_id(cls, usuario_id):
        session = SessionaLocal()

        usuario = session.get(Usuario, usuario_id)
        session.close()

        if not usuario:
            return {"erro": "Usuário não encontrado"}

        return usuario.to_dict()

    @classmethod
    def delete(cls, usuario_id):
        session = SessionaLocal()

        usuario = session.get(Usuario, usuario_id)

        if not usuario:
            session.close()
            return {"erro": "Usuário não encontrado"}

        session.delete(usuario)
        session.commit()
        session.close()

        return {"mensagem": "Usuário deletado com sucesso"}