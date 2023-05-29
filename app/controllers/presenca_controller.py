from ..webapp import db
from flask import Blueprint, make_response, send_file, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.aula import Aula
from app.utils.qrcode import gerar_qrcode
from datetime import datetime
from flask_login import login_required, current_user


import io

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
        


@bp.route("/qrcode", methods=["GET"])
@login_required
def qrcode(turma_id, aula_id):

    aula = Aula.query.filter_by(id=aula_id).first()
    qrcode_image = gerar_qrcode(aula.token)

    return send_file(qrcode_image, mimetype="image/png")
