# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:48:08 2025

@author: josea.gonzalez
"""

from pathlib import Path

def get_folder_size(folder_path):
    """Calcula el tamaño total de una carpeta en bytes."""
    folder = Path(folder_path)
    return sum(f.stat().st_size for f in folder.rglob('*') if f.is_file())

def list_folders_sizes(main_folder):
    """Muestra el tamaño de cada subcarpeta dentro de la carpeta principal."""
    main_path = Path(main_folder)
    
    if not main_path.exists():
        print(f"❌ La carpeta {main_folder} no existe.")
        return

    print(f"\n📂 Tamaño de cada subcarpeta en {main_folder}:\n")
    
    for subfolder in main_path.iterdir():
        if subfolder.is_dir():  # Solo analiza carpetas
            size_in_bytes = get_folder_size(subfolder)
            size_in_mb = size_in_bytes / (1024 * 1024)  # Convertir a MB
            size_in_gb = size_in_bytes / (1024 * 1024 * 1024)  # Convertir a GB
            print(f"  📁 {subfolder.name}: {size_in_mb:.2f} MB ({size_in_gb:.2f} GB)")

# Ruta de la carpeta principal
main_folder = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\207_\207_B\14 de mayo de 2025_207_B"

# Ejecutar la función
list_folders_sizes(main_folder)
