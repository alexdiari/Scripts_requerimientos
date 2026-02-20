import os, re
import pandas as pd
from pathlib import Path
from glob import glob
from unidecode import unidecode
import re

# =============================================================================
# Parametros
# =============================================================================
path = r'C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\198_\SIN RUNT\198_C_SIN RUNT'  # or unix / linux / mac path

# Get the files from the path provided in the OP
files = Path(path).glob('*.xlsx')  # .rglob to get subdirectories

for f in files:
    

    ruta_escritura = path#os.path.join(path,nom_solicitud[:len(nom_solicitud)-5]+'_DFML')
      
    if not os.path.exists(ruta_escritura):
        os.mkdir(ruta_escritura)
        
    datos = pd.read_excel(f)
    datos = pd.DataFrame(datos)
    datos = datos[["IDENTIFICACION"]]#datos.drop(columns = ['ITEM','SEGUNDO NOMBRE', 'PRIMER APELLIDO', 'SEGUNDO APELLIDO', 'ACTUACION','PRIMER NOMBRE/RAZON SOCIAL'])
    datos.columns = ['DOC']
    datos["DOC"] = datos["DOC"].str.upper()
    #datos = datos.drop_duplicates().dropna(0,how='any')
    datos = datos.drop_duplicates().dropna(axis=0, how='any')
    for dato in datos["DOC"].index.values.tolist():
        print(dato)
        if ((not "N," in datos["DOC"][dato]) and (not "C," in datos["DOC"][dato])) == True:
            #print("FLAG 1")
            if len(datos["DOC"][dato]) == 9 and (datos["DOC"][dato] == 8 or datos["DOC"][dato] == 9):
                datos["DOC"][dato] = "N," + datos["DOC"][dato]
            elif datos["DOC"][dato][1] != ",":
                datos["DOC"][dato][1] = ","
                datos["DOC"][dato] = "N," + datos["DOC"][dato]
            elif "-" in datos["DOC"][dato]:
                if datos["DOC"][dato][datos["DOC"][dato].find('-') + 1].isnumeric() != True:
                    datos["DOC"][dato] = datos["DOC"][dato][:len(datos["DOC"][dato])-1]
                else:
                    datos["DOC"][dato] = datos["DOC"][dato][:len(datos["DOC"][dato])-2]
                datos["DOC"][dato] = "N," + datos["DOC"][dato]
        elif "-" in datos["DOC"][dato]:
            if datos["DOC"][dato][datos["DOC"][dato].find('-') + 1].isnumeric() != True:
                datos["DOC"][dato] = datos["DOC"][dato][:len(datos["DOC"][dato])-1]
            else:
                datos["DOC"][dato] = datos["DOC"][dato][:len(datos["DOC"][dato])-2]
        elif datos["DOC"][dato][1] != ",":
            datos["DOC"][dato][1] = ","
       
        if datos['DOC'][dato] == 0 or datos['DOC'][dato] == 'C,0' or datos['DOC'][dato] == 'N,0':
            datos["DOC"][dato].drop()
    
    datos["DOC"] = datos["DOC"].str.replace(' ',"")
    datos["DOC"] = datos["DOC"].str.replace('.',"")
    datos['DOC'].to_csv(os.path.join(ruta_escritura,'Consolidado_WS_con_tipo_doc_prueba.txt'),mode = 'a',index=False,header = None, sep = ';')#f_{nom_solicitud} , quoting=csv.QUOTE_NONE
    
    datos["DOC"] = datos["DOC"].str.replace('(\D+)',"")
        
    datos['DOC'].to_csv(os.path.join(ruta_escritura,'Consolidado_WS_sin_tipo_doc_prueba.txt'),mode = 'a',index=False,header = None, sep = ';')#f_{nom_solicitud} , quoting=csv.QUOTE_NONE
    

