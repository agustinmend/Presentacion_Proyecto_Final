import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox

def prueba(conn_sqlserver , conn_mysql):
    cursor_sqlserver = conn_sqlserver.cursor()
    cursor_mysql = conn_mysql.cursor()
    tablas = ['lease', 'staff', 'customer', 'room', 'payment']
    for tabla in tablas:
        cursor_sqlserver.execute(f"SELECT COUNT(*) FROM {tabla}")
        registros_sqlserver = cursor_sqlserver.fetchone()[0]
        cursor_mysql.execute(f"SELECT COUNT(*) FROM {tabla}")
        registros_mysql = cursor_mysql.fetchone()[0]
        if registros_sqlserver == registros_mysql:
            print(f"La tabla '{tabla}' es igual en ambas bases de datos")
        else:
            print(f"La tabla: '{tabla}' no es igual en ambas base de datos")
    cursor_sqlserver.close()
    cursor_mysql.close()