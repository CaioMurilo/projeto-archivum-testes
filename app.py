from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import api

def create_app():
    app = Flask(__name__, static_folder='.')
    CORS(app)
    
    # Prepara o banco de dados
    init_db()
    
    # Registra o CRUD no servidor
    app.register_blueprint(api)
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("Servidor Archivum rodando em http://localhost:3000")
    app.run(port=3000, debug=True)