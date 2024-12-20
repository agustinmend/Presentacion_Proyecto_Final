import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox
#FUNCION AGREGAR
def agregar_customer(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('Datos customer')
    ventana_agregar.geometry('900x600')
    
    etiqueta_ID = tk.Label(ventana_agregar , text='INGRESE ID DEL CLIENTE')
    etiqueta_ID.pack(pady=10)
    entry_ID = tk.Entry(ventana_agregar)
    entry_ID.pack(pady=10)

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

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_customer(conn , entry_ID.get() , entry_firtsname.get() , entry_middlename.get() , entry_lastname.get() , entry_numberphone.get() , entry_email.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def agregar_lease(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('Agrgar datos')
    ventana_agregar.geometry('900x600')

    etiqueta_ID = tk.Label(ventana_agregar , text='INGRESE el ID DEL ALQUILER')
    etiqueta_ID.pack(pady=10)
    entry_ID = tk.Entry(ventana_agregar)
    entry_ID.pack(pady=10)

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

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_lease(conn , entry_ID.get() , entry_room_id.get() , entry_customerID.get() , entry_start_date.get() , entry_end_date.get() , var.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def agregar_mantinience(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_resquestID = tk.Label(ventana_agregar , text='INGRESE ID DEL PEDIDO')
    etiqueta_resquestID.pack(pady=10)
    entry_resquestID = tk.Entry(ventana_agregar)
    entry_resquestID.pack(pady=10)

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

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_mantinience(conn , entry_resquestID.get() , entry_roomID.get() , entry_customerID.get() , entry_resquest_date.get() , entry_descripcion.get() , var.get() , entry_employeeID.get() , ventana_agregar))
    boton_agregar.pack(pady=10)

def agregar_payment(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_paymentID = tk.Label(ventana_agregar , text='INGRESE ID DEL PAGO')
    etiqueta_paymentID.pack(pady=5)
    entry_paymentID = tk.Entry(ventana_agregar)
    entry_paymentID.pack(pady=5)

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

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_payment(conn , entry_paymentID.get() , entry_leaseID.get() , entry_customerID.get() , entry_employeeID.get() , entry_roomID.get() , entry_amount.get() , entry_paymentDate.get() , var1.get() , var2.get() , ventana_agregar))
    boton_agregar.pack(pady=5)

def agregar_room(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_roomID = tk.Label(ventana_agregar , text='INGRESE ID DE LA HABITACION')
    etiqueta_roomID.pack(pady=5)
    entry_roomID = tk.Entry(ventana_agregar)
    entry_roomID.pack(pady=5)

    etiqueta_roomnumber = tk.Label(ventana_agregar , text='INGRESE NRO DE HABITACION')
    etiqueta_roomnumber.pack(pady=5)
    entry_roomnumber = tk.Entry(ventana_agregar)
    entry_roomnumber.pack(pady=5)

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
    etiqueta_beds.pack(pady=5)
    entry_beds = tk.Entry(ventana_agregar)
    entry_beds.pack(pady=5)

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
    etiqueta_weeklyrent.pack(pady=5)
    entry_weeklyrent = tk.Entry(ventana_agregar)
    entry_weeklyrent.pack(pady=5)

    boton_salir = tk.Button(ventana_agregar , text='CANCELAR' , command= lambda : ventana_agregar.destroy())
    boton_salir.pack(pady=5)

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_room(conn , entry_roomID.get() , entry_roomnumber.get() , var1.get() , entry_beds.get() , var2.get() , var3.get() , entry_weeklyrent.get() , ventana_agregar))
    boton_agregar.pack(pady=5)
def agregar_staff(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.geometry('900x600')
    ventana_agregar.title('agregar datos')

    etiqueta_employeeID = tk.Label(ventana_agregar , text='INGRESE ID DEL EMPLEADO')
    etiqueta_employeeID.pack(pady=10)
    entry_employeeID = tk.Entry(ventana_agregar)
    entry_employeeID.pack(pady=10)

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

    boton_agregar = tk.Button(ventana_agregar , text='GUARDAR' , command= lambda : guardar_nuevo_staff(conn , entry_employeeID.get() , entry_firtsname.get() , entry_middlename.get() , entry_lastname.get() , entry_email.get() , entry_occupation.get() , ventana_agregar))
    boton_agregar.pack(pady=10)
def agregar(conn):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('AGREGAR')
    ventana_agregar.geometry('900x600')
    instruccion = tk.Label(ventana_agregar , text='SELECCIONE QUE DESEA AGREGAR')
    instruccion.pack(pady=10)
    boton_customer = tk.Button(ventana_agregar , text='CUSTOMER' , command= lambda : agregar_customer(conn))
    boton_customer.pack(pady=10)
    boton_lease = tk.Button(ventana_agregar , text='LEASE' , command= lambda : agregar_lease(conn))
    boton_lease.pack(pady=10)
    boton_mantinience = tk.Button(ventana_agregar , text='MANTINIENCE' , command= lambda : agregar_mantinience(conn))
    boton_mantinience.pack(pady=10)
    boton_payent = tk.Button(ventana_agregar , text='PAYMENT' , command= lambda : agregar_payment(conn))
    boton_payent.pack(pady=10)
    boton_Room = tk.Button(ventana_agregar , text='ROOM' , command= lambda : agregar_room(conn))
    boton_Room.pack(pady=10)
    boton_staff = tk.Button(ventana_agregar , text='STAFF' , command=lambda : agregar_staff(conn))
    boton_staff.pack(pady=10)
    boton_volver = tk.Button(ventana_agregar , text='VOLVER' , command= lambda : ventana_agregar.destroy())
    boton_volver.pack(pady=10)

def guardar_nuevo_customer(conn , customerid , firtsname , middlename , lastname , numberphone , email , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into customer (CustomerID , FirstName , MiddleName , LastName , NumberPhone , Email) values (? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (customerid , firtsname , middlename , lastname , numberphone , email))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()

def guardar_nuevo_lease(conn , leaseid , roomid , customerid , startdate , enddate , status , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into Lease (LeaseID , RoomID , CustomerID , StartDate , EndDate , Status) values (? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (leaseid , roomid , customerid , startdate , enddate , status))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()

def guardar_nuevo_mantinience(conn , resquestid , roomid , customerid , resquestdate , description , status , employeeid , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into Mantinience (RequestID , RoomID , CustomerID , RequestDate , Description , Status , EmployeeID) values (? , ? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (resquestid , roomid , customerid , resquestdate , description , status , employeeid))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()
def guardar_nuevo_payment(conn , paymentid , leaseid , customerid , employeeid , roomid , amount , paymentdate , paymentmethod , status , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into Payment (PaymentID , LeaseID , CustomerID , EmployeeID , RoomID , Amount , PaymentDate , PaymentMethod , Status) values (? , ? , ? , ? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (paymentid , leaseid , customerid , employeeid , roomid , amount , paymentdate , paymentmethod , status))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()
def guardar_nuevo_room(conn , roomid , roomnumber , type , beds , countwhitac , isoccupied , weeklyrent , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into Room (RoomID , RoomNumber , Type , Beds , CountWithAC , IsOccupied , WeeklyRent) values (? , ? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (roomid , roomnumber , type , beds , countwhitac , isoccupied , weeklyrent))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()

def guardar_nuevo_staff(conn , employeeID , firtsname , middlename , lastname , email , ocuppation , ventana_agregar):
    try:
        cursor = conn.cursor()
        query = f"insert into Staff (EmployeeID , FirstName , MiddleName , LastName , Email , Occupation) values (? , ? , ? , ? , ? , ?)"
        cursor.execute(query , (employeeID , firtsname , middlename , lastname , email , ocuppation))
        conn.commit()
        ventana_agregar.destroy()
        mensaje_confirmacion = tk.Toplevel()
        mensaje_confirmacion.geometry('200x100')
        mensaje_confirmacion.title('OPERACION EXITOSA')
        label = tk.Label(mensaje_confirmacion , text='Se ha agregado correctamente')
        label.pack(pady=5)
    except Exception as e:
        ventana_error = tk.Toplevel()
        ventana_error.geometry('200x100')
        ventana_error.title('ERROR')
        label = tk.Label(ventana_error , text=f'Error al agregar :{e}')
        label.pack(pady=5)
    finally:
        cursor.close()