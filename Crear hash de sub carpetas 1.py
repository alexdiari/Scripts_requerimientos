import os, hashlib
import pandas as pd
from pathlib import Path
from glob import glob
import codecs
import datetime as dt
import time



current_dir = r"C:\Users\josea.gonzalez\Documents\CONTRALORIA\CONSULTAS\RUES\2024IE0117882\x"
df2 = pd.DataFrame()
p_files = []

def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            p_files.append(d)
            #print(d)
            listdirs(d)
    return p_files


for dirs in listdirs(current_dir):
    
    print(dirs)
    for f in os.listdir(dirs):
        
        #p_files.append(os.path.join(root, subdir))
        current_file = os.path.join(dirs,f)
        file_name = os.path.basename(current_file)
        mod_time = time.ctime(os.path.getmtime(current_file))
        c_time = time.ctime(os.path.getctime(current_file))
        a_time = dt.date.fromtimestamp(os.stat(current_file).st_atime).strftime('%d/%m/%Y %H:%M:%S')
        f_size = os.path.getsize(current_file)
        f_extension = Path(file_name).suffix
        
        H = hashlib.md5()
        A = hashlib.sha1()
        S = hashlib.sha256()
        h = hashlib.sha512()
        
        # open file for reading in binary mode
        with open(current_file,'rb') as file:
    
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read()
                H.update(chunk)
                A.update(chunk)
                S.update(chunk)
                h.update(chunk)
        
        dict = {"Filename" : [f], "MD5" : [H.hexdigest()], "SHA1" : [A.hexdigest()], "SHA-256" : [S.hexdigest()], "SHA-512" : [h.hexdigest()],
                "Full Path" : [current_file], "Modified Time" : [mod_time], "Created Time" : [c_time],
                "Entry Modified Time" : [a_time], "File Size" : [f_size], "File Version" : [''], "Product Version" : [''],
                "Identical" : [''], "Extension" : [f_extension], "File Attributes" : ['A']}
        
        df = pd.DataFrame(dict)
                
        df2 = pd.concat([df, df2], ignore_index=True)

    df2.to_html(dirs + '\\Hash_List.html', border= "1", table_id= "Hash List")
    df2.drop(df2.index, inplace=True)

