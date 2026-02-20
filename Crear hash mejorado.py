
import os
import hashlib
import pandas as pd
from pathlib import Path
import time
import datetime as dt

current_dir = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\209\19 de mayo de 2025_209"

def listdirs(rootdir):
    """Lista todos los subdirectorios en el directorio dado."""
    p_files = []
    for dirpath, dirnames, filenames in os.walk(rootdir):
        p_files.append(dirpath)
    return p_files

# Crear un DataFrame vacío para almacenar los resultados
df2 = pd.DataFrame()

# Recorre todos los directorios
for dirs in listdirs(current_dir):
    print(f"Procesando directorio: {dirs}")
    
    # Procesa cada archivo en el directorio
    for f in os.listdir(dirs):
        current_file = os.path.join(dirs, f)
        
        # Asegúrate de que es un archivo
        if os.path.isfile(current_file):
            print(f"Procesando archivo: {current_file}")
            mod_time = time.ctime(os.path.getmtime(current_file))
            c_time = time.ctime(os.path.getctime(current_file))
            a_time = dt.datetime.fromtimestamp(os.stat(current_file).st_atime).strftime('%d/%m/%Y %H:%M:%S')
            f_size = os.path.getsize(current_file)
            f_extension = Path(current_file).suffix
            
            # Inicializa los hash
            H = hashlib.md5()
            A = hashlib.sha1()
            S = hashlib.sha256()
            h = hashlib.sha512()
            
            # Leer el archivo en modo binario
            try:
                with open(current_file, 'rb') as file:
                    while True:
                        chunk = file.read(1024)
                        if not chunk:
                            break
                        H.update(chunk)
                        A.update(chunk)
                        S.update(chunk)
                        h.update(chunk)

                # Agregar datos al DataFrame
                df2 = df2.append({
                    "Filename": f,
                    "MD5": H.hexdigest(),
                    "SHA1": A.hexdigest(),
                    "SHA-256": S.hexdigest(),
                    "SHA-512": h.hexdigest(),
                    "Full Path": current_file,
                    "Modified Time": mod_time,
                    "Created Time": c_time,
                    "Entry Modified Time": a_time,
                    "File Size": f_size,
                    "Extension": f_extension,
                }, ignore_index=True)

            except Exception as e:
                print(f"Error al procesar el archivo {current_file}: {e}")

    # Guardar el DataFrame como HTML
    if not df2.empty:
        output_file = os.path.join(dirs, 'Hash_List.html')
        df2.to_html(output_file, border="1", table_id="Hash List")
        print(f"Lista de hashes guardada en: {output_file}")
        df2 = pd.DataFrame()  # Reiniciar df2 para el siguiente directorio
    else:
        print(f"No se encontraron archivos en: {dirs}")