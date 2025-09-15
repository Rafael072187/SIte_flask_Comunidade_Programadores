from ComunidadeProgramadores import app, database
from ComunidadeProgramadores.models import Usuario

def criar_banco():
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Banco de dados criado com sucesso em ComunidadeImpressionadora/comunidade.db")

if __name__ == "__main__":
    criar_banco()

