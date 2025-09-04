from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired, Length


class RegistrationForm(FlaskForm):
    nome = StringField(
            label="Nome",
            validators=[InputRequired(message="É obrigatório informar um nome para cadastro"),
                        Length(max=60, message="O nome pode ter até 60 caracteres")])
    email = StringField(
            label="Email",
            validators=[InputRequired(message="É obrigatório informar um email para cadastro"),
                        Email(message="Informe um email válido"),
                        Length(max=180, message="O email pode ter até 180 caracteres")])
    password = PasswordField(
            label="Senha",
            validators=[InputRequired(message="É necessário escolher uma senha")])
    password2 = PasswordField(
            label="Confirme a senha",
            validators=[InputRequired(message="É necessário repetir a senha"),
                        EqualTo('password', message="As senhas não são iguais")])
    submit = SubmitField("Criar uma conta no sistema")
