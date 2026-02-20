import os
import shutil

def move_files(ruta_base):
    # Obtener una lista de carpetas en la ruta base
    carpetas = [carpeta for carpeta in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, carpeta))]

    # Obtener una lista de archivos en la ruta base
    archivos = [archivo for archivo in os.listdir(ruta_base) if os.path.isfile(os.path.join(ruta_base, archivo))]

    # Procesar cada archivo
    for archivo in archivos:
        # Extraer la parte del nombre base del archivo (sin extensión ni sufijo "_RUNT")
        nombre_base = archivo.split("_")[0].split(".")[0]  # Esto captura algo como "2024IE0136712"
        
        # Buscar la carpeta que contiene el nombre base
        carpeta_destino = next((carpeta for carpeta in carpetas if nombre_base in carpeta), None)
        
        if carpeta_destino:
            # Construir la ruta completa del archivo y la carpeta destino
            ruta_archivo = os.path.join(ruta_base, archivo)
            ruta_destino = os.path.join(ruta_base, carpeta_destino, archivo)
            
            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_archivo, ruta_destino)
            print(f"Archivo {archivo} movido a {carpeta_destino}")
        else:
            print(f"No se encontró carpeta para el archivo {archivo}")

    print("Proceso completado.")

# Ruta base donde están los archivos y carpetas
ruta_base = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\240\1 de agosto de 2025_240"  # Cambia esto a la ruta donde tienes los archivos y carpetas
move_files(ruta_base)
