# Práctica de Compiladores
## Segundo parcial || Práctica uno
### Limpiador de grámaticas libres de contexto 

**Camacho Zavala Ricardo**
**Valverde Rojas Gustavo**

Esta práctica tuvo como finalidad desarrollar una aplicación capaz de limpiar gramáticas libres de contexto clasificadas como tipo 2 (o tipo 3) de acuerdo con la jerarquía de Chomsky y fue desarrollado con el framework flask.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **modelo**: Contiene los modelos de datos.

- **vista**: Contiene los modelos de datos.
  
- **controlador**: Contiene los controladores de la aplicación.

## Evidencias de Funcionamiento
interfaz de inicio
![image](https://github.com/user-attachments/assets/fcaf46ee-9902-4ec6-89d4-1d8249b1f059)

agregar grámatica

limpieza de grámatica 

## Intrucciones de ejecución

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/GusValverde01/Practica_Compiladores.git
   ```
2. **Abre la terminal y ejecuta el siguiente comando para crear la carpeta venv (entorno virtual) y todo su contenido:**
    ```sh
    python -m venv venv
    ```
3. **Antes de activar el entorno (solo mientras está abierta la terminal actual) ejecuta:**
    ```sh
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```
4.  **Cuando te pregunte si deseas cambiar la directiva, responde: Si no es el caso, ignora esto**
    ```sh
    S
    ```
5.  **Luego activa el entorno virtual:**
    ```sh
    .\venv\Scripts\Activate.ps1
    ```
## En caso de no tener Flask instalado sigue este paso con el entorno virtual activado:

- **Instalar Flask:**
   ```sh
   pip install flask
   ```
## Continuando con la ejecución:
6. **En la terminal (aún con (venv) activo), corre la aplicación con:**
    ```sh
    python run.py
    ```
7. **Acceder al endpoint:**
    ```
    En el navegador: http://127.0.0.1:5000
    ```
## Se deberá mostrar en terminal esto si compiló con éxito: 
![image](https://github.com/user-attachments/assets/91dcd0b1-5fbd-494f-8873-8153bd1c4d80)


## Errores conocidos 

**Al no tener una versión de Python agregada en el path o en el control de versiones no puede se puede ejecutar el proyecto**