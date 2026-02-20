# =============================================================================
# Paquetes
# =============================================================================
import os, re
import pandas as pd
from glob import glob
from unidecode import unidecode
from time import time
from datetime import datetime
from sqlalchemy import create_engine
from pathlib import Path
# =============================================================================
# Conexión a BD 
# =============================================================================



engine_SNC = create_engine(
    'mssql+pyodbc://@sqlsrv-diari-ui-trv-ws.database.windows.net:1433/db-diari-ui-trv-ws-supernotariado'
    '?driver=ODBC+Driver+17+for+SQL+Server'
    '&authentication=ActiveDirectoryIntegrated'
)

engine_CAT = create_engine(
    'mssql+pyodbc://@sqlsrv-diari-ui-trv-ws.database.windows.net:1433/db-diari-ui-trv-ws-catastro'
    '?driver=ODBC+Driver+17+for+SQL+Server'
    '&authentication=ActiveDirectoryIntegrated'
)

engine_DAFP = create_engine('mssql+pyodbc://{server}:{port}/{db}?driver={dvr}&{auth}'
                          .format(server = '192.168.24.168',
                                  port = '1433',
                                  db = 'GPIF_DAFP',
                                  dvr = 'ODBC+Driver+17+for+SQL+Server',
                                  auth = 'trusted_connection=yes'))

engine_RUES = create_engine(
    'mssql+pyodbc://@sqlsrv-diari-ui-trv-ws.database.windows.net:1433/db-diari-ui-trv-ws-rues'
    '?driver=ODBC+Driver+17+for+SQL+Server'
    '&authentication=ActiveDirectoryIntegrated'
)






# =============================================================================
# Parametros
# =============================================================================0


path = r'C:\Users\josea.gonzalez\Documents\CONTRALORIA\UNCOPI\UNCOPI 2025\UNCOPI_SEPTIEMBRE\261\17 de septiembre de 2025_261' 

start_id =21409
#id inicial del paquete de uncopi en el inventario

RUES = True
DAFP = False
SUPERNOT = True
CATASTRO = True
PILA = False

# =============================================================================
# Script (No modificar)
# =============================================================================

files = glob(os.path.join(path,'*.xlsx'))  # .rglob to get subdirectories
appended_anotac = pd.DataFrame()
appended_propiet = pd.DataFrame()
appended_dafp = pd.DataFrame()
appended_cat = pd.DataFrame()
appended_rues = pd.DataFrame()
appended_pi = pd.DataFrame()

for f in files:
    base_name = os.path.basename(f).replace(".xlsx", "")
    if "RUNT" not in base_name:
        data = pd.read_excel(f)
        #print(data["IDENTIFICACIÓN"])
        data = data[["IDENTIFICACION"]]
        data["IDENTIFICACION"] = data["IDENTIFICACION"].astype(str)
        data["IDENTIFICACION"] = data["IDENTIFICACION"].str.replace('(\D+)',"")
        #data["IDENTIFICACIÓN"] = data["IDENTIFICACIÓN"].str.replace("N,","")
        #data["IDENTIFICACIÓN"] = data["IDENTIFICACIÓN"].str.replace(" ","")
        #data["IDENTIFICACIÓN"] = data["IDENTIFICACIÓN"].str.replace(".","")
        #data['IDENTIFICACIÓN'] = data['IDENTIFICACIÓN'].astype(float)
        data.rename(columns = {'IDENTIFICACION': 'IDENTIFICACION'}, inplace = True)
        
    
        
        
        if not os.path.exists(os.path.join(path, str(start_id) + '_' + base_name)):
                os.mkdir(os.path.join(path, str(start_id) + '_' + base_name))
         
        if SUPERNOT == True:
        
              for CC in data["IDENTIFICACION"]:
                  consulta_anotaciones = f'''select 
                 db.[tipodocidentcons]
          		,db.[identifconsultada] AS IDENTIFICACION
          		,db.[novedad]
          		,db.[idjurisdiccion]
          		,db.[jurisdiccion]
          		,db.[matricula]
          		,db.[chip]
          		,db.[cedulacatastral]
          		,db.[direccion]
          		,ac.[numeroanotacion]
          		,ac.[fechaanotacion]
          		,ac.[radicacionanotacion]
          		,ac.[nomdocumentoanotacionfolio]
          		,ac.[cantidadmonetaria]
          		,ac.[codnaturalezajuridicafolio]
          		,ac.[nomnaturalezajuridicafolio]
          		,ac.[comentario]
          		,ac.[grupo]
          		,pc.[razonsocial] as razonsocial_persona_cede
          		,pc.[numidtributaria] as numidtributaria_persona_cede
          		,pr.[primerapellido] as primerapellido_persona_recibe
          		,pr.[segundoapellido] as segundoapellido_persona_recibe
          		,pr.[primernombre] as primernombre_persona_recibe
          		,pr.[segundonombre] as segundonombre_persona_recibe
          		,pr.[codtipoidentificacion] as codtipoidentificacion_persona_recibe
          		,pr.[numerocedulaciudadania] as numerocedulaciudadania_persona_recibe
          		,pr.[espropietario] as espropietario_persona_recibe
          		,pr.[anotacioncertificadoid] as anotacioncertificadoid_persona_recibe
          		,pr.[tipopersona] as tipopersona_persona_recibe
          		,pr.[numidtributaria] as numidtributaria_persona_recibe
          		,pr.[razonsocial] as razonsocial_persona_recibe
          		,pr.[porcentajeparticipacion] as porcentajeparticipacion_persona_recibe
          		,db.[consecconsestjuridicologsupernot]
          		,db.[fechaconsestjuridicologsupernot]
          		,db.[departamentopredio]
          		,db.[municipiopredio]
          		,db.[estadomatricula]
          		,db.[numeropropietarios]
          		,db.[persrecibeprediocodtipoidentificacion]
          		,db.[persrecibepredionumeroidentificacion]
          		,db.[persrecibepredioprimerapellido]
          		,db.[persrecibeprediosegundoapellido]
          		,db.[persrecibepredioprimernombre]
          		,db.[persrecibeprediosegundonombre]
          		,db.[persrecibepredionumidtributaria]
          		,db.[persrecibeprediorazonsocial]
          		,db.[persrecibepredioespropietario]
          		,ac.[coddocumentoanotacionfolio]
          		,ac.[fechadocumentoanotacion]
          		,ac.[entidadanotacion]
          		,ac.[comentarioespecificaanotacionfolio]
          		,ac.[nombremunicipioanotacion]
          		,ac.[validez]
          		,ac.[codtipomoneda]
          		,pc.[anotacioncertificadoid] as anotacioncertificadoid_persona_cede
          		,pc.[tipopersona] as tipopersona_persona_cede
          		,pc.[espropietario] as espropietario_persona_cede
          		,pc.[numerocedulaciudadania] as numerocedulaciudadania_persona_cede
          		,pc.[codtipoidentificacion] as codtipoidentificacion_persona_cede
          		,pc.[primerapellido] as primerapellido_persona_cede
          		,pc.[primernombre] as primernombre_persona_cede
          		,pc.[segundoapellido] as segundoapellido_persona_cede
          		,pc.[segundonombre] as segundonombre_persona_cede
          		,pc.[porcentajeparticipacion] as porcentajeparticipacion_persona_cede
          		from [dbo].[matriculas_datosbasicos] db
          		left join matricula_anotacioncertificado ac on db.id = ac.idmatriculadatosbasicosid
          		left join anotacioncertificado_persona_cede pc on ac.id = pc.anotacioncertificadoid
          		left join anotacioncertificado_persona_recibe pr on ac.id = pr.anotacioncertificadoid
          		where db.IdentifConsultada = '{CC}'
                  ''' # and db.FECHA_CORTE in (SELECT MAX(db.FECHA_CORTE) FROM [db-diari-ui-trv-ws-supernotariado].[dbo].[Matriculas_DatosBasicos] db where db.IdentifConsultada = '{CC}')
                  
                  consulta_propietarios = f'''
                  SELECT db.idLogConsulta, db.id, db.IdentifConsultada AS IDENTIFICACION, db.IdJurisdiccion ,db.Matricula, db.novedad, db.Direccion, db.Chip, db.CedulaCatastral,
                  mp.TipoPersona, mp.NumeroCedulaCiudadania, mp.NumIdTributaria, mp.EsPropietario, mp.RazonSocial, mp.PrimerApellido, mp.SegundoApellido, mp.PrimerNombre, mp.SegundoNombre
                  FROM [dbo].[Matriculas_DatosBasicos] db
                  left join Matricula_Propietarios_Actuales mp on db.id = mp.MatriculaDatosBasicosid
                  where db.IdentifConsultada = '{CC}'
                  ''' #  and db.FECHA_CORTE in (SELECT MAX(db.FECHA_CORTE) FROM [dbo].[Matriculas_DatosBasicos] db where db.IdentifConsultada = '{CC}')
              
                  anotaciones = pd.read_sql(consulta_anotaciones,engine_SNC)
                  appended_anotac = appended_anotac.append(anotaciones)
                  appended_anotac['IDENTIFICACION'] = appended_anotac['IDENTIFICACION'].astype(str)
                  propietarios = pd.read_sql(consulta_propietarios,engine_SNC)
                  appended_propiet = appended_propiet.append(propietarios)
                  appended_propiet['IDENTIFICACION'] = appended_propiet['IDENTIFICACION'].astype(str)
                  print(f)
                  print(CC)
                  print(appended_anotac)
              
              df_Merge1 = pd.merge(data["IDENTIFICACION"], appended_anotac, on = 'IDENTIFICACION', how = 'left')
              df_Merge2 = pd.merge(data["IDENTIFICACION"], appended_propiet, on = 'IDENTIFICACION', how = 'left')
              
              df_Merge1 = df_Merge1.applymap(lambda x: str(x).replace('|', '') if isinstance(x, str) else x)
              df_Merge2 = df_Merge2.applymap(lambda x: str(x).replace('|', '') if isinstance(x, str) else x)
              
              df_Merge1.to_csv(os.path.join(path, str(start_id) + '_' + base_name, f'{base_name}_SUPERNOTARIADO_anotaciones.csv'), sep='|', index=False)
              df_Merge2.to_csv(os.path.join(path, str(start_id) + '_' + base_name, f'{base_name}_SUPERNOTARIADO_propietarios_propiedades.csv'), sep='|', index=False)
        
        if CATASTRO == True:
            
            for CC in data["IDENTIFICACION"]:
                consulta_cat = f'''
                select pr.idLogConsulta, pr.identifConsultada AS IDENTIFICACION, pr.matricula, pr.direccion_real,pr.chip,
                pro.numero_identificacion, pro.nombre_propietario, pro.primer_apellido, pro.segundo_apellido,av.avaluo_ano,av.valor_avaluo
                from  (Predio pr
                left join Propietario pro on pr.id = pro.Predioid) left join Avaluo av on av.Predioid = pr.id 
                where pr.IdentifConsultada = '{CC}'
                order by pr.id,av.avaluo_ano asc
                '''
            
                catastro = pd.read_sql(consulta_cat,engine_CAT)
                appended_cat = appended_cat.append(catastro)
                
            df_Merge4 = pd.merge(data["IDENTIFICACION"], appended_cat, on = 'IDENTIFICACION', how = 'left')
            df_Merge4.to_csv(os.path.join(path, str(start_id) + '_' + base_name, f'{base_name}_CATASTRO.csv') , index=False)
                
    
        
            
        if RUES == True:
            
            for CC in data["IDENTIFICACION"]:
                
                query_rues = f'''SELECT
                    [identConsultada] AS IDENTIFICACION
                	,[digito_verificacion] AS DIGITO_VERIFICACION
                	,[razon_social] AS NOMBRE_ENTIDAD
                	,[organizacion_juridica] AS ORGANIZACION_JURIDICA
                	,[codigo_tipo_sociedad] AS COD_TIPO_SOCIEDAD
                	,[tipo_sociedad] AS TIPO_SOCIEDAD
                	,[estado_matricula] AS ESTADO_MATRICULA
                	,[fecha_actualizacion_rues] AS FECHA_ACTUALIZACION_RUES
                	,[fecha_cancelacion] AS FECHA_CANCELACION
                	,[fecha_matricula] AS FECHA_MATRICULA
                	,[fecha_renovacion] AS FECHA_RENOVACION
                	,[ultimo_ano_renovado] AS [ULTIMO_AÑO_RENOVADO]
                	,[cod_ciiu_act_econ_pri] AS COD_CIIU_PRINC
                	,[desc_ciiu_act_econ_pri] AS DES_CIIU_PRINC
                	,[cod_ciiu_act_econ_sec] AS COD_CIIU_SEC
                	,[desc_ciiu_act_econ_sec] AS DES_CIIU_SEC
                	,[ciiu3] AS COD_CIIU_TERC
                	,[desc_ciiu3] AS DES_CIIU_TERC
                	,[tipo_identificacion] AS TIPO_ID_INTEGRANTE
                	,[dpto_comercial] AS DEPARTAMENTO_COM
                	,[municipio_comercial] AS MUNICIPIO_COM
                	,[direccion_comercial] AS DIRECCION_COM
                	,[telefono_comercial_1] AS TELEFONO_COM_1
                	,[telefono_comercial_2] AS TELEFONO_COM_2
                	,[telefono_comercial_3] AS TELEFONO_COM_3
                	,[correo_electronico_comercial] AS CORREO_ELECTRONICO_COMERCIAL
                	,[dpto_fiscal] AS DEPARTAMENTO_FISCAL
                	,[municipio_fiscal] AS MUNICIPIO_FISCAL
                	,[zona_fiscal] AS barrio_fiscal
                	,[direccion_fiscal] AS DIRECCION_FISCAL
                	,[telefono_fiscal_1] AS TELEFONO_FISCAL_1
                	,[telefono_fiscal_2] AS TELEFONO_FISCAL_2
                	,[telefono_fiscal_3] AS TELEFONO_FISCAL_3
                	,[correo_electronico_fiscal] AS CORREO_ELECTRONICO_FISCAL
                	,[idLogConsulta]
                    FROM [dbo].[RuesConsNitDatosBasicosBD]
                    where identConsultada = '{CC}'
                    '''
                
                consulta_RUES = pd.read_sql(query_rues, engine_RUES)
                appended_rues = appended_rues.append(consulta_RUES)
                appended_rues['IDENTIFICACION'] = appended_rues['IDENTIFICACION'].astype(str)
                
            df_Merge4 = pd.merge(data["IDENTIFICACION"], appended_rues, on = 'IDENTIFICACION', how = 'left')
            df_Merge4.to_excel(os.path.join(path, str(start_id) + '_' + base_name, f'{base_name}_RUES.xlsx') , index=False)
            
               
        if DAFP == True:
            
            for CC in data["IDENTIFICACION"]:
                
                df_ConsultaVinculaciones = f"""SELECT [ID_INSTITUCION]
                ,[INSTITUCION]
                ,[SECTOR]
                ,[CLASIFICACION_ORGANICA]
                ,[NATURALEZA]
                ,[MUNICIPIO_INSTITUCION]
                ,[DPTO_INSTITUCION]
                ,[TIPO_DOCUMENTO]
                ,[IDENTIFICACION]
                ,[PRIMER_NOMBRE]
                ,[SEGUNDO_NOMBRE]
                ,[PRIMER_APELLIDO]
                ,[SEGUNDO_APELLIDO]
                ,[TELEFONO]
                ,[DIRECCION_DOMICILIO]
                ,[CORREO_ELECTRONICO]
                ,[FECHA_INGRESO]
                ,[NOMBRAMIENTO_VINCULACION]
                ,[NATURALEZA_EMPLEO_ACTUAL]
                ,[NIVEL_JERARQUICO_EMPLEO]
                ,[DENOMINACION_EMPLEO_ACTUAL]
                ,[CODIGO_EMPLEO_ACTUAL]
                ,[GRADO_EMPLEO_ACTUAL]
                ,[DEPENDENCIA_EMPLEO_ACTUAL]
                ,[ASIGNACION_BASICA]
                ,[GASTOS_REPRESENTACION]
                ,[PRIMA_DIRECCION]
                FROM [GPIF_DAFP].[dbo].[ConsultaVinculaciones] db
                where db.IDENTIFICACION = '{CC}'
                """
                
                vinculaciones = pd.read_sql(df_ConsultaVinculaciones,engine_DAFP)
                vinculaciones.drop_duplicates()
                appended_dafp = appended_dafp.append(vinculaciones)
                appended_dafp['IDENTIFICACION'] = appended_dafp['IDENTIFICACION'].astype(str)
                
            #df_ConsultaVinculaciones["IDENTIFICACION"] = df_ConsultaVinculaciones["IDENTIFICACION"].astype(int)
            df_Merge3 = pd.merge(data["IDENTIFICACION"], appended_dafp, on = 'IDENTIFICACION', how = 'left')
            df_Merge3.to_excel(os.path.join(path, str(start_id) + '_' + base_name, f'{base_name}_DAFP.xlsx') , index=False)
                
            #df_ConsultaVinculaciones["IDENTIFICACION"] = df_ConsultaVinculaciones["IDENTIFICACION"].astype(int)
    
            
        start_id += 1
