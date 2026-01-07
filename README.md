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