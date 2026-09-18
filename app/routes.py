from app import app
from flask import render_template, redirect, flash, request

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/FichaPersonagem")
def ficha_personagem():
    return "Aqui será a página onde fica a criação da ficha"

@app.route("/login")
def login():
    return "Login efetuado"

@app.route("/cadastro")
def cadastro():
    return "Cadastro feito"