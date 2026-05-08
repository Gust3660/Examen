# Examen - Buscador de estados con Streamlit

Este proyecto ahora es una aplicación de Streamlit para comparar los algoritmos de búsqueda:
- DFS iterativo
- DFS recursivo
- BFS

## Uso local

1. Crea y activa tu entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la app:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Abre la URL que Streamlit muestre en la terminal.

## Cómo desplegar en Streamlit

1. Sube el repositorio a GitHub.
2. Crea una nueva app en Streamlit Community Cloud.
3. Selecciona este repositorio y el archivo `streamlit_app.py`.
4. Streamlit instalará las dependencias desde `requirements.txt` y lanzará la app automáticamente.

## Estructura relevante

- `streamlit_app.py`: interfaz principal de Streamlit.
- `busqueda/logic.py`: lógica de búsqueda y algoritmos.
- `requirements.txt`: dependencias del proyecto.

## Notas

- Los archivos de Django y configuración de Render se han eliminado para simplificar el proyecto a Streamlit.
- El estado inicial y el estado objetivo deben ingresarse como una lista de valores separados por espacios.
