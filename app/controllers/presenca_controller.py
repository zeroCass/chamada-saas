from ..webapp import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from ..models import Aula, Presenca, Aluno

bp = Blueprint("presenca", __name__)


def register_blueprint(parent_blueprint: Blueprint):
    parent_blueprint.register_blueprint(
        bp, url_prefix=f"/<int:aula_id>/presenca")


@bp.route("/", methods=["POST"])
@login_required
def registrar_presenca(turma_id, aula_id):
        data_atual = datetime.now()
        aluno_id = current_user.id

        # Verifica se o aluno já possui uma presença registrada para essa aula
        presenca_existente = Presenca.query.filter_by(aula_id=aula_id, aluno_id=aluno_id).first()
        if presenca_existente:
            flash("Presença já foi registrada", category="warning")
            return redirect(url_for("turmas.show", turma_id=turma_id))
        
        presenca = Presenca(aula_id=aula_id, data=data_atual, aluno_id=aluno_id)

        db.session.add(presenca)
        db.session.commit()

        flash("Chamada Assinada", category="sucess")
        return redirect(url_for("turmas.show", turma_id=turma_id))
        
@bp.route("/alunos", methods=["GET"])
@login_required
def listar_presencas(turma_id, aula_id):
    aula = Aula.query.get(aula_id)
    alunos = Aluno.query.all()
    presencas = Presenca.query.filter_by(aula_id=aula_id).all()

    return render_template("aulas/presencas.jinja2", aula=aula, alunos=alunos, presencas=presencas)
