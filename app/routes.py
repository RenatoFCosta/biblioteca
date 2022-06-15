from crypt import methods
from app import app
from flask import render_template, request

user = {'nome': 'Renato Ferreira da Costa',
        'cpf':'219.013.093-04',
        'email':'renatofcosta@yahoo.com.br'}

@app.route('/')
@app.route('/index', defaults={'nome':'convidado'})
@app.route('/index/<nome>')
def index(nome):
    return render_template('index.html',nome='convidado')

@app.route('/contato')
def contato():
    return render_template('contato.html',usuario=user)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/autenticar', methods=['POST'])    
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    return f'Usuário: {usuario} | Senha: {senha}'