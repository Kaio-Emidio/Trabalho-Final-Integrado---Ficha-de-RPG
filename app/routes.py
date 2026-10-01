from app import app
from flask import render_template, redirect, flash, request
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/FichaPersonagem")
def ficha_personagem():
    return "Aqui será a página onde fica a criação da ficha"

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    return render_template(
        "login.html",
        form=form
    )

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    form = CadastroForm()

    return render_template(
        "cadastro.html",
        form=form
    )
