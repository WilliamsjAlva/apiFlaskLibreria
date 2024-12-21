from flask import Blueprint, jsonify, request
from app.models import Genero, db

bp = Blueprint('generos', __name__, url_prefix='/generos')

@bp.route('/', methods=['GET'])
def get_generos():
    generos = Genero.query.all()
    return jsonify([{
        "id": genero.id,
        "nombre": genero.nombre,
        "fechaCreacion": genero.fechaCreacion,
        "fechaActualizacion": genero.fechaActualizacion
    } for genero in generos])

@bp.route('/', methods=['POST'])
def create_genero():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "El nombre es requerido"}), 400

    nuevo_genero = Genero(nombre=data['nombre'])
    db.session.add(nuevo_genero)
    db.session.commit()
    return jsonify({"id": nuevo_genero.id, "nombre": nuevo_genero.nombre}), 201
