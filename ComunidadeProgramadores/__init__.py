from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from ComunidadeProgramadores.models import Usuario
from ComunidadeProgramadores import app, database


app = Flask(__name__)


db_path = Path(__file__).parent / "comunidade.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"


app.config['SECRET_KEY'] = '5191b9426848e06041f34ecbb8849d22'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert alert-info'

engine = SQLAlchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = SQLAlchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Banco de dados criado com sucesso em ComunidadeImpressionadora/comunidade.db")
else:
    print("Base de dados já existente")



from ComunidadeProgramadores import routes