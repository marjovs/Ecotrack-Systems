from flask import *
from app.controllers.consumo_controller import consumo_bp
from app.controllers.setor_controller import setor_bp
from app.controllers.usuario_controller import usuario_bp
from flask_jwt_extended import JWTManager
from config import config
from datetime import timedelta

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(consumo_bp)
api_bp.register_blueprint(setor_bp)
api_bp.register_blueprint(usuario_bp)

jwt = JWTManager

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = config.secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)

    jwt.init_app(app)

    app.register_blueprint(api_bp)

    return app