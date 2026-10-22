from app import app
from flask import render_template, redirect, flash, request, url_for, abort
from flask_login import current_user
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm
from app.forms.modal_perfil_form import ModalPerfilForm
from app.services.UsuarioService import UsuarioService
from app.services.AuthenticationService import AuthenticationService
from app.models.usuario import Usuario

@app.route("/")
def home():
    logado = current_user.is_authenticated
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
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationService.login(formulario):
            flash("Login efetuado com sucesso!", "success")
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('home')
            return redirect(next_page)
        else:
            flash("Usuário ou senha inválidos.", "error")
    return render_template('login.html', title='Login', form=formulario)


@app.route('/logout')
def logout():
    success = AuthenticationService.logout()
    if not success:
        flash('Erro ao realizar o logout', category='error')
    return redirect(url_for('home'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formulario = CadastroForm()
    if formulario.validate_on_submit():
        sucesso = UsuarioService.salvar(formulario)
        if sucesso:
            flash("Usuário cadastrado com sucesso!", category = "success")
            return redirect(url_for('login'))
        else:
            flash("Erro ao cadastrar o novo usuário!", category = "error")
            return render_template("cadastro.html", form=formulario)
    return render_template("cadastro.html", form=formulario, title="Cadastro de Usuário")


@app.route("/admin")
def admin():
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)
    else:
        return render_template("admin.html", title="Administração")