# Rutas de archivos
INPUT_PATH = "data/Results.csv"
OUTPUT_PATH = "data/NuevosRFC.csv"

# Expresiones Regulares
RE_LIMPIEZA_RFC = r"[^A-Z0-9&Ñ]"
# Patrones de empresas para validación cruzada
PATRONES_MORALES = (
    r"S\.?A\.?|C\.?V\.?|S\.?C\.?|S\.?R\.?L\.?|A\.?C\.?|S\.?A\.?B\.?|"
    r"ASOCIACION|COOPERATIVA|FUNDACION|INSTITUTO|S DE RL|S A DE CV|SOCIEDAD"
)