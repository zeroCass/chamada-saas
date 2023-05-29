from ..webapp import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models import Aula

bp = Blueprint("presenca", __name__)


def register_blueprint(parent_blueprint: Blueprint):
    parent_blueprint.register_blueprint(
        bp, url_prefix=f"/<int:aula_id>/presenca")


@bp.route("/", methods=["POST", "GET"])
@login_required
def registrar_presenca(turma_id, aula_id):
    return f"<h1>Aula ID: {aula_id} </h1>"
