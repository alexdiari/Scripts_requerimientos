# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:34:18 2025

@author: josea.gonzalez
"""
    
import webbrowser

# Diccionario de enlaces con un número asociado
links = {
    #outlook
    "1": "https://outlook.office.com/mail/",
    #busqueda de RUES databricks
    "2": "https://adb-4922282910286097.17.azuredatabricks.net/login.html?o=4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097%3Fo%3D4922282910286097&next_url=%2Feditor%2Fnotebooks%2F3327779942180371%3Fo%3D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097%253Fo%253D4922282910286097&tuuid=eaf97ed7-a126-4b8d-9b0b-fedfc9117fdb#command/3838561884093297",
    #Sharepoint
    "3": "https://congenrep.sharepoint.com/sites/DIARI/unidad_analisis/Repositorios/Forms/AllItems.aspx?id=%2Fsites%2FDIARI%2Funidad%5Fanalisis%2FRepositorios%2FRepositorio%20de%20Gesti%C3%B3n%2F801116%2D077%2DINFORMES%2F801116%2D077%2D277%2DANAL%C3%8DTICA%20DE%20DATOS%2FGesti%C3%B3n%20Solicitudes%20Infor%2FSoportes%2F2025&viewid=31ff50a5%2Df16b%2D4237%2D860b%2Dd207f0fd7d7f",
    #Kactus
    "4": "https://talentohumano.contraloria.gov.co/webkactus/frmBiEdforL.aspx#no-back-button",
    #Campus virtual contraloría
    "5": "https://campusvirtualcef.contraloria.gov.co/login/index.php?loginredirect=1",
    #WS
    "6": "https://wsdiari.contraloria.gov.co/Start/Inicio",
    #Sigecoc
    "7": "https://sigedoc.contraloria.gov.co/SGD_WEB/main/index.jsp",
    #Portal de Rues
    "8": "https://ruesfront.rues.org.co/interno/?term=80059878",
    #Azure
    "9": "https://dev.azure.com/diaricgr/BID_TRVS_SOPORTE",
    #SIGECI Procedimiento Obtención Fuentes de Información
    "10": "https://prorrogasireci.contraloria.gov.co/CDISC/Entorno/InCopiaNoControlada?codigo=575",
    #Inventario
    "11": "https://congenrep.sharepoint.com/:x:/r/sites/DIARI/unidad_analisis/_layouts/15/doc2.aspx?sourcedoc=%7B63e48526-4101-43f6-a6c0-1bab137bf48d%7D&action=view&activeCell=%27Inventario%27!G12964&wdinitialsession=d4d68bd1-1f69-c685-f6aa-ce245261c432&wdrldsc=9&wdrldc=1&wdrldr=AccessTokenExpiredWarningUnauthenticated%2CRefreshin",
    #DATABRICKS
    "12": "https://adb-4922282910286097.17.azuredatabricks.net/?o=4922282910286097"
    
}

while True:
    print("\nSelecciona un enlace para abrir:")
    for key, url in links.items():
        print(f"{key}. {url}")

    print("0. Salir")

    choice = input("Ingresa el número del enlace que quieres abrir: ")

    if choice == "0":
        print("Saliendo del programa...")
        break
    elif choice in links:
        webbrowser.open_new_tab(links[choice])
        print(f"Abriendo {links[choice]}...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        
        

