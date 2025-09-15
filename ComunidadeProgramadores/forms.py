from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ComunidadeProgramadores.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usário', validators=[DataRequired(), Length(min=5, max=16)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=16)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario= Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=16)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    
    Curso_powerpoint = BooleanField('PowerPoint')
    Curso_excel = BooleanField('Excel')
    Curso_vba = BooleanField('VBA')
    Curso_powerbi = BooleanField('Power BI')
    Curso_python = BooleanField('Python')
    Curso_java = BooleanField('Java')
    Curso_javascript = BooleanField('JavaScript')
    Curso_html_css = BooleanField('HTML & CSS')
    Curso_sql = BooleanField('SQL')
    Curso_n8n = BooleanField('N8N')
    Curso_aws = BooleanField('AWS')
    Curso_ia = BooleanField('Inteligência Artificial')
    Curso_flutterflow = BooleanField('FlutterFlow')
    Curso_make = BooleanField('Make')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario= Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')
            

class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired()])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')