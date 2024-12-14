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

def crear_tablas_mysql(conn_sqlserver, conn_mysql):
    cursor_sqlserver = conn_sqlserver.cursor()
    cursor_mysql = conn_mysql.cursor()

    cursor_sqlserver.execute(""" 
        SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'
    """)
    tablas = cursor_sqlserver.fetchall()

    for tabla in tablas:
        nombre_tabla = tabla[0]
        if nombre_tabla in ['sysdiagrams']:
            continue
        cursor_mysql.execute(f"SHOW TABLES LIKE '{nombre_tabla}'")
        tabla_existe = cursor_mysql.fetchone()
        if tabla_existe:
            continue
        cursor_sqlserver.execute(f"""
            SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{nombre_tabla}'
        """)
        columnas = cursor_sqlserver.fetchall()

        cursor_sqlserver.execute(f"""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
            WHERE TABLE_NAME = '{nombre_tabla}' AND CONSTRAINT_NAME = 'PRIMARY'
        """)
        columnas_clave_primaria = cursor_sqlserver.fetchall()
        claves_primarias = [col[0] for col in columnas_clave_primaria]
        columnas_mysql = []
        for columna in columnas:
            nombre_columna = columna[0]
            tipo_dato = columna[1]
            longitud = columna[2]
            if tipo_dato in ['varchar', 'nvarchar']:
                longitud = longitud or 255
                columnas_mysql.append(f"{nombre_columna} VARCHAR({longitud})")
            elif tipo_dato in ['int']:
                columnas_mysql.append(f"{nombre_columna} INT")
            elif tipo_dato in ['datetime']:
                columnas_mysql.append(f"{nombre_columna} DATETIME")
            else:
                columnas_mysql.append(f"{nombre_columna} TEXT")
        if claves_primarias:
            columnas_mysql.append(f"PRIMARY KEY ({', '.join(claves_primarias)})")
        columnas_str = ", ".join(columnas_mysql)
        cursor_mysql.execute(f"CREATE TABLE {nombre_tabla} ({columnas_str});")
    
    conn_mysql.commit()
    cursor_mysql.close()
    cursor_sqlserver.close()

def actualizar_datos(conn_sqlserver, conn_mysql):
    cursor_sqlserver = conn_sqlserver.cursor()
    cursor_mysql = conn_mysql.cursor()
    cursor_sqlserver.execute("""
        SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'
    """)
    tablas = cursor_sqlserver.fetchall()
    for tabla in tablas:
        nombre_tabla = tabla[0]
        cursor_mysql.execute(f"SHOW TABLES LIKE '{nombre_tabla}'")
        tabla_existe = cursor_mysql.fetchone()
        if tabla_existe:
            cursor_mysql.execute(f"DELETE FROM {nombre_tabla}")
        cursor_sqlserver.execute(f"SELECT * FROM {nombre_tabla}")
        datos = cursor_sqlserver.fetchall()
        columnas = [desc[0] for desc in cursor_sqlserver.description]
        for fila in datos:
            valores = ', '.join([f"'{str(valor)}'" if valor is not None else "NULL" for valor in fila])
            columnas_str = ', '.join(columnas)
            sql = f"""
                INSERT INTO {nombre_tabla} ({columnas_str}) VALUES ({valores});
            """
            cursor_mysql.execute(sql)

    conn_mysql.commit()
    print("Sincronización completada.")
    cursor_sqlserver.close()
    cursor_mysql.close()