import polars as pl
import re
from src.globals import RE_LIMPIEZA_RFC, PATRONES_MORALES

def validar_y_limpiar_rfc(df: pl.DataFrame) -> pl.DataFrame:
    """Aplica limpieza de caracteres y filtro de longitud técnica."""
    return (
        df.with_columns(
            pl.col("RFC")
            .str.to_uppercase()
            .str.replace_all(RE_LIMPIEZA_RFC, "")
            .alias("RFC_Limpio")
        )
        # Regla: Solo RFCs de 12 o 13 caracteres son válidos
        .filter(pl.col("RFC_Limpio").str.len_chars().is_in([12, 13]))
    )

def aplicar_integridad_negocio(df: pl.DataFrame) -> pl.DataFrame:
    """Regla: Si RFC mide 13 pero el nombre tiene siglas de empresa, se elimina."""
    return df.filter(
        ~(
            (pl.col("RFC_Limpio").str.len_chars() == 13) & 
            (pl.col("Razon_Social").str.to_uppercase().str.contains(PATRONES_MORALES))
        )
    )

def normalizar_razon_social(df: pl.DataFrame) -> pl.DataFrame:
    """Genera Nombre_Limpio con mayúsculas, sin guiones bajos y sin espacios dobles."""
    return df.with_columns(
        pl.col("Razon_Social")
        .str.to_uppercase()
        .str.replace_all("_", " ")
        .str.replace_all(r"\s+", " ")
        .str.strip_chars()
        .alias("Nombre_Limpio")
    )