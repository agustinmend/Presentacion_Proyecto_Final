import pyodbc
import pymysql
import pandas
def conectar_sqlserver():
    try:
        conn_serversql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=' + 'AGUSTIN' + ';'
                    'DATABASE=' + 'residencial' + ';'
                    'trusted_connection=yes')
        print('CONECCION CON SERVER SQL EXITOSA')
        return conn_serversql
    except pyodbc.Error as e:
        print(f"Error al conectar con sql server: ",{e})
        raise
def conectar_mysql():
    try:
        conn_mysql = pymysql.connect(
            host='localhost',
            user='root',
            password='camade2pisossql',
            database='prueba',
            port=3306
        )
        print('Coneccion con MySQL exitosa')
        return conn_mysql
    except pymysql.Error as e:
        print(f"Error al conectar con mySQL: ",{e})
        raise
def cerrar_serversql(conn_sqlserver):
    try:
        if conn_sqlserver:
            conn_sqlserver.close()
            print('Conexión con SQL Server cerrada exitosamente.')
    except Exception as e:
        print(f"Error al cerrar la conexión de SQL Server: {e}")
def cerrar_mysql(conn_mysql):
    try:
        if conn_mysql:
            conn_mysql.close()
            print('Conexión con MySQL cerrada exitosamente.')
    except Exception as e:
        print(f"Error al cerrar la conexión de MySQL: {e}")
def cerrar_cursorserver(cursor_serversql):
    if cursor_serversql:
        cursor_serversql.close()
        print('cursor sqlserver cerrado')
def cerrar_cursormysql(cursor_mysql):
    if cursor_mysql:
        cursor_mysql.close()
        print('Cursor sql cerrado')

