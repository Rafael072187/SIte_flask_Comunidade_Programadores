from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import inspect

app = Flask(__name__)

# Caminho do banco de dados
db_path = Path(__file__).parent / "comunidade.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

# Configurações extras
app.config['SECRET_KEY'] = '5191b9426848e06041f34ecbb8849d22'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert alert-info'

# Verificar se tabela existe e criar caso não exista
with app.app_context():
    engine = database.engine
    inspector = inspect(engine)
    if not inspector.has_table("usuario"):
        database.drop_all()
        database.create_all()
        print(f"Banco de dados criado com sucesso em {db_path}")
    else:
        print("Base de dados já existente")

# Importar rotas no final
from ComunidadeProgramadores import routes
