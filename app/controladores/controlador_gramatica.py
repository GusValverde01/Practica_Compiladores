from flask import Blueprint, render_template, request
from app.modelos.gramatica import Gramatica

gramatica_bp = Blueprint('gramatica', __name__)

@gramatica_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@gramatica_bp.route('/procesar', methods=['POST'])
def ingresar_gramatica():
    gramatica = request.form.get('gramatica', '')
    gr = Gramatica(gramatica)
    cuadrupla = gr.mostrar_cuadrupla()
    resultado = f"""
        <strong>No terminales (N):</strong> {cuadrupla['N']}<br>
        <strong>Terminales (T):</strong> {cuadrupla['T']}<br>
        <strong>Producciones (P):</strong> <pre>{cuadrupla['P']}</pre><br>
        <strong>Símbolo inicial (S):</strong> {cuadrupla['S']}
    """

    clasificacion = gr.clasificar_chomsky()
    resultado = f"""
    <strong>No terminales (N):</strong> {cuadrupla['N']}<br>
    <strong>Terminales (T):</strong> {cuadrupla['T']}<br>
    <strong>Producciones (P):</strong> <pre>{cuadrupla['P']}</pre><br>
    <strong>Símbolo inicial (S):</strong> {cuadrupla['S']}<br>
    <strong>Clasificación (Chomsky):</strong> <span style='color:blue'>{clasificacion}</span>
    """

    return render_template('index.html', resultado=resultado)

#Se mostraran los resultados en los metodos de limpieza 
@gramatica_bp.route('/procesar', methods=['POST'], endpoint='procesar_gramatica')
def ingresar_gramatica():
    gramatica = request.form.get('gramatica', '')
    gr = Gramatica(gramatica)
    cuadrupla = gr.mostrar_cuadrupla()
    clasificacion = gr.clasificar_chomsky()

    vivos, muertos = gr.simbolos_vivos_muertos()
    accesibles, inaccesibles = gr.simbolos_accesibles_inaccesibles()
    reglas_eliminadas = ""
    if clasificacion in ["Tipo 2 (Gramática Libre de Contexto)", "Tipo 3 (Gramática Regular)"]:
        reglas_eliminadas = gr.limpiar()  # Realiza la limpieza solo si es tipo 2 o 3

    cuadrupla_final = gr.mostrar_cuadrupla()

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
