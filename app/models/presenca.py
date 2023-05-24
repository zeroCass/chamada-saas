from . import db
from flask_login import UserMixin


class Presenca(UserMixin, db.Model):
    __tablename__ = "presenca"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=True)
    aluno_matricula = db.Column(db.String(15), db.ForeignKey(
        'usuario.matricula'), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    # Esses relacionamentos permitem acessar o aluno e a turma associados a uma presença específica.
    aluno = db.relationship('Aluno', backref='presencas')
    turma = db.relationship('Turma', backref='presencas')
