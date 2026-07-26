
import pandas as pd
import mysql.connector                  #Librería para trabajar con Mysql
import streamlit as st

# CONEXION A LA DASE DE DATOS
@st.cache_data
def cargar_datos():                     #Función para realizar la conexión a la DB y obtener la tabla de datos

    try:
        conexion_db = mysql.connector.connect(  #Método para configurar parámetros de conexión
            host = "sql10.freesqldatabase.com",                 #Equipo local, Información del Servidor DB
            user = "sql10833735",                      #Nombre del administrador DB
            password = "9UeFiiSCXD",       #Password del administrador
            database =  "sql10833735"        #Nombre de la DB
        )


        consulta_sql = "SELECT * FROM ventas_vehiculos"  # Consulta SQL
        df = pd.read_sql(consulta_sql,conexion_db)
        conexion_db.close()
        
        return df    #Devolver el resultado al archivo que lo solicitó

    except Exception as error:             # Captura el error y lo asign a una variable
        print(f"SE DETECTÓ UN PROBLEMA:{error}")