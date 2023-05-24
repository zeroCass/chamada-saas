from . import db
from sqlalchemy import Enum

class Aula(db.Model):
    __tablename__ = "aula"

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    data_aula = db.Column(db.Date, nullable=False)
    status = db.Column(
        Enum("agendado", "finalizado", "em andamento", "cancelado", name="StatusAula"), nullable=False)

    presencas = db.relationship('Presenca', backref='aula_presenca', lazy=True) #1 to N

    def __repr__(self) -> str:
        return "<Aula %r>" % self.id
