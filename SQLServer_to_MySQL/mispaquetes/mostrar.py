import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox

#FUNCION MOSTRAR
def mostrar(conn , tabla):
    query = "Select * from " + tabla
    df = pandas.read_sql(query , conn)
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title('TABLA')
    ventana_tabla.geometry("900x600")
    tree = ttk.Treeview(ventana_tabla)
    tree.pack(fill=tk.BOTH , expand= True)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    for col in df.columns:
        tree.heading(col , text= col)
        tree.column(col , width=150)

    for _, row in  df.iterrows():
        tree.insert("", "end" , values=list(row))

def mostrar_tablas(conn):
    ventana_tablas = tk.Toplevel()
    ventana_tablas.title('opciones de tabla')
    ventana_tablas.geometry('900x600')
    etiqueta = tk.Label(ventana_tablas , text='SELECCIONA LA TABLA Q DESEAS VER')
    etiqueta.pack(pady=20)
    boton_customer = tk.Button(ventana_tablas , text='CUSTOMER' , command= lambda : mostrar(conn , "customer"))
    boton_customer.pack(pady=20)
    boton_Lease = tk.Button(ventana_tablas , text='LEASE' , command= lambda : mostrar(conn , "lease"))
    boton_Lease.pack(pady=20)
    boton_mantinience = tk.Button(ventana_tablas , text='MANTINIENCE' , command= lambda : mostrar(conn , "mantinience"))
    boton_mantinience.pack(pady=20)
    boton_payent = tk.Button(ventana_tablas , text='PAYMENT' , command= lambda : mostrar(conn , "payment"))
    boton_payent.pack(pady=20)
    boton_Room = tk.Button(ventana_tablas , text='ROOM' , command= lambda : mostrar(conn , "room"))
    boton_Room.pack(pady=20)
    boton_staff = tk.Button(ventana_tablas , text='STAFF' , command=lambda : mostrar(conn , "staff"))
    boton_staff.pack(pady=20)
    boton_salir = tk.Button(ventana_tablas , text='VOLVER' , command= lambda : ventana_tablas.destroy())
    boton_salir.pack(pady=10)


