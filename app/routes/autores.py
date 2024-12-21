from flask import Blueprint, jsonify, request
from app.models import Autor, db

bp = Blueprint('autores', __name__, url_prefix='/autores')

@bp.route('/', methods=['GET'])
def get_autores():
    autores = Autor.query.all()
    return jsonify([{
        "id": autor.id,
        "nombre": autor.nombre,
        "fechaCreacion": autor.fechaCreacion,
        "fechaActualizacion": autor.fechaActualizacion
    } for autor in autores])

@bp.route('/', methods=['POST'])
def create_autor():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "El nombre es requerido"}), 400

    nuevo_autor = Autor(nombre=data['nombre'])
    db.session.add(nuevo_autor)
    db.session.commit()
    return jsonify({"id": nuevo_autor.id, "nombre": nuevo_autor.nombre}), 201

@bp.route('/<int:id>', methods=['PATCH'])
def update_autor(id):
    autor = Autor.query.get_or_404(id)
    data = request.get_json()
    autor.nombre = data.get('nombre', autor.nombre)
    db.session.commit()
    return jsonify({"id": autor.id, "nombre": autor.nombre}), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_autor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return jsonify({"message": "Autor eliminado"}), 200
