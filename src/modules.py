import polars as pl
from src.globals import RE_LIMPIEZA_RFC, PATRONES_MORALES

def validar_y_limpiar_rfc(df: pl.DataFrame) -> pl.DataFrame:
    """
    Limpia y filtra RFCs eliminando falsos positivos (ceros, basura numérica).
    """
    return (
        df.with_columns(
            pl.col("RFC")
            .cast(pl.Utf8)
            .str.to_uppercase()
            .str.replace_all(RE_LIMPIEZA_RFC, "")
            .alias("RFC_Limpio")
        )
        # 1. Filtro de Longitud Técnica (12 o 13)
        .filter(pl.col("RFC_Limpio").str.len_chars().is_in([12, 13]))
        
        # 2. Filtro de Estructura Básica:
        # Debe empezar con 3 o 4 letras (A-Z, &, Ñ) seguidas de al menos un número.
        # Esto elimina de golpe los "0000000000"
        .filter(pl.col("RFC_Limpio").str.contains(r"^[A-Z&Ñ]{3,4}[0-9]"))
    )

def filtrar_registros_vacios(df: pl.DataFrame) -> pl.DataFrame:
    """Elimina filas donde la Razon_Social sea nula, esté vacía o solo tenga espacios."""
    return df.filter(
        (pl.col("Razon_Social").is_not_null()) & 
        (pl.col("Razon_Social").str.strip_chars() != "")
    )

def limpiar_puntos_finales(df: pl.DataFrame) -> pl.DataFrame:
    """Regla: Si la Razón Social termina en punto, se elimina dicho punto."""
    return df.with_columns(
        pl.col("Razon_Social")
        .str.replace(r"\.$", "") 
        .alias("Razon_Social")
    )

def aplicar_integridad_negocio(df: pl.DataFrame) -> pl.DataFrame:
    """
    Reglas de Integridad:
    1. RFC 13 + Siglas de Empresa (S.A., C.V., etc.) -> ELIMINAR.
    2. RFC 13 + Punto (.) en Razón Social -> ELIMINAR.
    """
    return df.filter(
        ~(
            (pl.col("RFC_Limpio").str.len_chars() == 13) & 
            (
                (pl.col("Razon_Social").str.to_uppercase().str.contains(PATRONES_MORALES)) |
                (pl.col("Razon_Social").str.contains(r"\.")) 
            )
        )
    )

def normalizar_razon_social(df: pl.DataFrame) -> pl.DataFrame:
    """Normalización de nombres para reporte en Excel."""
    return df.with_columns(
        pl.col("Razon_Social")
        .cast(pl.Utf8)
        .str.to_uppercase()
        .str.replace_all("_", " ")
        .str.replace_all(r"\s+", " ")
        .str.strip_chars()
        .alias("Nombre_Limpio")
    )