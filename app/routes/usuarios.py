from flask import Blueprint, jsonify, request
from app.models import Usuario, db

bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        "id": usuario.id,
        "nombre": usuario.nombre,
        "fechaCreacion": usuario.fechaCreacion,
        "fechaActualizacion": usuario.fechaActualizacion
    } for usuario in usuarios])

@bp.route('/', methods=['POST'])
def create_usuario():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "El nombre es requerido"}), 400

    nuevo_usuario = Usuario(nombre=data['nombre'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"id": nuevo_usuario.id, "nombre": nuevo_usuario.nombre}), 201
