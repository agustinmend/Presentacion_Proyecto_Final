import pyodbc
import pandas

# Declare 'con' globally
con = None

def connection_to_db():
    """Attempts to connect to the database."""
    global con  # Declare con as global so it can be used in other functions
    try:
        con = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=JORGE;"
            "Database=Residencial;"
            "Trusted_Connection=yes;"
        )
        print("Connection Successful!")
        return (True, None)  # Success
    except Exception as e:
        print("Connection failed:", e)
        return (False, str(e))  # Failure with error message

def show_table(table_name):
    """Shows data from a table."""
    global con  # Use the global connection here
    query = f"SELECT * FROM dbo.{table_name}"

    # Use the global connection for reading SQL
    read = pandas.read_sql_query(query, con)
    return read

def get_column_names(table_name):
    global con
    query = (
        f"SELECT COLUMN_NAME "
        f"FROM INFORMATION_SCHEMA.COLUMNS "
        f"WHERE TABLE_NAME = '{table_name}';"
    )

    # Crear un cursor a partir de la conexión global
    cursor = con.cursor()
    # Ejecuta la consulta
    cursor.execute(query)
    # Recupera todos los nombres de las columnas
    column_names = [row[0] for row in cursor.fetchall()]
    # Cierra el cursor
    cursor.close()
    
    return column_names

def insert_data(connection, table_name, entries):
    """Insert data into a table."""
    try:
        # Generate the SQL query dynamically based on columns and values
        columns_str = ", ".join(entries.keys())
        placeholders = ", ".join(["?"] * len(entries))
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, *entries.values())
        connection.commit()

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def update_data(connection, table_name, entries, condition=None):
    """Update data in a table with flexibility to set conditions."""
    try:
        # Validate if entries is a dictionary
        if not isinstance(entries, dict):
            raise ValueError("Entries must be a dictionary.")

        # Generate the SET clause dynamically based on the entries
        set_clause = ", ".join([f"{column} = ?" for column in entries.keys()])
        
        # Construct the base SQL query
        query = f"UPDATE {table_name} SET {set_clause}"
        
        # If a condition is provided, add the WHERE clause
        if condition:
            query += f" WHERE {condition}"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, tuple(entries.values()))  # Pass values as a tuple
        connection.commit()

        print(f"Rows updated: {cursor.rowcount}")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False