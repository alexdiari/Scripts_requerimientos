# -*- coding: utf-8 -*-
"""
@author: josea.gonzalez
"""

import pandas as pd
import os

# Ruta principal
ruta_principal = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2026\UNCOPI FEBRERO\334\18 de febrero de 2026_334"

# Palabras clave para filtrar
palabras_clave = ["CATASTRO", "SUPERNOTARIADO"]

# Recorre subcarpetas
for carpeta, _, archivos in os.walk(ruta_principal):
    for archivo in archivos:
        if archivo.lower().endswith(".csv") and any(palabra.lower() in archivo.lower() for palabra in palabras_clave):
            ruta_csv = os.path.join(carpeta, archivo)

            try:
                # Intentar primero con coma
                try:
                    df = pd.read_csv(ruta_csv, encoding="utf-8", sep=",", engine="python", error_bad_lines=False)
                except Exception:
                    df = pd.read_csv(ruta_csv, encoding="utf-8", sep="|", engine="python", error_bad_lines=False)

                # Si quedó en una sola columna, reintentar con pipe
                if df.shape[1] == 1:
                    df = pd.read_csv(ruta_csv, encoding="utf-8", sep="|", engine="python", error_bad_lines=False)

                # Guardar como Excel
                nombre_excel = archivo.replace(".csv", ".xlsx")
                ruta_excel = os.path.join(carpeta, nombre_excel)
                df.to_excel(ruta_excel, index=False)

                print(f"✅ Convertido: {ruta_csv} → {ruta_excel}")

                # Eliminar CSV original
                os.remove(ruta_csv)
                print(f"🗑️ Eliminado: {ruta_csv}")

            except Exception as e:
                print(f"⚠️ Error al procesar {ruta_csv}: {e}")
