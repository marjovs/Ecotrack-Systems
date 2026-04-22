from flask import *
from app.services.consumo_service import *
from sqlalchemy.exc import *
from flask_jwt_extended import *
from datetime import datetime

consumo_bp = Blueprint('consumo', __name__, url_prefix='/consumos')

@consumo_bp.route('/', methods=['POST'])
@jwt_required()
def create_consumo():
    try:
        data = request.json
        user_id = get_jwt_identity()

        if not data:
            return jsonify({'error': 'Dados são obrigatórios.'}), 400

        result = ConsumoService.create(data, user_id)

        return jsonify({
            "message": result,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }), 201

    except Exception:
        return jsonify({'error': 'Erro ao registrar consumo.'}), 500

@consumo_bp.route('/', methods=['GET'])
@jwt_required()
def get_consumos():
    try:
        user_id = get_jwt_identity()
        result = ConsumoService.find_all(user_id)

        return jsonify(result), 200

    except Exception:
        return jsonify({'error': 'Erro ao buscar consumos.'}), 500

@consumo_bp.route('/relatorio', methods=['GET'])
@jwt_required()
def relatorio():
    try:
        user_id = get_jwt_identity()
        result = ConsumoService.relatorio_geral(user_id)

        return jsonify({
            "message": "Relatório geral de consumo",
            "data": result
        }), 200

    except Exception:
        return jsonify({'error': 'Erro ao gerar relatório.'}), 500

@consumo_bp.route('/acima-meta', methods=['GET'])
@jwt_required()
def acima_meta():
    try:
        user_id = get_jwt_identity()
        result = ConsumoService.acima_meta(user_id)

        return jsonify(result), 200

    except Exception:
        return jsonify({'error': 'Erro ao buscar dados.'}), 500

@consumo_bp.route('/estatisticas', methods=['GET'])
@jwt_required()
def estatisticas():
    try:
        user_id = get_jwt_identity()
        result = ConsumoService.estatisticas(user_id)

        return jsonify(result), 200

    except Exception:
        return jsonify({'error': 'Erro ao gerar estatísticas.'}), 500