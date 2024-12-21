from app.routes.autores import bp as autores_bp
from app.routes.generos import bp as generos_bp
from app.routes.editoriales import bp as editoriales_bp
from app.routes.usuarios import bp as usuarios_bp
from app.routes.resenas import bp as resenas_bp
from app.routes.libros import bp as libros_bp

def register_routes(app):
    app.register_blueprint(autores_bp)
    app.register_blueprint(generos_bp)
    app.register_blueprint(editoriales_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(resenas_bp)
    app.register_blueprint(libros_bp)
