from flask import Flask

def crear_app():
    app = Flask(__name__, 
                template_folder='vistas/templates', 
                static_folder='vistas/static')

    from app.controladores.controlador_gramatica import gramatica_bp
    app.register_blueprint(gramatica_bp)

    return app
