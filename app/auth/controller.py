from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Aluno, Professor
from ..webapp import db

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.jinja2")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")
        tipo_usuario = request.form.get("tipo_usuario")
    
    # Verificar se o email já está cadastrado no banco de dados
        email_existente = Aluno.query.filter_by(email=email).first() or Professor.query.filter_by(email=email).first()
        if email_existente:
            flash("Email já cadastrado. Por favor, tente com outro email.")

    # Salvar os dados nas tabelas correspondentes com base no tipo de usuário
        try:
            if tipo_usuario == "Aluno":
                aluno = Aluno(nome=nome, email=email, matricula=matricula, senha=senha)
                db.session.add(aluno)
            elif tipo_usuario == "Professor":
                professor = Professor(nome=nome, email=email, matricula=matricula, senha=senha)
                db.session.add(professor)

            db.session.commit()
            flash("Registro realizado com sucesso!")
            return redirect(url_for("index.index"))
        except Exception:
            db.session.rollback()
            flash("Erro ao se Registrar")

    return render_template("auth/register.jinja2")