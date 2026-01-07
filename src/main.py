import polars as pl
from src.globals import INPUT_PATH, OUTPUT_PATH
import src.modules as mod

def main():
    print(" Iniciando...")

    try:
        df = pl.read_csv(INPUT_PATH)
        
        # Procesamiento
        df_final = (
            df.pipe(mod.validar_y_limpiar_rfc)
              .pipe(mod.filtrar_registros_vacios)
              .pipe(mod.limpiar_simbolos)
              .pipe(mod.quitar_regimen_legal)
              .pipe(mod.limpiar_conectores_finales)
              .pipe(mod.limpiar_puntos_finales)
              .pipe(mod.aplicar_integridad_negocio)
              .pipe(mod.normalizar_razon_social)
              .select(["RFC_Limpio", "Nombre_Limpio"])
              .sort("RFC_Limpio")
              .filter(pl.col("Nombre_Limpio") != "")
        )

        # CARGA OPTIMIZADA PARA EXCEL:
        df_final.write_csv(OUTPUT_PATH, include_bom=True, separator=",")
        
        print(f" Proceso finalizado. Registros totales: {df_final.height}")
        print(f" Guardado en: {OUTPUT_PATH}")

    except Exception as e:
        print(f" Error en el proceso: {e}")

if __name__ == "__main__":
    main()