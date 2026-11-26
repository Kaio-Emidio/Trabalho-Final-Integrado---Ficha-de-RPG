from app import app, db
from flask import render_template, redirect, flash, request, url_for, abort
from flask_login import current_user, login_required
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroForm
from app.forms.modals_ficha.modal_perfil_form import ModalPerfilForm
from app.forms.modals_ficha.modal_atributos_form import ModalAtributosForm
from app.forms.admin_usuario_form import AdminUsuarioForm
from app.forms.raca_form import RacaForm
from app.forms.classe_form import ClasseForm
from app.services.UsuarioService import UsuarioService
from app.services.AuthenticationService import AuthenticationService
from app.models.usuario import Usuario
from app.models.raca import Raca
from app.models.classe import Classe
from sqlalchemy.exc import SQLAlchemyError

@app.route("/")
def home():
    logado = current_user.is_authenticated
    adm = logado and current_user.role == Usuario.ROLES['ADM']
    return render_template('index.html',
                           logado = logado,
                           adm=adm)

@app.route("/racas")
def racas():
    logado = current_user.is_authenticated
    adm = logado and current_user.role == Usuario.ROLES['ADM']
    racas = Raca.query.order_by(Raca.nome).all()
    return render_template('racas.html',
                           logado = logado,
                           adm=adm,
                           racas=racas)


@app.route("/classes")
def classes():
    logado = current_user.is_authenticated
    adm = logado and current_user.role == Usuario.ROLES['ADM']

    classes = Classe.query.order_by(Classe.nome).all()

    return render_template('classe.html',
                           logado=logado,
                           adm=adm,
                           classes=classes)


@app.route("/classes/nova", methods=["GET", "POST"])
def admin_nova_classe():
    formulario = ClasseForm()
    if formulario.validate_on_submit():
        classe = Classe(
            nome=formulario.nome.data.strip(),
            vida_inicial=formulario.vida_inicial.data,
            vida_por_nivel=formulario.vida_por_nivel.data,
            dado_de_vida=formulario.dado_de_vida.data.strip()
        )
        db.session.add(classe)
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            app.logger.exception("Erro ao cadastrar classe")
            flash("Não foi possível cadastrar a classe.", "error")
        else:
            flash("Classe cadastrada com sucesso.", "success")
            return redirect(url_for('classes'))

    return render_template("wiki/classe_form.html",
                           title="Adicionar classe",
                           formulario=formulario,
                           acao="Adicionar classe")


@app.route("/admin/classes/<int:classe_id>/editar", methods=["GET", "POST"])
@login_required
def admin_editar_classe(classe_id):
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    classe = db.session.get(Classe, classe_id)
    if classe is None:
        abort(404)

    formulario = ClasseForm(classe_id=classe.id, obj=classe)
    if formulario.validate_on_submit():
        classe.nome = formulario.nome.data.strip()
        classe.vida_inicial = formulario.vida_inicial.data
        classe.vida_por_nivel = formulario.vida_por_nivel.data
        classe.dado_de_vida = formulario.dado_de_vida.data.strip()
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            app.logger.exception("Erro ao atualizar classe %s", classe.id)
            flash("Não foi possível atualizar a classe.", "error")
        else:
            flash("Classe atualizada com sucesso.", "success")
            return redirect(url_for('classes'))

    return render_template("wiki/classe_form.html",
                           title="Editar classe",
                           formulario=formulario,
                           acao="Salvar alterações",
                           classe=classe)


@app.route("/admin/classes/<int:classe_id>/excluir", methods=["POST"])
@login_required
def admin_excluir_classe(classe_id):
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    classe = db.session.get(Classe, classe_id)
    if classe is None:
        abort(404)
    if classe.personagens or classe.habilidades:
        flash("Não é possível excluir uma classe vinculada a personagens ou habilidades.",
              "error")
        return redirect(url_for('classes'))

    try:
        db.session.delete(classe)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao excluir classe %s", classe.id)
        flash("Não foi possível excluir a classe.", "error")
    else:
        flash("Classe excluída com sucesso.", "success")
    return redirect(url_for('classes'))


@app.route("/admin/racas/nova", methods=["GET", "POST"])
@login_required
def admin_nova_raca():
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    formulario = RacaForm()
    if formulario.validate_on_submit():
        raca = Raca(
            nome=formulario.nome.data.strip(),
            tipo_criatura=formulario.tipo_criatura.data.strip(),
            tamanho=formulario.tamanho.data.strip()
        )
        db.session.add(raca)
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            app.logger.exception("Erro ao cadastrar raça")
            flash("Não foi possível cadastrar a raça.", "error")
        else:
            flash("Raça cadastrada com sucesso.", "success")
            return redirect(url_for('racas'))

    return render_template("admin/raca_form.html",
                           title="Adicionar raça",
                           formulario=formulario,
                           acao="Adicionar raça")


@app.route("/admin/racas/<int:raca_id>/editar", methods=["GET", "POST"])
@login_required
def admin_editar_raca(raca_id):
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    raca = db.session.get(Raca, raca_id)
    if raca is None:
        abort(404)

    formulario = RacaForm(raca_id=raca.id, obj=raca)
    if formulario.validate_on_submit():
        raca.nome = formulario.nome.data.strip()
        raca.tipo_criatura = formulario.tipo_criatura.data.strip()
        raca.tamanho = formulario.tamanho.data.strip()
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            app.logger.exception("Erro ao atualizar raça %s", raca.id)
            flash("Não foi possível atualizar a raça.", "error")
        else:
            flash("Raça atualizada com sucesso.", "success")
            return redirect(url_for('racas'))

    return render_template("admin/raca_form.html",
                           title="Editar raça",
                           formulario=formulario,
                           acao="Salvar alterações",
                           raca=raca)


@app.route("/admin/racas/<int:raca_id>/excluir", methods=["POST"])
@login_required
def admin_excluir_raca(raca_id):
    if current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    raca = db.session.get(Raca, raca_id)
    if raca is None:
        abort(404)
    if raca.personagens or raca.habilidades:
        flash("Não é possível excluir uma raça vinculada a personagens ou habilidades.",
              "error")
        return redirect(url_for('racas'))

    try:
        db.session.delete(raca)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao excluir raça %s", raca.id)
        flash("Não foi possível excluir a raça.", "error")
    else:
        flash("Raça excluída com sucesso.", "success")
    return redirect(url_for('racas'))

@app.route("/ficha/<id>")
@login_required
def ficha_personagem(id):
    logado = current_user.is_authenticated
    modal_perfil = ModalPerfilForm()
    modal_atb = ModalAtributosForm()
    return render_template('ficha.html',
                           logado = logado,
                           nome = 'Rogerinho',
                           modal_perfil = modal_perfil,
                           modal_atb = modal_atb)

@app.route("/login", methods=["GET", "POST"])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationService.login(formulario):
            flash("Login efetuado com sucesso.", "success")
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('home')
            return redirect(next_page)
        flash("Usuário ou senha inválidos.", "error")
    elif request.method == "POST":
        flash("Não foi possível efetuar o login. Verifique os dados informados.", "error")
    return render_template('login.html', title='Login', form=formulario)


@app.route('/logout')
@login_required
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
            flash("Cadastro efetuado com sucesso. Faça login para continuar.", "success")
            return redirect(url_for('login'))
        else:
            flash("Erro ao cadastrar o novo usuário!", category = "error")
            return render_template("cadastro.html", form=formulario)
    if request.method == "POST":
        flash("Não foi possível concluir o cadastro. Verifique os dados informados.", "error")
    return render_template("cadastro.html", form=formulario, title="Cadastro de Usuário")


@app.route("/wiki")
@login_required
def wiki():
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)
    else:
        usuarios = UsuarioService.listar().all()
        racas = Raca.query.order_by(Raca.nome).all()
        return render_template("wiki.html",
                               title="Administração",
                               usuarios=usuarios,
                               racas=racas)


@app.route("/admin/usuarios/<int:usuario_id>/editar", methods=["GET", "POST"])
@login_required
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
            return redirect(url_for('wiki'))

    return render_template("admin_editar_usuario.html",
                           title="Editar usuário",
                           formulario=formulario,
                           usuario=usuario)


@app.route("/admin/usuarios/<int:usuario_id>/excluir", methods=["POST"])
@login_required
def admin_excluir_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)
    if usuario.id == current_user.id:
        flash("Você não pode excluir a própria conta de administrador.", "error")
        return redirect(url_for('wiki'))
    if usuario.personagens:
        flash("Não é possível excluir este usuário enquanto ele tiver personagens vinculados.",
              "error")
        return redirect(url_for('wiki'))

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
    return redirect(url_for('wiki'))


@app.route("/admin/usuarios/<int:usuario_id>/promover", methods=["POST"])
@login_required
def admin_promover_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)
    if usuario.role != Usuario.ROLES['USER']:
        flash("Este usuário não possui perfil padrão.", "error")
        return redirect(url_for('wiki'))

    usuario.role = Usuario.ROLES['ADM']
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao promover usuário %s", usuario.id)
        flash("Não foi possível promover o usuário.", "error")
    else:
        flash("Usuário promovido a administrador com sucesso.", "success")
    return redirect(url_for('wiki'))


@app.route("/admin/usuarios/<int:usuario_id>/rebaixar", methods=["POST"])
@login_required
def admin_rebaixar_usuario(usuario_id):
    if not current_user.is_authenticated or current_user.role != Usuario.ROLES['ADM']:
        abort(403)

    usuario = UsuarioService.buscar_por_id(usuario_id)
    if usuario is None:
        abort(404)
    if usuario.id == current_user.id:
        flash("Você não pode remover a própria autorização de administrador.", "error")
        return redirect(url_for('wiki'))
    if usuario.role != Usuario.ROLES['ADM']:
        flash("Este usuário não possui perfil de administrador.", "error")
        return redirect(url_for('wiki'))
    if Usuario.query.filter_by(role=Usuario.ROLES['ADM']).count() <= 1:
        flash("Não é possível rebaixar o último administrador.", "error")
        return redirect(url_for('wiki'))

    usuario.role = Usuario.ROLES['USER']
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao rebaixar usuário %s", usuario.id)
        flash("Não foi possível remover a autorização de administrador.", "error")
    else:
        flash("Administrador rebaixado a usuário padrão com sucesso.", "success")
    return redirect(url_for('wiki'))

@app.errorhandler(403)
def erro_403(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def erro_404(e):
    return render_template('404.html'), 404