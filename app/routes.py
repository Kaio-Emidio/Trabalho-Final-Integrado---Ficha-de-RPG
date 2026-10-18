from app import app
from flask import render_template, redirect, flash, request, url_for
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm
from app.forms.modal_perfil_form import ModalPerfilForm

@app.route("/")
def home():
    logado = True
    return render_template('index.html',
                           logado = logado)

@app.route("/ficha/<id>")
def ficha_personagem(id):
    modal_perfil = ModalPerfilForm()
    return render_template('ficha.html',
                           nome = 'Rogerinho',
                           modal_perfil = modal_perfil)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # Lógica de autenticação entraria aqui
        pass
        
    return render_template("login.html", 
                           form=form)

@app.route('/logout')
def logout():
    pass

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    
    if form.validate_on_submit():
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('login'))
        
        
    return render_template("cadastro.html", 
                           form=form)
