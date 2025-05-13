# Práctica de Compiladores
## Limpiador de grámaticas libres de contexto 

**Camacho Zavala Ricardo**

**Valverde Rojas Gustavo**

Esta práctica tuvo como finalidad desarrollar una aplicación capaz de limpiar gramáticas libres de contexto clasificadas como tipo 2 (o tipo 3) de acuerdo con la jerarquía de Chomsky.

Este programa analiza y transforma gramáticas libres de contexto (CFGs) para producir
una versión simplificada. Incluye clasificación, limpieza y reestructuración según
los principios de teoría de compiladores, y fue desarrollado con el framework Flask.

## Estructura del Proyecto

El proyecto sigue una estructura tipica de Flask, está organizado de la siguiente manera:

- **Modelo**: Donde contiene los modelos de datos, proporciona la lógica para procesar y analizar gramáticas formales.

- **Vista**: Contiene los modelos de datos y muestra un formulario para ingresar la gramática y los resultados generados.
  
- **Controlador**: Donde contiene los controladores de la aplicación, define la ruta y maneja las solicitudes GET/POST, interactuando con la clase Gramatica. 

## Intrucciones de ejecución

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/GusValverde01/Practica_Compiladores.git
   ```
2. **Abrir la terminal y ejecutar el siguiente comando para crear la carpeta venv (entorno virtual) y todo su contenido:**
    ```sh
    python -m venv venv
    ```
3. **Antes de activar el entorno (solo mientras está abierta la terminal actual) ejecutar:**
    ```sh
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```
4.  **Cuando pregunte si deseas cambiar la directiva, responde: Si no es el caso, ignorar esto**
    ```sh
    S
    ```
5.  **Luego activar el entorno virtual:**
    ```sh
    .\venv\Scripts\Activate.ps1
    ```
### En caso de no tener Flask instalado seguir este paso con el entorno virtual activado:

- **Instalar Flask:**
   ```sh
   pip install flask
   ```
### Continuando con la ejecución:
6. **En la terminal (aún con (venv) activo), corre la aplicación con:**
    ```sh
    python run.py
    ```
7. **Acceder al endpoint:**
    ```
    En el navegador: http://127.0.0.1:5000
    ```
### Se deberá mostrar en terminal esto si compiló con éxito: 
![image](https://github.com/user-attachments/assets/91dcd0b1-5fbd-494f-8873-8153bd1c4d80)

## Evidencias de Funcionamiento
Interfaz de inicio
![Captura de pantalla 2025-05-11 011004](https://github.com/user-attachments/assets/320b1275-8ec5-4876-b486-3010bb30c248)

Agregar grámatica
![Captura de pantalla 2025-05-11 011121](https://github.com/user-attachments/assets/c6943d74-4278-444f-8964-c0de9529310a)

Limpieza de grámatica 
![Captura de pantalla 2025-05-11 011430](https://github.com/user-attachments/assets/c7dee773-ee31-40a8-8dbf-693aa0807a01)


## Errores conocidos 

Al no tener una versión de Python agregada en el path o en el control de versiones no se puede ejecutar el proyecto, se recomienda tener la version de python 3.13 o superior ya que en esta versión fue desarrollado

**En caso de no tener agregado en el path la versión de python, se explica a continuación:**
1. Buscar en el buscador de windows "path" o "control de versiones"
   ![Captura de pantalla 2025-05-13 013019](https://github.com/user-attachments/assets/647a16d8-79a8-4473-b926-c2762042a28d)
2. En el menú que aparecío, selecciona "variables de entorno", es el último boton
   ![Captura de pantalla 2025-05-13 013121](https://github.com/user-attachments/assets/d145ef3a-5d6c-4ec1-ad94-986949dfd0f0)
3. Por último, en caso de no tener la versión agregada en el path, hazlo dando click en "nueva", tendrás que seleccionar la ruta donde tengas instalado python
   ![Captura de pantalla 2025-05-13 013202](https://github.com/user-attachments/assets/26f59e0e-5fb9-434d-b097-4e8fa21eb44f)
4. En caso de que esto no funcione, deberás instalar de nuevo python, y durante la instalación selecciona que agregue las variables directo al path
