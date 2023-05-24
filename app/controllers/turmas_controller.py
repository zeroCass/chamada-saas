from ..webapp import db
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from ..models import Turma

bp = Blueprint("turmas", __name__)


@bp.route("/", methods=["GET"])
@login_required
def index():
    turmas = Turma.query.all()
    # user_type = session.get("user_type")

    print(f"Turmas: {turmas}")
    return render_template("turmas/index.jinja2", turmas=turmas)


@bp.route("/new", methods=["GET"])
@login_required
def new():
    return render_template("turmas/new.jinja2")

@bp.route("/validate", methods=["GET", "POST"])
@login_required
def validate():
    if request.method == "POST":
        # senha = request.form.get("senha")
        flash("Você foi matriculado em uma turma")
        return redirect(url_for("turmas.index"))
    
    return render_template("turmas/validate.jinja2")

@bp.route("/", methods=["POST"])
@login_required
def create():
    nome = request.form.get("nome")
    horario = request.form.get("horario")
    senha = request.form.get("senha")
    semestre = request.form.get("semestre")
    professor_id = current_user.id

    print(
        f"Form fields: {nome}, {horario}, {senha}, {semestre}, {professor_id}")

    new_turma = Turma(nome=nome, horario=horario, senha=senha,
                      semestre=semestre, professor_id=professor_id)
    try:
        db.session.add(new_turma)
        db.session.commit()
        flash("Turma criada")
    except Exception:
        db.session.rollback()
        flash("Erro ao criar turma")

    return redirect(url_for("turmas.index"))
