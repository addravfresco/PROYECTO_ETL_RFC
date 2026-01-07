PROYECTO_ETL_RFC/
├── .venv/                  # Entorno virtual
├── .gitignore              # Archivos excluidos de Git
├── data/                   # Directorio de datos
│   ├── Results.csv         # Fuente original
│   └── NuevosRFC.csv       # Resultado del proceso
├── src/                    # Código fuente
│   ├── __init__.py         # Hace que la carpeta sea un paquete
│   ├── globals.py          # Constantes y rutas
│   ├── modules.py          # Funciones de transformación (Polars)
│   └── main.py             # Orquestador principal
├── README.md               # Documentación
└── requirements.txt        # Dependencias del proyecto

# Proyecto ETL: Normalización y Validación de Registros Fiscales (RFC)

## Objetivo
Este proyecto tiene como finalidad automatizar la limpieza, validación y normalización de una base de datos de contribuyentes. El script procesa archivos CSV para asegurar que los RFC cumplan con la estructura oficial del SAT y que las Razones Sociales se transformen en nombres comerciales limpios y estandarizados.

## Estructura del Proyecto
El código sigue una arquitectura modular para facilitar su mantenimiento y escalabilidad:

* **`main.py`**: Orquestador del proyecto. Contiene la secuencia lógica de llamadas a las funciones de limpieza.
* **`modules.py`**: Contiene todas las funciones de transformación de datos (limpieza de símbolos, normalización de texto y validación de RFC).
* **`globals.py`**: Centraliza todas las variables globales, rutas de archivos y expresiones regulares (Regex).
* **`data/`**: Carpeta destinada a los archivos de entrada (`Results.csv`) y salida (`NuevosRFC.csv`).

## Funcionalidades Principales
1.  **Validación de RFC**: Filtrado de registros con longitud incorrecta (12 o 13 caracteres) y eliminación de caracteres no permitidos.
2.  **Limpieza de Razón Social**:
    * Conversión a mayúsculas y eliminación de acentos.
    * Reemplazo de guiones bajos por espacios y eliminación de espacios dobles.
    * **Regex Avanzado**: Eliminación de regímenes legales (S.A. de C.V., S.C., SOFOM, S.P.R. de R.L., etc.).
    * **Limpieza de conectores**: Eliminación de palabras huérfanas al final de la cadena (DE, DEL, LA).
3.  **Integridad de Negocio**: Identificación de discrepancias entre la longitud del RFC y la naturaleza del nombre (Físicas vs. Morales).

## Instalación y Uso
1. Clonar el repositorio.
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
3. Colocar el archivo de origen en data/Results.csv.
4. Ejecutar el proceso:
    python main.py

Tecnologías Utilizadas
Python 3.x

Polars: Biblioteca de procesamiento de datos de alto rendimiento.

Regex: Expresiones regulares para limpieza avanzada de texto.   