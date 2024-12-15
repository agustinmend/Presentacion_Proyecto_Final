import pyodbc
import pymysql
import pandas
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
        columnas_mysql.append("fecha_modificacion DATETIME DEFAULT NULL")
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
            cursor_sqlserver.execute(f"SELECT * FROM {nombre_tabla}")
            datos_sqlserver = cursor_sqlserver.fetchall()
            columnas_sqlserver = [desc[0] for desc in cursor_sqlserver.description]
            for fila_sqlserver in datos_sqlserver:
                valores_sqlserver = ', '.join([f"'{str(valor)}'" if valor is not None else "NULL" for valor in fila_sqlserver])
                columnas_str = ', '.join(columnas_sqlserver)
                cursor_mysql.execute(f"SELECT * FROM {nombre_tabla} WHERE {columnas_sqlserver[0]} = {fila_sqlserver[0]}")
                fila_mysql = cursor_mysql.fetchone()
                if fila_mysql:
                    cambios = False
                    set_clause = []
                    for col_sqlserver, valor_sqlserver, valor_mysql in zip(columnas_sqlserver, fila_sqlserver, fila_mysql):
                        if valor_sqlserver != valor_mysql:
                            set_clause.append(f"{col_sqlserver} = '{str(valor_sqlserver)}'" if valor_sqlserver is not None else f"{col_sqlserver} = NULL")
                            cambios = True
                    if cambios:
                        set_clause.append("fecha_modificacion = NOW()")
                        set_clause_str = ", ".join(set_clause)
                        cursor_mysql.execute(f"""
                            UPDATE {nombre_tabla}
                            SET {set_clause_str}
                            WHERE {columnas_sqlserver[0]} = {fila_sqlserver[0]}
                        """)
                else:
                    cursor_mysql.execute(f"""
                        INSERT INTO {nombre_tabla} ({columnas_str}, fecha_modificacion) 
                        VALUES ({valores_sqlserver}, NOW())
                    """)
    conn_mysql.commit()
    print("Sincronización completada.")
    cursor_sqlserver.close()
    cursor_mysql.close()