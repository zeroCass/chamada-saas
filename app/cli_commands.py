from flask.cli import AppGroup
from .webapp import db
from seed import alunos, professores, turmas
from .models import Aluno, Professor, Turma

seed_cli = AppGroup("seed")


@seed_cli.command("alunos")
def seed_alunos():
    for aluno in alunos:
        db.session.add(Aluno(**aluno))
    db.session.commit()


@seed_cli.command("professores")
def seed_professores():
    for professor in professores:
        db.session.add(Professor(**professor))
    db.session.commit()


@seed_cli.command("turmas")
def seed_turmas():
    for turma in turmas:
        db.session.add(Turma(**turma))
    db.session.commit()
