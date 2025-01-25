from flask import Flask
from app import create_app
from app.views import (
    index, listar_estudiantes, crear_estudiante, editar_estudiante, eliminar_estudiante,
    listar_cursos, crear_curso, editar_curso, eliminar_curso,
    listar_inscripciones, crear_inscripcion, eliminar_inscripcion
)

app = create_app()

# Registrar rutas
app.add_url_rule('/', 'index', index)
app.add_url_rule('/estudiante', 'listar_estudiantes', listar_estudiantes)
app.add_url_rule('/crear-estudiante', 'crear_estudiante', crear_estudiante, methods=['GET', 'POST'])
app.add_url_rule('/editar-estudiante/<int:id>', 'editar_estudiante', editar_estudiante, methods=['GET', 'POST'])
app.add_url_rule('/eliminar-estudiante/<int:id>', 'eliminar_estudiante', eliminar_estudiante)
app.add_url_rule('/cursos', 'listar_cursos', listar_cursos)
app.add_url_rule('/crear-curso', 'crear_curso', crear_curso, methods=['GET', 'POST'])
app.add_url_rule('/editar-curso/<int:id>', 'editar_curso', editar_curso, methods=['GET', 'POST'])
app.add_url_rule('/eliminar-curso/<int:id>', 'eliminar_curso', eliminar_curso)
app.add_url_rule('/inscripciones', 'listar_inscripciones', listar_inscripciones)
app.add_url_rule('/crear-inscripcion', 'crear_inscripcion', crear_inscripcion, methods=['GET', 'POST'])
app.add_url_rule('/eliminar-inscripcion/<int:id>', 'eliminar_inscripcion', eliminar_inscripcion)

if __name__ == '__main__':
    #app = create_app()
    app.run(debug=True)
