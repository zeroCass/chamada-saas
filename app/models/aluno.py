from . import db
from .usuario import Usuario
from .matricula import association_table


class Aluno(Usuario):
    __tablename__ = "aluno"

    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    # Criamos uma tabela de associação chamada association_table. Essa tabela representa a relação de muitos-para-muitos entre Aluno e Turma.
    turmas = db.relationship(
        'Turma', secondary=association_table, backref='alunos')

    def __repr__(self) -> str:
        return f"<Aluno {self.id}> Nome:{self.nome} - Matricula:{self.matricula} - Email:{self.email} - Turmas:{self.turmas}"
