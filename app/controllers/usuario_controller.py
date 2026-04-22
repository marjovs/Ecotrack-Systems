from flask import *
from app.services.usuario_service import *
from sqlalchemy.exc import *
from app.validations.validations import *
from flask_jwt_extended import *
from datetime import datetime

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')


@usuario_bp.route('/cadastro', methods=['POST'])
@jwt_required()
def create_usuario():
    try:
        usuario = request.json

        valid_password(usuario.get('password'))

        return jsonify({'message': UsuarioService.create(usuario)}), 201
    except PasswordLengthError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao cadastrar o usuário.'}), 500

@usuario_bp.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({'error': 'Username e senha são obrigatórios.'}), 400
        
        if UsuarioService.login(username, password):
            access_token = create_access_token(identity=username)
            return jsonify({'message': 'Login realizado com sucesso',
                            'access_token': access_token}), 200
        else:
            return jsonify({'error': 'Credenciais inválidas.'}), 401
    except UserNotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Ocorreu um erro ao realizar o login.'}), 500

@usuario_bp.route('/', methods=['GET'])
@jwt_required()
def get_usuarios():
    return jsonify(UsuarioService.find_all())


@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
@jwt_required()
def get_usuario_by_id(usuario_id):
    current_user = get_jwt_identity()

    if current_user != usuario_id:
        return jsonify({'error': 'Acesso negado'}), 403

    result = UsuarioService.find_by_id(usuario_id)

    if not result:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    return jsonify(result)


@usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])
@jwt_required()
def delete_usuario(usuario_id):
    current_user = get_jwt_identity()

    if current_user != usuario_id:
        return jsonify({'error': 'Acesso negado'}), 403

    result = UsuarioService.delete(usuario_id)

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })