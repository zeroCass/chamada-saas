from . import db
from flask_login import UserMixin
from .matricula import association_table

class Aluno(UserMixin, db.Model):
    __tablename__ = "aluno"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    matricula = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    turmas = db.relationship('Turma', secondary=association_table, backref='alunos') #Criamos uma tabela de associação chamada association_table. Essa tabela representa a relação de muitos-para-muitos entre Aluno e Turma.