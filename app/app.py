from flask import Flask
from flask_restful import Api

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path para importações.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.routes import configure_routes

app = Flask(__name__)
api = Api(app)

configure_routes(api)

if __name__ == '__main__':
    app.run(debug=True, port=5000)