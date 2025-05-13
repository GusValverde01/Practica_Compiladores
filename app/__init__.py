from flask import Flask

# Define la función para crear la aplicación Flask
def crear_app():
    app = Flask(__name__, 
                template_folder='vistas/templates', # Carpeta donde se encuentran las plantillas HTML
                static_folder='vistas/static') # Carpeta para archivos estáticos (CSS)

    # Importa el blueprint definido en controlador_gramatica.py
    from app.controladores.controlador_gramatica import gramatica_bp
    app.register_blueprint(gramatica_bp)

    return app
