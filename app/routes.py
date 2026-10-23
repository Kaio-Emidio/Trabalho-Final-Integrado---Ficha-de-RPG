from app import app, db
from flask import render_template, redirect, flash, request, url_for, abort
from flask_login import current_user
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm
from app.forms.admin_usuario_form import AdminUsuarioForm
from app.forms.modal_perfil_form import ModalPerfilForm
from app.services.UsuarioService import UsuarioService
from app.services.AuthenticationService import AuthenticationService
from app.models.usuario import Usuario
from sqlalchemy.exc import SQLAlchemyError

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
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('home')
            return redirect(next_page)
    return render_template('login.html', title='Login', form=formulario)


@app.route('/logout')
def logout():
    success = AuthenticationService.logout()
    if not success:
        flash("Erro ao efetuar logout!", category = "error")
    return redirect(url_for('home'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formulario = CadastroForm()
    if formulario.validate_on_submit():
        sucesso = UsuarioService.salvar(formulario)
        if sucesso:
            return redirect(url_for('login'))
        else:
            flash("Erro ao cadastrar o novo usuário!", category = "error")
            return render_template("cadastro.html", form=formulario)
    return render_template("cadastro.html", form=formulario, title="Cadastro de Usuário")


@app.route("/admin")
def admin():
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)
    else:
        usuarios = UsuarioService.listar().all()
        return render_template("admin.html",
                               title="Administração",
                               usuarios=usuarios)


@app.route("/admin/usuarios/<int:usuario_id>/editar", methods=["GET", "POST"])
def admin_editar_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)

    formulario = AdminUsuarioForm(usuario.id, obj=usuario)
    if formulario.validate_on_submit():
        usuario.username = formulario.username.data.strip()
        usuario.email = formulario.email.data.strip().lower()
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            app.logger.exception("Erro ao atualizar usuário %s", usuario.id)
            flash("Não foi possível atualizar o usuário.", "error")
        else:
            flash("Usuário atualizado com sucesso.", "success")
            return redirect(url_for('admin'))

    return render_template("admin_editar_usuario.html",
                           title="Editar usuário",
                           formulario=formulario,
                           usuario=usuario)


@app.route("/admin/usuarios/<int:usuario_id>/excluir", methods=["POST"])
def admin_excluir_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)
    if usuario.id == current_user.id:
        flash("Você não pode excluir a própria conta de administrador.", "error")
        return redirect(url_for('admin'))
    if usuario.personagens:
        flash("Não é possível excluir este usuário enquanto ele tiver personagens vinculados.",
              "error")
        return redirect(url_for('admin'))

    try:
        sucesso = UsuarioService.remover(usuario)
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao excluir usuário %s", usuario.id)
        flash("Não foi possível excluir o usuário.", "error")
    else:
        if sucesso:
            flash("Usuário excluído com sucesso.", "success")
        else:
            flash("Não foi possível excluir o usuário.", "error")
    return redirect(url_for('admin'))


@app.route("/admin/usuarios/<int:usuario_id>/promover", methods=["POST"])
def admin_promover_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)
    if usuario.role != Usuario.ROLES['USER']:
        flash("Este usuário não possui perfil padrão.", "error")
        return redirect(url_for('admin'))

    usuario.role = Usuario.ROLES['ADM']
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao promover usuário %s", usuario.id)
        flash("Não foi possível promover o usuário.", "error")
    else:
        flash("Usuário promovido a administrador com sucesso.", "success")
    return redirect(url_for('admin'))


@app.errorhandler(403)
def erro_403(e):
    return render_template('403.html'), 403