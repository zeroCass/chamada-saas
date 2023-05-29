from ..webapp import db
from flask import Blueprint, make_response, send_file
from flask_login import login_required
from ..models.aula import Aula
from app.utils.qrcode import gerar_qrcode

import io

bp = Blueprint("presenca", __name__)


def register_blueprint(parent_blueprint: Blueprint):
    parent_blueprint.register_blueprint(
        bp, url_prefix=f"/<int:aula_id>/presenca")


@bp.route("/", methods=["POST", "GET"])
@login_required
def registrar_presenca(turma_id, aula_id):
    return f"<h1>Aula ID: {aula_id} </h1>"


@bp.route("/qrcode", methods=["GET"])
@login_required
def qrcode(turma_id, aula_id):

    aula = Aula.query.filter_by(id=aula_id).first()
    qrcode_image = gerar_qrcode(aula.token)

    return send_file(qrcode_image, mimetype="image/png")
