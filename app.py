from flask import Flask, render_template, flash, redirect, url_for  # Importar flash, redirect e url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Configuração inicial do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'  # Defina uma chave secreta forte aqui

# Criar um formulário usando Flask-WTF
class MeuFormulario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota para módulos
@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

# Rota para segurança, onde vamos exibir o formulário
@app.route('/seguranca', methods=['GET', 'POST'])
def seguranca():
    form = MeuFormulario()
    if form.validate_on_submit():  # Verifica se o formulário foi submetido e validado
        nome = form.nome.data
        flash(f"Formulário enviado com sucesso por {nome}!", "success")
        return render_template('seguranca.html', form=form)
    elif form.is_submitted() and not form.validate():  # Se o formulário foi submetido mas não validado
        flash("Erro: Formulário não validado. Verifique os campos e tente novamente.", "error")

    return render_template('seguranca.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
