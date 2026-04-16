from flask import *
from app.services.setor_service import SetorService
from datetime import datetime

setor_bp = Blueprint('setor', __name__, url_prefix='/setores')

@setor_bp.route('/', methods=['POST'])
def create_setor():
    data = request.json
    result = SetorService.create(data)

    return jsonify({
        "message": result,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }), 201

@setor_bp.route('/', methods=['GET'])
def get_setores():
    return jsonify(SetorService.find_all())