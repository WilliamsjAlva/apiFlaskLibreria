from flask import Blueprint, jsonify, request
from app.models import Resena, db

bp = Blueprint('resenas', __name__, url_prefix='/resenas')

@bp.route('/', methods=['GET'])
def get_resenas():
    resenas = Resena.query.all()
    return jsonify([{
        "id": resena.id,
        "contenido": resena.contenido,
        "libroId": resena.libroId,
        "usuarioId": resena.usuarioId,
        "fechaCreacion": resena.fechaCreacion,
        "fechaActualizacion": resena.fechaActualizacion
    } for resena in resenas])

@bp.route('/', methods=['POST'])
def create_resena():
    data = request.get_json()
    if not data or 'contenido' not in data or 'libroId' not in data or 'usuarioId' not in data:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    nueva_resena = Resena(
        contenido=data['contenido'],
        libroId=data['libroId'],
        usuarioId=data['usuarioId']
    )
    db.session.add(nueva_resena)
    db.session.commit()
    return jsonify({"id": nueva_resena.id, "contenido": nueva_resena.contenido}), 201
