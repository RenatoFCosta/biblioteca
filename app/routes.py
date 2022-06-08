from app import app
from flask import render_template

user = {'nome': 'Renato Ferreira da Costa',
        'cpf':'219.013.093-04',
        'email':'renatofcosta@yahoo.com.br'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html', usuario=user)