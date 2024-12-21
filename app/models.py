from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Editorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    anoPublicacion = db.Column(db.Integer, nullable=False)
    autorId = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    generoId = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
    editorialId = db.Column(db.Integer, db.ForeignKey('editorial.id'), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Resena(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    libroId = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fechaCreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaActualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)
