from ..webapp import db
from .aluno import Aluno
from .professor import Professor
from .turma import Turma
from .presenca import  Presenca
from .matricula import association_table

__all__ = [Aluno, Professor, Turma, Presenca, association_table]