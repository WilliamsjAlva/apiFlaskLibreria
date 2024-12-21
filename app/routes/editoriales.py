from flask import Blueprint, jsonify, request
from app.models import Editorial, db

bp = Blueprint('editoriales', __name__, url_prefix='/editoriales')

@bp.route('/', methods=['GET'])
def get_editoriales():
    editoriales = Editorial.query.all()
    return jsonify([{
        "id": editorial.id,
        "nombre": editorial.nombre,
        "fechaCreacion": editorial.fechaCreacion,
        "fechaActualizacion": editorial.fechaActualizacion
    } for editorial in editoriales])

@bp.route('/', methods=['POST'])
def create_editorial():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "El nombre es requerido"}), 400

    nueva_editorial = Editorial(nombre=data['nombre'])
    db.session.add(nueva_editorial)
    db.session.commit()
    return jsonify({"id": nueva_editorial.id, "nombre": nueva_editorial.nombre}), 201
