from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.setor_controller import setor_bp
    from app.controllers.consumo_controller import consumo_bp
    from app.controllers.usuario_controller import usuario_bp

    app.register_blueprint(setor_bp)
    app.register_blueprint(consumo_bp)
    app.register_blueprint(usuario_bp)

    return app