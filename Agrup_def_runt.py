# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 07:59:30 2025

@author: josea.gonzalez
"""

import os
import shutil

# Ruta base donde están las carpetas _RUNT
ruta_base = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\220\13 de junio de 2025_220"

# Crear carpeta destino
ruta_destino = os.path.join(ruta_base, "RUNT_AGRUPADOS")
os.makedirs(ruta_destino, exist_ok=True)

carpetas_movid_as = 0

# Buscar carpetas que terminan en _RUNT (sin incluir la carpeta destino)
for nombre in os.listdir(ruta_base):
    carpeta_origen = os.path.join(ruta_base, nombre)

    if os.path.isdir(carpeta_origen) and nombre.endswith("_RUNT") and nombre != "RUNT_AGRUPADOS":
        nueva_ubicacion = os.path.join(ruta_destino, nombre)

        # Mover carpeta completa
        shutil.move(carpeta_origen, nueva_ubicacion)
        print(f"📁 Movida: {nombre} -> RUNT_AGRUPADOS/")
        carpetas_movid_as += 1

if carpetas_movid_as == 0:
    print("❌ No se encontraron carpetas que terminen en '_RUNT'.")
else:
    print(f"\n✅ Se movieron {carpetas_movid_as} carpetas a 'RUNT_AGRUPADOS'.")

