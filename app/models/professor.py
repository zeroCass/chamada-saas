from . import db
from .usuario import Usuario


class Professor(Usuario):
    __tablename__ = "professor"

    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    # um prof pode ter varias turmas (relação um para N)
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def __repr__(self) -> str:
        return f"<Professor {self.id}> Nome:{self.nome} - Matricula:{self.matricula} - Email:{self.email} - Turmas:{self.turmas}"
