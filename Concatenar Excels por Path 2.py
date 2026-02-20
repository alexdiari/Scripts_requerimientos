# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:21:15 2022

@author: danielf.moreno
"""

from pathlib import Path
import pandas as pd

path = r'S:\2.DELEGADAS\UNCOPI\RESPUESTAS RUNTt\Originales\SOLRUNT215_30052025'  # or unix / linux / mac path

# Get the files from the path provided in the OP
files = Path(path).glob('*.xlsx')  # .rglob to get subdirectories

dfs = list()
for f in files:
    data = pd.read_excel(f)
    # .stem is method for pathlib objects to get the filename w/o the extension
    data['Archivo Origen'] = f.stem
    dfs.append(data)

df = pd.concat(dfs, ignore_index=True)
df["IDENTIFICACION"] = df["IDENTIFICACION"].str.replace("C,","")
df["IDENTIFICACION"] = df["IDENTIFICACION"].str.replace("N,","")
df = df.drop(['ITEM'], axis=1)

"""
df.head()
print(df.columns)
print(df)
"""

df.to_excel(r'S:\2.DELEGADAS\UNCOPI\RESPUESTAS RUNTt\Originales\SOLRUNT215_30052025\SOLRUNT215_30052025.xlsx', index=False)



