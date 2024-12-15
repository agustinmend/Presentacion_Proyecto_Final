import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox

def invertir_string(str , i):
    if i == len(str):
        return ''
    else:
        return invertir_string(str , i + 1) + str[i]

def defensa(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'customer' AND COLUMN_NAME = 'modificacion'
    """)
    columna_existe = cursor.fetchone()
    if not columna_existe:
        cursor.execute('ALTER TABLE customer ADD modificacion VARCHAR(50)')
    cursor.execute('SELECT customerid, firstname FROM customer')
    filas = cursor.fetchall()
    for fila in filas:
        customerid = fila[0]
        firstname = fila[1]
        string_invertida = invertir_string(firstname , 0)
        query = 'UPDATE customer SET modificacion = ? WHERE customerid = ?'
        cursor.execute(query, (string_invertida, customerid))
    conn.commit()
    cursor.close()