from . import db
from flask_login import UserMixin

class Turma(UserMixin, db.Model):
    __tablename__ = "turma"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    semestre = db.Column(db.String(10), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False) #professor_id armazenará o ID do professor relacionado à turma.
    #token_presenca