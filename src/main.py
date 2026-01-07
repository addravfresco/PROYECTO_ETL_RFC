import polars as pl
from src.globals import INPUT_PATH, OUTPUT_PATH
import src.modules as mod

def main():
    print("🚀 Iniciando ETL de Normalización Fiscal...")

    # 1. Extracción
    try:
        df = pl.read_csv(INPUT_PATH)
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")
        return

    # 2. Transformación (Pipeline)
    df_final = (
        df.pipe(mod.validar_y_limpiar_rfc)
          .pipe(mod.aplicar_integridad_negocio)
          .pipe(mod.normalizar_razon_social)
          # Deduplicación: Si el RFC se repite, nos quedamos con el nombre más largo
          .with_columns(pl.col("Nombre_Limpio").str.len_chars().alias("temp_len"))
          .sort("temp_len", descending=True)
          .unique(subset=["RFC_Limpio"], keep="first")
          .select(["RFC_Limpio", "Nombre_Limpio"])
          .sort("RFC_Limpio")
    )

    # 3. Carga
    df_final.write_csv(OUTPUT_PATH)
    print(f"✅ ETL finalizado con éxito.")
    print(f"📁 Archivo generado: {OUTPUT_PATH}")
    print(f"📝 Registros procesados: {df_final.height}")

if __name__ == "__main__":
    main()