from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administracao_redes_locais')
def administracao_redes_locais():
    return render_template('administracao_redes_locais.html')

@app.route('/processamento_computacional')
def processamento_computacional():
    return render_template('processamento_computacional.html')


if __name__ == '__main__':
    app.run(debug=True)