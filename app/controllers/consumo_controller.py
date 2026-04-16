from flask import *
from app.services.consumo_service import ConsumoService
from datetime import datetime

consumo_bp = Blueprint('consumo', __name__, url_prefix='/consumos')

@consumo_bp.route('/', methods=['POST'])
def create_consumo():
    data = request.json
    result = ConsumoService.create(data)

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }), 201

@consumo_bp.route('/', methods=['GET'])
def get_consumos():
    return jsonify(ConsumoService.find_all())

@consumo_bp.route('/relatorio', methods=['GET'])
def relatorio():
    result = ConsumoService.relatorio_geral()

    return jsonify({
        "message": "Relatório geral de consumo",
        "data": result
    }), 200

@consumo_bp.route('/acima-meta', methods=['GET'])
def acima_meta():
    return jsonify(ConsumoService.acima_meta())

@consumo_bp.route('/estatisticas', methods=['GET'])
def estatisticas():
    return jsonify(ConsumoService.estatisticas())