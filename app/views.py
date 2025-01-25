from datetime import date
from flask import render_template, request, redirect, url_for, flash, Flask
from app.models import db, Estudiante, Curso, Inscripcion

app = Flask(__name__, template_folder='app/templates')

# Pagina de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para listar estudiantes
@app.route("/estudiante")
def listar_estudiantes():
    estudiantes = Estudiante.query.all()
    return render_template('estudiantes/index.html', estudiantes=estudiantes)

# Ruta para crear un estudiante
@app.route('/crear-estudiante', methods=['GET', 'POST'])
def crear_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        email = request.form['email']

        nuevo_estudiante = Estudiante(nombre=nombre, apellido=apellido, edad=edad, email=email)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        flash('Estudiante agregado con éxito')
        return redirect(url_for('listar_estudiantes'))

    return render_template('estudiantes/create.html')

# Ruta para editar un estudiante
@app.route('/editar-estudiante/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    estudiante = Estudiante.query.get(id)
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        estudiante.apellido = request.form['apellido']
        estudiante.edad = request.form['edad']
        estudiante.email = request.form['email']

        db.session.commit()
        flash('Estudiante actualizado con éxito')
        return redirect(url_for('listar_estudiantes'))

    return render_template('estudiantes/edit.html', estudiante=estudiante)

# Ruta para eliminar un estudiante
@app.route('/eliminar-estudiante/<int:id>', methods=['POST'])
def eliminar_estudiante(id):
    estudiante = Estudiante.query.get(id)
    db.session.delete(estudiante)
    db.session.commit()
    flash('Estudiante eliminado con éxito')
    return redirect(url_for('listar_estudiantes'))

# Ruta para listar cursos
@app.route('/cursos')
def listar_cursos():
    cursos = Curso.query.all()
    return render_template('cursos/index.html', cursos=cursos)

# Ruta para crear cursos
@app.route('/crear-curso', methods=['GET', 'POST'])
def crear_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nivel = request.form['nivel']
        profesor = request.form['profesor']

        nuevo_curso = Curso(nombre=nombre, nivel=nivel, profesor=profesor)
        db.session.add(nuevo_curso)
        db.session.commit()
        flash('Curso agregado con éxito')
        return redirect(url_for('listar_cursos'))
    
    return render_template('cursos/create.html')

# Ruta para editar cursos
@app.route('/editar-curso/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = Curso.query.get(id)

    if request.method == 'POST':
        curso.nombre = request.form['nombre']
        curso.nivel = request.form['nivel']
        curso.profesor = request.form['profesor']

        db.session.commit()
        flash('Curso actualizado con éxito')
        return redirect(url_for('listar_cursos'))
    
    return render_template('cursos/edit.html', curso=curso)

# Ruta para eliminar un curso
@app.route('/eliminar-curso/<int:id>', methods=['POST'])
def eliminar_curso(id):
    curso = Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    flash('Curso eliminado con éxito')
    return redirect(url_for('listar_cursos'))

# Ruta para listar inscripciones
@app.route('/inscripciones')
def listar_inscripciones():
    inscripciones = Inscripcion.query.all()
    return render_template('inscripciones/index.html', inscripciones=inscripciones)

# Ruta para crear inscripción
@app.route('/crear-inscripcion', methods=['GET', 'POST'])
def crear_inscripcion():
    estudiantes = Estudiante.query.all()
    cursos = Curso.query.all()

    if request.method == 'POST':
        estudiante_id = request.form['estudiante_id']
        curso_id = request.form['curso_id']
        nueva_inscripcion = Inscripcion(estudiante_id=estudiante_id, curso_id=curso_id)
        db.session.add(nueva_inscripcion)
        db.session.commit()
        flash('Inscripción agregada con éxito')
        return redirect(url_for('listar_inscripciones'))

    return render_template('inscripciones/create.html', estudiantes=estudiantes, cursos=cursos)

# Ruta para eliminar inscripción
@app.route('/eliminar-inscripcion/<int:id>', methods=['POST'])
def eliminar_inscripcion(id):
    inscripcion = Inscripcion.query.get(id)
    db.session.delete(inscripcion)
    db.session.commit()
    flash('Inscripción eliminada con éxito')
    return redirect(url_for('listar_inscripciones'))

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
