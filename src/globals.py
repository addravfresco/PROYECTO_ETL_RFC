# globals.py

# Rutas de archivos
INPUT_PATH = "data/Results.csv"
OUTPUT_PATH = "data/NuevosRFC.csv"
AUDIT_PATH = "data/Auditoria_Limpieza_Nombres.csv"

# Expresiones Regulares
RE_LIMPIEZA_RFC = r"[^A-Z0-9&Ñ]"


PATRONES_MORALES = (
    r"S\.?A\.?|C\.?V\.?|S\.?C\.?|S\.?R\.?L\.?|A\.?C\.?|S\.?A\.?B\.?|S\.?A\.?P\.?I\.?|"
    r"ASOCIACION|COOPERATIVA|FUNDACION|INSTITUTO|S\s?DE\s?RL|SOCIEDAD|SOFOM|UNIV|COLEGIO|"
    r"CONSTRUCC|INMOBILIARI|MEXICO|SERVICIOS|SOLUCIONES|GRUPO|CORP"
)


REGIMENES_LEGALES = [
    r"\bS\.?\s?DE\s?R\.?\s?L\.?\s?DE\s?C\.?\s?V\.?\b",
    r"\bSOCIEDAD\sANONIMA\sDE\sCAPITAL\sVARIABLE\b",
    r"\bSOCIEDAD\sDE\sRESPONSABILIDAD\sLIMITADA\b",
    r"\bSOFOM\s?E\.?N\.?R\.?\b",
    r"\bS\.?\s?A\.?\s?P\.?\s?I\.?\s?DE\s?C\.?\s?V\.?\b",
    r"\bS\.?\s?P\.?\s?R\.?\s?DE\s?R\.?\s?L\.?\b",
    r"\bS\.?\s?A\.?\s?B\.?\s?DE\s?C\.?\s?V\.?\b", 
    r"\bS\.?\s?A\.?\s?DE\s?C\.?\s?V\.?\b",
    r"\bS\.?\s?A\.?\s?P\.?\s?I\.?\b",
    r"\bS\.?\s?A\.?\b", r"\bC\.?\s?V\.?\b", r"\bS\.?\s?C\.?\b",
    r"\bA\.?\s?C\.?\b", r"\bS\.?\s?R\.?\s?L\.?\b", r"\bE\.?\s?N\.?\s?R\.?\b"
]