from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Aluno, Professor
from ..webapp import db

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")

        try:
            # Verificar se existe essa natricula cadastrada no banco de dados
                user = Aluno.query.filter_by(matricula=matricula).first() or Professor.query.filter_by(matricula=matricula).first()
                if user:
                    if user.senha == senha:
                        flash("Logado com sucesso!", category="sucess")
                        login_user(user, remember=True)
                        return redirect(url_for("index.index"))
                    else:
                        flash("Senha invalida!", category="error")
                else:
                    flash("Usuario nao existe!", category="error")
        except Exception:
            db.session.rollback()
            flash("Erro ao acessar o banco de dados.", category="error")

    return render_template("auth/login.jinja2")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")
        tipo_usuario = request.form.get("tipo_usuario")
    
        try:
        # Verificar se o email já está cadastrado no banco de dados
            email_existente = Aluno.query.filter_by(email=email).first() or Professor.query.filter_by(email=email).first()
            if email_existente:
                flash("Email já cadastrado. Por favor, tente com outro email.", category="error")

        # Salvar os dados nas tabelas correspondentes com base no tipo de usuário
            if tipo_usuario == "Aluno":
                aluno = Aluno(nome=nome, email=email, matricula=matricula, senha=senha)
                db.session.add(aluno)
                login_user(aluno, remember=True) #ERRO
            elif tipo_usuario == "Professor":
                professor = Professor(nome=nome, email=email, matricula=matricula, senha=senha)
                db.session.add(professor)
                login_user(professor, remember=True) #ERRO

            db.session.commit()
            flash("Registro realizado com sucesso!", category="sucess")
            return redirect(url_for("index.index"))
        
        except Exception:
            db.session.rollback()
            flash("Erro ao se Registrar", category="error")

    return render_template("auth/register.jinja2")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))