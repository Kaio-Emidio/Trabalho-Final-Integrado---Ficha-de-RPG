from app import app
from flask import render_template, redirect, flash, request
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm

@app.route("/")
def home():
    logado = False
    return render_template('index.html',
                           logado = logado)

@app.route("/ficha/<id>")
def ficha_personagem(id):
    return render_template('ficha.html',
                           nome = 'rogerinho')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", 
                           form=form)

@app.route('/logout')
def logout():
    pass

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    return render_template("cadastro.html", 
                           form=form)
