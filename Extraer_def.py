# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 07:49:50 2025

@author: josea.gonzalez
"""

import os
import shutil

# Ruta principal donde buscar
ruta_base = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\220\13 de junio de 2025_220"

# Extensiones válidas de Excel
extensiones_excel = ['.xlsx', '.xls', '.xlsm']

archivos_encontrados = 0

# Recorrer subdirectorios y archivos
for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base):
    for archivo in archivos:
        nombre_sin_ext, extension = os.path.splitext(archivo)

        # Verificar que termina en _RUNT y que es un archivo Excel
        if nombre_sin_ext.endswith("_RUNT") and extension.lower() in extensiones_excel:
            ruta_archivo = os.path.join(carpeta_actual, archivo)

            # Carpeta contenedora original
            nombre_carpeta_original = os.path.basename(carpeta_actual)

            # Carpeta destino: misma ubicación que la original + "_RUNT"
            carpeta_destino = os.path.join(os.path.dirname(carpeta_actual), f"{nombre_carpeta_original}_RUNT")
            os.makedirs(carpeta_destino, exist_ok=True)

            # Copiar archivo al nuevo directorio
            ruta_destino = os.path.join(carpeta_destino, archivo)
            shutil.copy2(ruta_archivo, ruta_destino)

            print(f"✅ Copiado: {ruta_archivo} -> {ruta_destino}")
            archivos_encontrados += 1

if archivos_encontrados == 0:
    print("❌ No se encontraron archivos Excel con terminación '_RUNT'.")
else:
    print(f"\n✅ Proceso completado. Archivos copiados: {archivos_encontrados}")

