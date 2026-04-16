from flask import *
from app.services.usuario_service import UsuarioService
from datetime import datetime

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')


@usuario_bp.route('/', methods=['POST'])
def create_usuario():
    data = request.json
    result = UsuarioService.create(data)

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }), 201


@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    return jsonify(UsuarioService.find_all())


@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario_by_id(usuario_id):
    result = UsuarioService.find_by_id(usuario_id)

    return jsonify(result)


@usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    result = UsuarioService.delete(usuario_id)

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })


@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    result = UsuarioService.login(
        data.get("email"),
        data.get("senha")
    )

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })