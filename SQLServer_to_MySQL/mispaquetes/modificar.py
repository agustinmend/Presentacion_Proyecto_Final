import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox
#FUNCION MODIFICAR
def modificar(conn):
    ventana_tablas = tk.Toplevel()
    ventana_tablas.title('opciones de tabla')
    ventana_tablas.geometry('900x600')
    etiqueta = tk.Label(ventana_tablas , text='SELECCIONA LA TABLA Q DESEAS MODIFICAR')
    etiqueta.pack(pady=20)
    boton_customer = tk.Button(ventana_tablas , text='CUSTOMER' , command= lambda : modificar_customer(conn))
    boton_customer.pack(pady=20)
    boton_Lease = tk.Button(ventana_tablas , text='LEASE' , command= lambda : modificar_lease(conn))
    boton_Lease.pack(pady=20)
    boton_mantinience = tk.Button(ventana_tablas , text='MANTINIENCE' , command= lambda : modificar_mantinience(conn))
    boton_mantinience.pack(pady=20)
    boton_payent = tk.Button(ventana_tablas , text='PAYMENT' , command= lambda : modificar_payment(conn))
    boton_payent.pack(pady=20)
    boton_Room = tk.Button(ventana_tablas , text='ROOM' , command= lambda : modificar_room(conn))
    boton_Room.pack(pady=20)
    boton_staff = tk.Button(ventana_tablas , text='STAFF' , command=lambda : modificar_staff(conn))
    boton_staff.pack(pady=20)
    boton_salir = tk.Button(ventana_tablas , text='VOLVER' , command= lambda : ventana_tablas.destroy())
    boton_salir.pack(pady=10)


def modificar_customer(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL CLIENTE QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_customerid = tk.Entry(ventana_id)
    entry_customerid.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_customer(conn , entry_customerid.get()))
    boton_eliminar.pack(pady=5)
    

def modificar_lease(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL ALQUILER QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_leaseid = tk.Entry(ventana_id)
    entry_leaseid.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_lease(conn , entry_leaseid.get()))
    boton_eliminar.pack(pady=5)


def modificar_mantinience(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL PEDIDO QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_resquestID = tk.Entry(ventana_id)
    entry_resquestID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_mantinience(conn , entry_resquestID.get()))
    boton_eliminar.pack(pady=5)


def modificar_payment(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL PAGO QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_PaymentID = tk.Entry(ventana_id)
    entry_PaymentID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_payment(conn , entry_PaymentID.get()))
    boton_eliminar.pack(pady=5)

def modificar_room(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DE LA HABITACION QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_roomID = tk.Entry(ventana_id)
    entry_roomID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_room(conn , entry_roomID.get()))
    boton_eliminar.pack(pady=5)

def modificar_staff(conn):
    ventana_id = tk.Toplevel()
    ventana_id.title('datos')
    ventana_id.geometry('300x200')
    texto = tk.Label(ventana_id , text='INGRESE ID DEL EMPLEADO QUE DESEA MODIFICAR')
    texto.pack(pady=5)
    entry_employeeID = tk.Entry(ventana_id)
    entry_employeeID.pack(pady=5)
    boton_salir = tk.Button(ventana_id , text='CANCELAR' , command= lambda : ventana_id.destroy())
    boton_salir.pack(pady=10)
    boton_eliminar = tk.Button(ventana_id , text='MODIFICAR' , command= lambda : modificar_datos_staff(conn , entry_employeeID.get()))
    boton_eliminar.pack(pady=5)

def modificar_datos_customer(conn , customerID):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('Datos customer')
    ventana_agregar.geometry('900x600')
    
    etiqueta_firtsname = tk.Label(ventana_agregar , text='INGRESE NOMBRE DEL CLIENTE')
    etiqueta_firtsname.pack(pady=10)
    entry_firtsname = tk.Entry(ventana_agregar)
    entry_firtsname.pack(pady=10)

    etiqueta_middlename = tk.Label(ventana_agregar , text='INGRESE SEGUNDO NOMBRE DEL CLIENTE')
    etiqueta_middlename.pack(pady=10)
    entry_middlename = tk.Entry(ventana_agregar)
    entry_middlename.pack(pady=10)
    
    etiqueta_Lastname = tk.Label(ventana_agregar , text='INGRESE APELLIDO DEL CLIENTE')
    etiqueta_Lastname.pack(pady=10)
    entry_lastname = tk.Entry(ventana_agregar)
    entry_lastname.pack(pady=10)
    
    etiqueta_numberphone = tk.Label(ventana_agregar , text='INGRESE NRO DE TELEFONO DEL CLIENTE')
    etiqueta_numberphone.pack(pady=10)
    entry_numberphone = tk.Entry(ventana_agregar)
    entry_numberphone.pack(pady=10)
    
    etiqueta_email = tk.Label(ventana_agregar , text='INGRESE EMAIL DEL CLIENTE')
    etiqueta_email.pack(pady=10)
    entry_email = tk.Entry(ventana_agregar)
    entry_email.pack(pady=10)  
    
    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=10)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios_customer(conn , customerID , entry_firtsname.get() , entry_middlename.get() , entry_lastname.get() , entry_numberphone.get() , entry_email.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def modificar_datos_lease(conn , leaseid):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('Agrgar datos')
    ventana_agregar.geometry('900x600')

    etiqueta_room_id = tk.Label(ventana_agregar , text='INGRESE EL ID DE LA HABITACION')
    etiqueta_room_id.pack(pady=10)
    entry_room_id = tk.Entry(ventana_agregar)
    entry_room_id.pack(pady=10)

    etiqueta_customerID = tk.Label(ventana_agregar , text='INGRESE EL ID DEL CLIENTE')
    etiqueta_customerID.pack(pady=10)
    entry_customerID = tk.Entry(ventana_agregar)
    entry_customerID.pack(pady=10)

    etiqueta_start_date = tk.Label(ventana_agregar , text='INGRESE LA FECHA DE INICIO')
    etiqueta_start_date.pack(pady=10)
    entry_start_date = tk.Entry(ventana_agregar)
    entry_start_date.pack(pady=10)

    etiqueta_end_date = tk.Label(ventana_agregar , text='INGRESE LA FECHA DE FIN')
    etiqueta_end_date.pack(pady=10)
    entry_end_date = tk.Entry(ventana_agregar)
    entry_end_date.pack(pady=10)

    var = tk.StringVar()
    etiqueta_status = tk.Label(ventana_agregar , text="INGRESE STATUS DEL ALQUILER")
    etiqueta_status.pack(pady=10)
    radio_status1 = tk.Radiobutton(ventana_agregar , text="Completed" , value="Completed" , variable= var)
    radio_status1.pack(pady=10)
    radio_status2 = tk.Radiobutton(ventana_agregar , text="Active" , value="Active" , variable= var)
    radio_status2.pack(pady=10)
    radio_status3 = tk.Radiobutton(ventana_agregar , text="Available" , value="Available" , variable= var)
    radio_status3.pack(pady=10)
    radio_status4 = tk.Radiobutton(ventana_agregar , text="reserved" , value="reserved" , variable= var)
    radio_status4.pack(pady=10)

    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=10)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios_lease(conn , leaseid , entry_room_id.get() , entry_customerID.get() , entry_start_date.get() , entry_end_date.get() , var.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def modificar_datos_mantinience(conn , resquestID):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_roomID = tk.Label(ventana_agregar , text='INGRESE ID DE LA HABITACION')
    etiqueta_roomID.pack(pady=10)
    entry_roomID = tk.Entry(ventana_agregar)
    entry_roomID.pack(pady=10)

    etiqueta_customerID = tk.Label(ventana_agregar , text='INGRESE ID DEL CLIENTE')
    etiqueta_customerID.pack(pady=10)
    entry_customerID = tk.Entry(ventana_agregar)
    entry_customerID.pack(pady=10)

    etiqueta_resquest_date = tk.Label(ventana_agregar , text='INGRESE LA FECHA DEL PEDIDO')
    etiqueta_resquest_date.pack(pady=10)
    entry_resquest_date = tk.Entry(ventana_agregar)
    entry_resquest_date.pack(pady=10)

    etiqueta_descripcion = tk.Label(ventana_agregar , text='DESCRIBA EL PEDIDO')
    etiqueta_descripcion.pack(pady=10)
    entry_descripcion = tk.Entry(ventana_agregar)
    entry_descripcion.pack(pady=10)

    var = tk.StringVar()
    etiqueta_status = tk.Label(ventana_agregar , text="INGRESE STATUS DEL PEDIDO")
    etiqueta_status.pack(pady=10)
    radio_status1 = tk.Radiobutton(ventana_agregar , text="Completed" , value="Completed" , variable= var)
    radio_status1.pack(pady=5)
    radio_status2 = tk.Radiobutton(ventana_agregar , text="In Progress" , value="In Progress" , variable= var)
    radio_status2.pack(pady=5)
    radio_status3 = tk.Radiobutton(ventana_agregar , text="Pending" , value="Pending" , variable= var)
    radio_status3.pack(pady=5)

    etiqueta_employeeID = tk.Label(ventana_agregar , text='INGRESE ID DEL EMPLEADO')
    etiqueta_employeeID.pack(pady=10)
    entry_employeeID = tk.Entry(ventana_agregar)
    entry_employeeID.pack(pady=10)
    
    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=10)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios_mantinience(conn , resquestID , entry_roomID.get() , entry_customerID.get() , entry_resquest_date.get() , entry_descripcion.get() , var.get() , entry_employeeID.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def modificar_datos_payment(conn , paymentID):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_leaseID = tk.Label(ventana_agregar , text='INGRESE ID DEL ALQUILER')
    etiqueta_leaseID.pack(pady=5)
    entry_leaseID = tk.Entry(ventana_agregar)
    entry_leaseID.pack(pady=5)

    etiqueta_customerID = tk.Label(ventana_agregar , text='INGRESE ID DEL CLIENTE')
    etiqueta_customerID.pack(pady=5)
    entry_customerID = tk.Entry(ventana_agregar)
    entry_customerID.pack(pady=5)

    etiqueta_employeeID = tk.Label(ventana_agregar , text='INGRESE ID DEL EMPLEADO')
    etiqueta_employeeID.pack(pady=5)
    entry_employeeID = tk.Entry(ventana_agregar)
    entry_employeeID.pack(pady=5)

    etiqueta_roomID = tk.Label(ventana_agregar , text='INGRESE ID DE LA HABITACION')
    etiqueta_roomID.pack(pady=5)
    entry_roomID = tk.Entry(ventana_agregar)
    entry_roomID.pack(pady=5)

    etiqueta_amount = tk.Label(ventana_agregar , text='INGRESE MONTO A PAGAR')
    etiqueta_amount.pack(pady=5)
    entry_amount = tk.Entry(ventana_agregar)
    entry_amount.pack(pady=5)

    etiqueta_paymentDate = tk.Label(ventana_agregar , text='INGRESE FECHA DEL PAGO')
    etiqueta_paymentDate.pack(pady=5)
    entry_paymentDate = tk.Entry(ventana_agregar)
    entry_paymentDate.pack(pady=5)

    var1 = tk.StringVar()
    etiqueta_paymentmethod = tk.Label(ventana_agregar , text="INGRESE METODO DE PAGO")
    etiqueta_paymentmethod.pack(pady=5)
    radio_paymentmethod1 = tk.Radiobutton(ventana_agregar , text="Credit Card" , value="Credit Card" , variable= var1)
    radio_paymentmethod1.pack(pady=5)
    radio_paymentmethod2 = tk.Radiobutton(ventana_agregar , text="Debit Card" , value="Debit Card" , variable= var1)
    radio_paymentmethod2.pack(pady=5)
    radio_paymentmethod3 = tk.Radiobutton(ventana_agregar , text="Cash" , value="Cash" , variable= var1)
    radio_paymentmethod3.pack(pady=5)
    radio_paymentmethod4 = tk.Radiobutton(ventana_agregar , text="Bank Transfer" , value="Bank Transfer" , variable= var1)
    radio_paymentmethod4.pack(pady=5)

    var2 = tk.StringVar()
    etiqueta_status = tk.Label(ventana_agregar , text="INGRESE STATUS DEL PEDIDO")
    etiqueta_status.pack(pady=5)
    radio_status1 = tk.Radiobutton(ventana_agregar , text="Completed" , value="Completed" , variable= var2)
    radio_status1.pack(pady=5)
    radio_status2 = tk.Radiobutton(ventana_agregar , text="Reserved" , value="Reserved" , variable= var2)
    radio_status2.pack(pady=5)
    radio_status3 = tk.Radiobutton(ventana_agregar , text="Pending" , value="Pending" , variable= var2)
    radio_status3.pack(pady=5)

    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=5)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios_payment(conn , paymentID , entry_leaseID.get() , entry_customerID.get() , entry_employeeID.get() , entry_roomID.get() , entry_amount.get() , entry_paymentDate.get() , var1.get() , var2.get() , ventana_agregar))
    boton_agregar.pack(pady=5)

def modificar_datos_room(conn , roomID):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_roomnumber = tk.Label(ventana_agregar , text='INGRESE NRO DE HABITACION')
    etiqueta_roomnumber.pack(pady=10)
    entry_roomnumber = tk.Entry(ventana_agregar)
    entry_roomnumber.pack(pady=10)

    var1 = tk.StringVar()
    etiqueta_type = tk.Label(ventana_agregar , text="ELIJA TIPO DE HABITACION")
    etiqueta_type.pack(pady=5)
    radio_type1 = tk.Radiobutton(ventana_agregar , text="Single" , value="Single" , variable= var1)
    radio_type1.pack(pady=5)
    radio_type2 = tk.Radiobutton(ventana_agregar , text="Matrimonial" , value="Matrimonial" , variable= var1)
    radio_type2.pack(pady=5)
    radio_type3 = tk.Radiobutton(ventana_agregar , text="Double" , value="Double" , variable= var1)
    radio_type3.pack(pady=5)
    radio_type4 = tk.Radiobutton(ventana_agregar , text="Suite" , value="Suite" , variable= var1)
    radio_type4.pack(pady=5)
    radio_type5 = tk.Radiobutton(ventana_agregar , text="Double Deluxe" , value="Double Deluxe" , variable= var1)
    radio_type5.pack(pady=5)
    radio_type6 = tk.Radiobutton(ventana_agregar , text="Single Deluxe" , value="Single Deluxe" , variable= var1)
    radio_type6.pack(pady=5)
    radio_type7 = tk.Radiobutton(ventana_agregar , text="Family" , value="Family" , variable= var1)
    radio_type7.pack(pady=5)

    etiqueta_beds = tk.Label(ventana_agregar , text='INGRESE NRO DE CAMAS')
    etiqueta_beds.pack(pady=10)
    entry_beds = tk.Entry(ventana_agregar)
    entry_beds.pack(pady=10)

    var2 = tk.StringVar()
    etiqueta_countwhitac = tk.Label(ventana_agregar , text="CUENTA CON AIRE ACONDICIONADO?")
    etiqueta_countwhitac.pack(pady=5)
    radio_countwhitac1 = tk.Radiobutton(ventana_agregar , text="Yes" , value="Yes" , variable= var2)
    radio_countwhitac1.pack(pady=5)
    radio_countwhitac2 = tk.Radiobutton(ventana_agregar , text="No" , value="No" , variable= var2)
    radio_countwhitac2.pack(pady=5)

    var3 = tk.StringVar()
    etiqueta_ocuped = tk.Label(ventana_agregar , text="LA HABITACION ESTA SIENDO OCUPADA?")
    etiqueta_ocuped.pack(pady=10)
    radio_ocuped1 = tk.Radiobutton(ventana_agregar , text="Yes" , value="Yes" , variable= var3)
    radio_ocuped1.pack(pady=5)
    radio_ocuped2 = tk.Radiobutton(ventana_agregar , text="No" , value="No" , variable= var3)
    radio_ocuped2.pack(pady=5)

    etiqueta_weeklyrent = tk.Label(ventana_agregar , text='INGRESE MONTO DE ALQUILER SEMANAL')
    etiqueta_weeklyrent.pack(pady=10)
    entry_weeklyrent = tk.Entry(ventana_agregar)
    entry_weeklyrent.pack(pady=10)

    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=10)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios_room(conn , roomID , entry_roomnumber.get() , var1.get() , entry_beds.get() , var2.get() , var3.get() , entry_weeklyrent.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def modificar_datos_staff(conn , employeeID):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_firtsname = tk.Label(ventana_agregar , text='INGRESE NOMBRE DEL EMPLEADO')
    etiqueta_firtsname.pack(pady=10)
    entry_firtsname = tk.Entry(ventana_agregar)
    entry_firtsname.pack(pady=10)

    etiqueta_middlename = tk.Label(ventana_agregar , text='INGRESE SEGUNDO NOMBRE DEL EMPLEADO')
    etiqueta_middlename.pack(pady=10)
    entry_middlename = tk.Entry(ventana_agregar)
    entry_middlename.pack(pady=10)
    
    etiqueta_Lastname = tk.Label(ventana_agregar , text='INGRESE APELLIDO DEL EMPLEADO')
    etiqueta_Lastname.pack(pady=10)
    entry_lastname = tk.Entry(ventana_agregar)
    entry_lastname.pack(pady=10)
    
    etiqueta_email = tk.Label(ventana_agregar , text='INGRESE EMAIL DEL EMPLEADO')
    etiqueta_email.pack(pady=10)
    entry_email = tk.Entry(ventana_agregar)
    entry_email.pack(pady=10)  

    etiqueta_occupation = tk.Label(ventana_agregar , text='INGRESE OCUPACION DEL EMPLEADO')
    etiqueta_occupation.pack(pady=10)
    entry_occupation = tk.Entry(ventana_agregar)
    entry_occupation.pack(pady=10) 
    
    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=10)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_cambios(conn , employeeID , entry_firtsname.get() , entry_middlename.get() , entry_lastname.get() , entry_email.get() , entry_occupation.get() , ventana_agregar))
    boton_agregar.pack(pady=10)
def guardar_cambios(conn , employeeID , firtsname , middlename , lastname , email , occupation , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update staff
        set firstname = ? , middlename = ? , lastname = ?, email = ?, occupation = ?
        Where EmployeeID = ?"""
        cursor.execute(query , (firtsname , middlename , lastname , email , occupation, employeeID))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()

def guardar_cambios_customer(conn , customerID , firtsname , middlename , lastname , numberphone , email , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update customer
        set firstname = ? , middlename = ? , lastname = ?, numberphone = ?, email = ?
        Where CustomerID = ?"""
        cursor.execute(query , ( firtsname , middlename , lastname , numberphone , email , customerID))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()
def guardar_cambios_lease(conn , leaseid , roomid , customerID , startdate , enddate , status, ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update lease
        set roomid = ? , customerid = ? , startdate = ?, enddate = ?, status = ?
        Where leaseid = ?"""
        cursor.execute(query , ( roomid , customerID , startdate , enddate , status , leaseid))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()

def guardar_cambios_mantinience(conn , resquestID , roomID , customerID , resquestdate , descripcion , status , employeeID , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update mantinience
        set roomid = ? , customerid = ? , requestdate = ?, description = ?, status = ?, employeeid = ?
        Where requestid = ?"""
        cursor.execute(query , (roomID , customerID , resquestdate , descripcion , status , employeeID , resquestID))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()
    
def guardar_cambios_payment(conn , paymentID , leaseID , customerID , employeeID , roomID , amount , paymentDate , paymentmethod , status , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update Payment
        set leaseid = ? , customerid = ? , employeeid = ?, roomid = ?, amount = ?, paymentdate = ? , paymentmethod = ? , status = ?
        Where paymentid = ?"""
        cursor.execute(query , (leaseID , customerID , employeeID , roomID , amount , paymentDate , paymentmethod , status , paymentID))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()
    
def guardar_cambios_room(conn , roomID , roomnumber , type , beds , countwhitac , ocuped , weeklyrent , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = """
        update room
        set roomnumber = ? , type = ? , beds = ?, CountWithAC = ?, isoccupied = ?, weeklyrent = ?
        Where roomid = ?"""
        cursor.execute(query , (roomnumber , type , beds , countwhitac , ocuped , weeklyrent , roomID))
        conn.commit()
        ventana_agregar.destroy()
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.geometry('200x100')
        ventana_confirmacion.title('Operacion Exitosa')
        mensaje = tk.Label(ventana_confirmacion , text='Se ha modificado correctamente')
        mensaje.pack()
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        mensaje_error = tk.Label(ventana_error , text=f'Algo salio mal: {e}')
        mensaje_error.pack()
    finally:
        cursor.close()
    pass