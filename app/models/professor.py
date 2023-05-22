from . import db
from flask_login import UserMixin

class Professor(UserMixin, db.Model):
    __tablename__ = "professor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    matricula = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    turmas = db.relationship('Turma', backref='professor', lazy=True) #um prof pode ter varias turmas (relação um para N)