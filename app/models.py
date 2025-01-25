from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para la tabla Estudiantes
class Estudiante(db.Model):
    __tablename__ = 'Estudiantes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Estudiante {self.nombre} {self.apellido}>'

# Modelo para la tabla Cursos
class Curso(db.Model):
    __tablename__ = 'Cursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)
    profesor = db.Column(db.String(100))

    def __repr__(self):
        return f'<Curso {self.nombre}>'
    
# Modelo para la tabla Inscripciones
class Inscripcion(db.Model):
    __tablename__ = 'Inscripciones'
    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('Estudiantes.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('Cursos.id'), nullable=False)
    fecha_inscripcion = db.Column(db.Date, default=date.today, nullable=False)

    estudiante = db.relationship('Estudiante', backref=db.backref('inscripciones', lazy=True))
    curso = db.relationship('Curso', backref=db.backref('inscripciones', lazy=True))

    def __repr__(self):
        return f'<Inscripcion Estudiante {self.estudiante_id} Curso {self.curso_id}>'