import os
import psycopg2

from crypt import methods
from app import app
from flask import render_template, url_for, request, redirect, flash

user = {'nome': 'Renato Ferreira da Costa',
        'cpf':'219.013.093-04',
        'email':'renatofcosta@yahoo.com.br'}
app.secret_key = 'kJMOUD(*#@JDOIJ@D #@*JD@#J_@#JD)J@P'
# conn = None
# cur = None        

def get_db_connection():
    conn = psycopg2.connect(host='192.168.100.5',
                            database='cefa',
                            user='renato',  #os.environ['DB_USERNAME']
                            password='msemd'  ) #os.environ['DB_PASSWORD']
    if conn:
        return conn
    else:
        print('Erro na conexão com o Banco de Dados')
        return None

def conectar():
    conn = get_db_connection()
    return conn


def desconectar(conn):
    conn.close()  


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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

@app.route('/consultarlivros', methods=['GET', 'POST'])    
def consultarlivros():
    campo = request.form.get('campo')
    texto = request.form.get('texto')
    if texto:
        print('Valores vindos do formulário:')
        print('Campo:', campo)
        print('texto:', texto)
        dados = (campo,texto)
        print(dados[0])
        print(dados[1])
        conn = conectar()
        cur = conn.cursor()
        cur.execute('SELECT * FROM livros;')
        livros = cur.fetchall()
        cur.close()
        desconectar(conn)
        print(livros)
    else:
        print('Carregando formulário pela primeira vez...')
        livros = None
        dados = None
    return render_template('consultarlivros.html', livros=livros, dados=dados)