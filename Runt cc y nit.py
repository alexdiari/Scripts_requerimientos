import os
import pandas as pd
from pathlib import Path

# =============================================================================
# Parámetros
# =============================================================================
path = r'C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\238\RUNT\SIN RUNT_238'
files = Path(path).glob('*.xlsx')

for f in files:
    ruta_escritura = path

    if not os.path.exists(ruta_escritura):
        os.mkdir(ruta_escritura)

    datos = pd.read_excel(f)
    datos = pd.DataFrame(datos)
    datos = datos[["IDENTIFICACION"]]
    datos.columns = ['DOC']
    datos["DOC"] = datos["DOC"].astype(str).str.upper().str.strip()
    datos = datos.drop_duplicates().dropna(axis=0, how='any')

    # Normalización
    for idx in datos.index:
        doc = datos.at[idx, "DOC"]

        # Si no contiene prefijo
        if not doc.startswith(("N,", "C,")):
            if "-" in doc:
                doc = doc.split("-")[0]  # Eliminar sufijos
            doc = doc.replace(" ", "").replace(".", "")
            if len(doc) >= 9:
                datos.at[idx, "DOC"] = f"N,{doc}"
            else:
                datos.at[idx, "DOC"] = f"C,{doc}"
        else:
            # Limpiar si tiene guión
            if "-" in doc:
                doc = doc.split("-")[0]
                datos.at[idx, "DOC"] = doc

    # Eliminar blancos, puntos y ceros inválidos
    datos["DOC"] = datos["DOC"].str.replace(' ', '').str.replace('.', '', regex=False)
    datos = datos[~datos["DOC"].isin(["C,0", "N,0", "0"])]

    # Archivo con prefijos C, y N,
    datos['DOC'].to_csv(os.path.join(ruta_escritura, 'Consolidado_WS_con_tipo_doc_prueba.txt'),
                        mode='a', index=False, header=None, sep=';')

    # Archivo sin prefijos
    datos['DOC_NUM'] = datos['DOC'].str.replace(r'^[CN],', '', regex=True)
    datos['DOC_NUM'].to_csv(os.path.join(ruta_escritura, 'Consolidado_WS_sin_tipo_doc_prueba.txt'),
                            mode='a', index=False, header=None, sep=';')

    # Archivo solo cédulas (sin C,)
    cedulas = datos[datos['DOC'].str.startswith("C,")]
    cedulas['DOC_NUM'].to_csv(os.path.join(ruta_escritura, 'Solo_Cedulas_sin_prefijo.txt'),
                              mode='a', index=False, header=None, sep=';')

    # Archivo solo NITs (sin N,)
    nits = datos[datos['DOC'].str.startswith("N,")]
    nits['DOC_NUM'].to_csv(os.path.join(ruta_escritura, 'Solo_NITs_sin_prefijo.txt'),
                           mode='a', index=False, header=None, sep=';')
