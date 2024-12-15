import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox

#FUNCION ELIMINAR
def deleted(conn):
    ventana_opciones = tk.Toplevel()
    ventana_opciones.geometry('900x600')
    ventana_opciones.title('Opciones')

    etiqueta = tk.Label(ventana_opciones , text='SELECCIONA LA TABLA')
    etiqueta.pack(pady=20)
    boton_customer = tk.Button(ventana_opciones , text='CUSTOMER' , command= lambda : eliminar_customer(conn))
    boton_customer.pack(pady=20)
    boton_Lease = tk.Button(ventana_opciones , text='LEASE' , command= lambda : eliminar_lease(conn))
    boton_Lease.pack(pady=20)
    boton_mantinience = tk.Button(ventana_opciones , text='MANTINIENCE' , command= lambda : eliminar_mantinience(conn))
    boton_mantinience.pack(pady=20)
    boton_payent = tk.Button(ventana_opciones , text='PAYMENT' , command= lambda : eliminar_payment(conn))
    boton_payent.pack(pady=20)
    boton_Room = tk.Button(ventana_opciones , text='ROOM' , command= lambda : eliminar_room(conn))
    boton_Room.pack(pady=20)
    boton_staff = tk.Button(ventana_opciones , text='STAFF' , command=lambda : eliminar_staff(conn))
    boton_staff.pack(pady=20)
    boton_salir = tk.Button(ventana_opciones , text='VOLVER' , command= lambda : ventana_opciones.destroy())
    boton_salir.pack(pady=10)

def eliminar_customer(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL CLIENTE QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_customerid = tk.Entry(ventana_id)
    entry_customerid.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_customerid.get() , 'Customer' , 'CustomerID' , ventana_id))
    boton_eliminar.pack(pady=5)
def eliminar_lease(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL ALQUILER QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_leaseid = tk.Entry(ventana_id)
    entry_leaseid.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_leaseid.get() ,'Lease' , 'LeaseID' , ventana_id))
    boton_eliminar.pack(pady=5)
    

def eliminar_mantinience(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL PEDIDO QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_resquestID = tk.Entry(ventana_id)
    entry_resquestID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_resquestID.get() ,'Mantinience' , 'RequestID' , ventana_id))
    boton_eliminar.pack(pady=5)

def eliminar_payment(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL PAGO QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_resquestID = tk.Entry(ventana_id)
    entry_resquestID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_resquestID.get() ,'Payment' , 'PaymentID' , ventana_id))
    boton_eliminar.pack(pady=5)



def eliminar_room(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DE LA HABITACION QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_resquestID = tk.Entry(ventana_id)
    entry_resquestID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_resquestID.get() ,'Room' , 'RoomID' , ventana_id))
    boton_eliminar.pack(pady=5)


def eliminar_staff(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL EMPLEADO QUE DESEA ELIMINAR')
    texto.pack(pady=5)
    entry_resquestID = tk.Entry(ventana_id)
    entry_resquestID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='ELIMINAR' , command= lambda : delete(conn , entry_resquestID.get() ,'Staff' , 'EmployeeID' , ventana_id))
    boton_eliminar.pack(pady=5)


def delete(conn , dato ,tabla , columna , ventana_anterior):
    try:    
        cursor = conn.cursor()
        query = f'DELETE from {tabla} WHERE {columna} = ?'
        cursor.execute(query , (dato))
        conn.commit()

        ventana_anterior.destroy()
        ventana_exito = tk.Toplevel()
        ventana_exito.title('exito')
        label = tk.Label(ventana_exito , text='Eliminacion exitosa')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.title('ERROR')
        label_error = tk.Label(ventana_error , text=f'Ocurrio algo: {e}')
        label_error.pack(pady=5)
    finally:
        cursor.close()
