from flask import *
from app.services.setor_service import *
from sqlalchemy.exc import *
from flask_jwt_extended import *
from datetime import datetime

setor_bp = Blueprint('setor', __name__, url_prefix='/setores')

@setor_bp.route('/', methods=['POST'])
def create_setor():
    try:
        data = request.json

        if not data or not data.get('nome'):
            return jsonify({'error': 'O campo "nome" é obrigatório.'}), 400

        result = SetorService.create(data)

        return jsonify({
            "message": result,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }), 201

    except Exception:
        return jsonify({'error': 'Erro ao criar setor.'}), 500

@setor_bp.route('/', methods=['GET'])
def get_setores():
    try:
        result = SetorService.find_all()
        return jsonify(result), 200

    except Exception:
        return jsonify({'error': 'Erro ao buscar setores.'}), 500