from ..webapp import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models import Turma, Aula
from datetime import datetime

bp = Blueprint("aulas", __name__)

@bp.route("/", methods=["GET"])
@login_required
def new():
    turma_id = request.args.get('turma_id')  # Acessando o valor do parâmetro 'turma_id' no URL
    turma = Turma.query.get(turma_id)
    return render_template("aulas/new.jinja2", turma=turma)

@bp.route("/<int:turma_id>/create", methods=["POST"])
@login_required
def create(turma_id):
    data_aula = request.form['data_aula']
    
    data_aula = datetime.strptime(data_aula, "%Y-%m-%d").date()

    # Verificar se já existe uma aula agendada para a data informada
    existing_aula = Aula.query.filter_by(turma_id=turma_id, data_aula=data_aula).first()
    if existing_aula:
        flash("Já existe uma aula para essa data")
        return redirect(url_for("turmas.show", id=turma_id))
        

    data_atual = datetime.now().date()
    hora_atual = datetime.now().time()

    turma = Turma.query.get(turma_id)

    if data_aula < data_atual:
        status = "finalizado"
    elif data_aula > data_atual:
        status = "agendado"
    else:
        if hora_atual >= turma.horario_inicio and hora_atual < turma.horario_fim:
            status = "em andamento"
        elif hora_atual > turma.horario_inicio and hora_atual >= turma.horario_fim:
            status = "finalizado"
        else:
            status = "agendado"
        
    aula = Aula(turma_id=turma_id, data_aula=data_aula, status=status)

    db.session.add(aula)
    db.session.commit()
    
    return redirect(url_for("turmas.show", id=turma_id))
