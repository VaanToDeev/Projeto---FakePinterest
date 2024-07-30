from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, length
from wtforms import ValidationError
from fakepin.models import Usuario

class formLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class formCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), length(6, 20)])
    confirmar_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    submit = SubmitField("Criar Conta")

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if Usuario:
            raise ValidationError("E-mail ja cadastrado. Faça o login. ")

