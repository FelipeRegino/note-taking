"""Note Taking.

Aplicação para criar anotações
"""


def create_app():
    """Função de configuração inicial da aplicação."""
    from flask import Flask
    from .view.note import MOD_NOTE
    from api.database import DB_SESSION

    app = Flask(__name__)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """Função para desligar a conexão com o banco de dados."""
        DB_SESSION.remove()

    app.register_blueprint(MOD_NOTE)

    return app
