import mispaquetes.coneccion_BD as conect
import mispaquetes.mostrar as mostrar
import mispaquetes.agregar as add
import mispaquetes.eliminar as deleted
import mispaquetes.modificar as mod
import mispaquetes.migrar as migrar
import mispaquetes.defensa as defensa
import tkinter as tk
conn_sqlserver = None
cursor_sqlserver = None
conn_mysql = None
cursor_mysql = None
try:
    root = tk.Tk()
    root.title('Residencial')
    root.geometry('900x600')
    conn_sqlserver = conect.conectar_sqlserver()
    conn_mysql = conect.conectar_mysql()
    migrar.crear_tablas_mysql(conn_sqlserver , conn_mysql)

    Encabezado = tk.Label(root , text="""BIENVENIDO\nQUE DESEA HACER HOY?""")
    Encabezado.pack(pady=20)

    boton_mostrar = tk.Button(root , text= 'MOSTRAR TABLA' , command=lambda : mostrar.mostrar_tablas(conn_sqlserver))
    boton_mostrar.pack(pady=20)

    boton_agregar = tk.Button(root , text= 'AGREGAR' , command=lambda : add.agregar(conn_sqlserver))
    boton_agregar.pack(pady=20)

    boton_modificar = tk.Button(root , text='MODIFICAR' , command= lambda : mod.modificar(conn_sqlserver))
    boton_modificar.pack(pady=20)

    boton_eliminar = tk.Button(root , text='ELIMINAR', command= lambda : deleted.deleted(conn_sqlserver))
    boton_eliminar.pack(pady=20)

    boton_defensa = tk.Button(root , text='DEFENSA DEL CODIGO' , command= lambda : defensa.defensa(conn_sqlserver))
    boton_defensa.pack(pady=20)

    boton_actualizar = tk.Button(root , text='MIGRAR A MYSQL' , command= lambda : migrar.actualizar_datos(conn_sqlserver , conn_mysql))
    boton_actualizar.pack(pady=20)
    root.mainloop()
except Exception as e:
    print('Ocurrio algo: ',{e})
finally:
    conect.cerrar_serversql(conn_sqlserver)
    conect.cerrar_mysql(conn_mysql)