import pyodbc
import pandas
from sqlalchemy import create_engine
from recursivity import reverse
import pymysql
import sounds

# Declare 'con' globally
con = None
con_mysql = None

def connection_to_db():
    """Attempts to connect to the database."""
    global con
    try:
        con = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=JORGE;"
            "Database=Residencial;"
            "Trusted_Connection=yes;"
        )
        print("Connection Successful!")
        return (True, None)
    except Exception as e:
        print("Connection failed:", e)
        return (False, str(e)) 

def connection_to_mySQL():
    """Connects to database from mySQL"""
    global con_mysql
    try:
        con_mysql = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='residential',
            port=3306,
            charset="utf8mb4",  # Establece la codificación
            use_unicode=True
        )
        print('Coneccion con MySQL exitosa')
        return con_mysql
    except pymysql.Error as e:
        print(f"Error al conectar con mySQL: ",{e})
        raise

def show_table(table_name):
    """Shows data from a table."""
    global con 
    query = f"SELECT * FROM dbo.{table_name}"


    read = pandas.read_sql_query(query, con)
    return read

def get_column_names(table_name):
    global con
    query = (
        f"SELECT COLUMN_NAME "
        f"FROM INFORMATION_SCHEMA.COLUMNS "
        f"WHERE TABLE_NAME = '{table_name}';"
    )


    cursor = con.cursor()
    cursor.execute(query)
    column_names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    
    return column_names

def insert_data(connection, table_name, entries):
    """Insert data into a table."""
    try:

        columns_str = ", ".join(entries.keys())
        placeholders = ", ".join(["?"] * len(entries))
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        cursor = connection.cursor()
        cursor.execute(query, *entries.values())
        connection.commit()

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def update_data(conn, table_name: str, PK_Name: str, Column_Names: list, Values: list, PK_Value):
    """
    Actualiza registros en una tabla específica.

    :param conn: Conexión activa a la base de datos.
    :param table_name: Nombre de la tabla.
    :param PK_Name: Nombre de la columna clave primaria.
    :param Column_Names: Lista de nombres de las columnas a actualizar.
    :param Values: Lista de valores nuevos para las columnas.
    :param PK_Value: Valor de la clave primaria para identificar el registro.
    :return: True si se actualizó correctamente, False en caso de error.
    """

    set_clause = ", ".join([f"{col} = ?" for col in Column_Names])


    sql_update_query = f"""
    UPDATE {table_name}
    SET {set_clause}
    WHERE {PK_Name} = ?;
    """
    valores = Values + [PK_Value]

    try:
        cursor = conn.cursor()
        cursor.execute(sql_update_query, valores)
        conn.commit()
        print("Registro actualizado correctamente.")
        return True
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return False
    finally:
        cursor.close()

import pyodbc

def getTablePK(table_name):
    global con
    query = (f"SELECT COLUMN_NAME "
             f"FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
             f"WHERE TABLE_NAME = '{table_name}' "
             f"AND CONSTRAINT_NAME IN ("
             f"SELECT CONSTRAINT_NAME "
             f"FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS "
             f"WHERE TABLE_NAME = '{table_name}' "
             f"AND CONSTRAINT_TYPE = 'PRIMARY KEY')")

    cursor = con.cursor()
    cursor.execute(query)
    columns = cursor.fetchall()


    if columns:
        pk_columns = [col[0] for col in columns] 
        return ", ".join(pk_columns)  
    else:
        return None
    

def update_data(table_name: str, PK_Name: str, Column_Names: list, Values: list):
    global con
    """
    Actualiza registros en una tabla específica.

    :param conn: Conexión activa a la base de datos.
    :param table_name: Nombre de la tabla.
    :param PK_Name: Nombre de la columna clave primaria.
    :param Column_Names: Lista de nombres de las columnas a actualizar.
    :param Values: Lista de valores nuevos para las columnas.
    :param PK_Value: Valor de la clave primaria para identificar el registro.
    :return: True si se actualizó correctamente, False en caso de error.
    """

    set_clause = ", ".join([f"{col} = ?" for col in Column_Names])

    sql_update_query = f"""
    UPDATE {table_name}
    SET {set_clause}
    WHERE {PK_Name} = ?;
    """

    try:
        cursor = con.cursor() 
        cursor.execute(sql_update_query, Values)
        con.commit()
        print("Registro actualizado correctamente.")
        return True
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return False

def delete_data(table_name, pk_column, pk_value):
    global con
    """Delete data from a table based on a primary key value."""
    try:

        query = f"DELETE FROM {table_name} WHERE {pk_column} = ?"

        cursor = con.cursor()
        cursor.execute(query, (pk_value,))

        con.commit()

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

"""Migracion de base de datos a mySQL hecho por Agustín Mendoza"""

def migrar_datos():
    cursor_sqlserver = con.cursor()
    cursor_mysql = con_mysql.cursor()
    try:
        # Obtener las tablas desde SQL Server
        cursor_sqlserver.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
        """)
        tablas = [tabla[0] for tabla in cursor_sqlserver.fetchall()]

        for nombre_tabla in tablas:
            print(f"Migrando datos de la tabla: {nombre_tabla}")

            # Obtener datos de la tabla desde SQL Server
            cursor_sqlserver.execute(f"SELECT * FROM {nombre_tabla}")
            datos = cursor_sqlserver.fetchall()

            # Obtener los nombres de las columnas
            columnas = [desc[0] for desc in cursor_sqlserver.description]
            columnas_str = ', '.join(columnas)

            # Verificar si la tabla existe en MySQL
            cursor_mysql.execute("SHOW TABLES LIKE %s", (nombre_tabla,))
            if not cursor_mysql.fetchone():
                print(f"La tabla {nombre_tabla} no existe en MySQL. Creándola...")
                # Generar CREATE TABLE basado en la estructura de SQL Server
                cursor_sqlserver.execute(f"""
                    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_NAME = '{nombre_tabla}'
                """)
                columnas_info = cursor_sqlserver.fetchall()
                columnas_mysql = []
                for col in columnas_info:
                    col_name, data_type, char_length = col
                    if data_type in ('nvarchar', 'varchar'):
                        columnas_mysql.append(f"`{col_name}` VARCHAR({char_length or 255})")
                    elif data_type in ('int', 'bigint'):
                        columnas_mysql.append(f"`{col_name}` INT")
                    elif data_type in ('datetime', 'date'):
                        columnas_mysql.append(f"`{col_name}` DATETIME")
                    elif data_type in ('varbinary', 'image'):
                        columnas_mysql.append(f"`{col_name}` LONGBLOB")
                    else:
                        columnas_mysql.append(f"`{col_name}` TEXT")
                create_table_sql = f"""
                    CREATE TABLE `{nombre_tabla}` ({', '.join(columnas_mysql)});
                """
                cursor_mysql.execute(create_table_sql)

            # Eliminar registros existentes
            cursor_mysql.execute(f"DELETE FROM `{nombre_tabla}`")

            # Procesar datos para manejar binarios y codificación
            def limpiar_fila(fila):
                nueva_fila = []
                for valor in fila:
                    if isinstance(valor, bytes):
                        try:
                            nueva_fila.append(valor.decode('utf-8'))  # Intenta UTF-8
                        except UnicodeDecodeError:
                            try:
                                nueva_fila.append(valor.decode('latin1'))  # Intenta Latin1
                            except UnicodeDecodeError:
                                nueva_fila.append(valor)  # Mantén bytes crudos
                    else:
                        nueva_fila.append(valor)
                return tuple(nueva_fila)

            datos_limpios = [limpiar_fila(fila) for fila in datos]

            # Insertar los datos en MySQL
            if datos_limpios:
                placeholders = ', '.join(['%s'] * len(columnas))
                sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders})"
                cursor_mysql.executemany(sql, datos_limpios)

        # Confirmar la transacción en MySQL
        con_mysql.commit()
        print("Migración completada con éxito.")
        sounds.succed_task()

    except Exception as e:
        print(f"Error durante la migración: {e}")
        con_mysql.rollback()
    finally:
        cursor_sqlserver.close()
        cursor_mysql.close()

def clone_reversed_columns(table_name: str):
    global con
    """Clones only string columns, but stores their reversed values in new columns with {column_name}REV."""

    try:
        query = f"""
        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table_name}'
        AND DATA_TYPE IN ('varchar', 'nvarchar', 'text', 'char', 'nchar');
        """
        cursor = con.cursor()
        cursor.execute(query)

        columns = cursor.fetchall()
        string_columns = [col[0] for col in columns]
        column_types = {col[0]: (col[1], col[2]) for col in columns}

        if not string_columns:
            return False

        for col in string_columns:
            col_type, max_len = column_types[col]
            new_col_type = col_type
            if max_len is not None:
                new_col_len = max_len
            else:
                new_col_len = 255

            new_column = f"{col}REV"
            alter_table_query = f"ALTER TABLE {table_name} ADD {new_column} {new_col_type}({new_col_len});"
            cursor.execute(alter_table_query)
        con.commit()

        for col in string_columns:
            new_column = f"{col}REV"
            select_query = f"SELECT {col} FROM {table_name};"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            if not rows:
                continue

            for row in rows:
                original_value = row[0]
                if original_value is not None:
                    reversed_value = reverse(original_value, "", len(original_value) - 1)
                    print(f"Original: {original_value} -> Reversed: {reversed_value}")
                else:
                    reversed_value = None

   
                if original_value is not None and reversed_value is not None:
                    update_query = f"UPDATE {table_name} SET {new_column} = ? WHERE {col} = ?;"
                    cursor.execute(update_query, (reversed_value, original_value))

        con.commit()
        return True

    except Exception as e:
        return False

    finally:
        cursor.close()

def removeReversedColumn(table_name, column_name):
    global con
    cursor = con.cursor()

    try:
        check_column_query = f"""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}REV';
        """
        cursor.execute(check_column_query)
        column_exists = cursor.fetchone()

        if not column_exists:
            print(f"Column '{column_name}REV' does not exist in table '{table_name}'.")
            return False

        drop_column_query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}REV;"
        cursor.execute(drop_column_query)

        con.commit()
        print(f"Column '{column_name}REV' successfully removed from table '{table_name}'.")
        return True

    except Exception as e:
        print(f"Error removing column '{column_name}REV': {e}")
        con.rollback()
        return False