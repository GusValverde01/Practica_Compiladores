from flask import Blueprint, render_template, request
from app.modelos.gramatica import Gramatica

# Crea el blueprint para el controlador de gramatica
gramatica_bp = Blueprint('gramatica', __name__)

@gramatica_bp.route('/', methods=['GET', 'POST'])
def ingresar_gramatica():
    resultado = None

    if request.method == 'POST':
        gramatica_texto = request.form['gramatica']
        gr = Gramatica(gramatica_texto)

        cuadrupla = gr.mostrar_cuadrupla()
        clasificacion = gr.clasificacion()
        vivos = ', '.join(sorted([str(s) for s in gr.simbolos_vivos() if s is not None]))
        muertos = ', '.join(sorted([str(s) for s in gr.simbolos_muertos() if s is not None]))
        accesibles = ', '.join(sorted([str(s) for s in gr.simbolos_accesibles() if s is not None]))
        inaccesibles = ', '.join(sorted([str(s) for s in gr.simbolos_inaccesibles() if s is not None]))
        reglas_eliminadas = gr.reglas_eliminadas()
        cuadrupla_final = gr.mostrar_cuadrupla_final()

        resultado = f"""
        <strong>No terminales (N):</strong> {cuadrupla['N']}<br>
        <strong>Terminales (T):</strong> {cuadrupla['T']}<br>
        <strong>Producciones (P):</strong> <pre>{cuadrupla['P']}</pre><br>
        <strong>Símbolo inicial (S):</strong> {cuadrupla['S']}<br>
        <strong>Clasificación (Chomsky):</strong> <span style='color:blue'>{clasificacion}</span><br>
        <hr>
        <strong>Símbolos Vivos:</strong> {vivos}<br>
        <strong>Símbolos Muertos:</strong> {muertos}<br>
        <strong>Símbolos Accesibles:</strong> {accesibles}<br>
        <strong>Símbolos Inaccesibles:</strong> {inaccesibles}<br>
        <strong>Reglas Eliminadas:</strong> <pre>{reglas_eliminadas}</pre><br>
        <hr>
        <strong>Cuádrupla final limpia:</strong><br>
        No terminales: {cuadrupla_final['N']}<br>
        Terminales: {cuadrupla_final['T']}<br>
        Producciones: <pre>{cuadrupla_final['P']}</pre><br>
        Símbolo inicial: {cuadrupla_final['S']}
        """

    return render_template('index.html', resultado=resultado)
