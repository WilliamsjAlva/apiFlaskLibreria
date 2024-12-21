from flask import Blueprint, request, jsonify
from app.models import Libro, db

bp = Blueprint('libros', __name__, url_prefix='/libros')

@bp.route('/', methods=['GET'])
def obtener_libros():
    libros = Libro.query.all()
    return jsonify([
        {
            'id': libro.id,
            'titulo': libro.titulo,
            'anoPublicacion': libro.anoPublicacion,
            'autorId': libro.autorId,
            'generoId': libro.generoId,
            'editorialId': libro.editorialId,
            'fechaCreacion': libro.fechaCreacion,
            'fechaActualizacion': libro.fechaActualizacion
        } for libro in libros
    ])

@bp.route('/', methods=['POST'])
def crear_libro():
    datos = request.json
    nuevo_libro = Libro(
        titulo=datos['titulo'],
        anoPublicacion=datos['anoPublicacion'],
        autorId=datos['autorId'],
        generoId=datos['generoId'],
        editorialId=datos['editorialId']
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({
        'id': nuevo_libro.id,
        'titulo': nuevo_libro.titulo
    }), 201
