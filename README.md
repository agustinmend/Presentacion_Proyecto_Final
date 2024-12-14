# Presentacion_Proyecto_Final
## definicion del problema
Se nos encargo modernizar el actual sistema de un residencial para la gestion de datos puesto que este esta basado en tecnologia obsoleta, es lento, poco fiable y propenso a inconcistencia en los datos, para modernizar este sistema ambiguo nosotros hemos desarrollado una aplicacion que permita conectarse con la actual base de datos hecha en SQL Server con opcion a modificar registros, ver las tablas de la actual base de datos , eliminar registros, para que posterior al uso de estas funciones estos cambios se los puedan migrar a una nueva base de datos en MySQL sin generar duplicados ni perdiendo datos
## Manejo de la Aplicacion
La base de datos en Server Sql se encuentra de la siguiente manera
![image](https://github.com/user-attachments/assets/8a51132f-807e-44fb-a5dd-47db4c259136)
En el diagrama podemos observar como estan relacionadas las tablas en SQL server y que columnas contienen, nuestra aplicacion se conecta con esta base de datos tras q se ejecuta al mismo tiempo que tambien se conecta con otra base de datos en mysql, de haber algun problema para conectarse con estas el programa mostrara un mensaje de error en la terminal indicando el porque no se pudo conectar, caso contrario si la aplicacion se conecta con estas de manera exitosa se mostrara un mensaje en la terminal confirmando la conexion.
Una vez lograda la conexion la aplicacion mostrara la ventana principal con 5 botones q corresponden a cada una de las funciones q puede ejecutar el programa.
![image](https://github.com/user-attachments/assets/344d7c7b-921e-4472-8f18-8c3ffbb68bee)
### Mostrar tabla
si se le da click nos abrira otra ventana que preguntara "Que tabla desea ver?" y ofrecera seis opciones distintas de tablas para poder ver y un boton "volver" con el cual se destruye esa ventana y se regresa a la principal, si se selecciona una de las opciones que se brindan el programa abrira una nueva ventana mostrando la tabla de la opcion que se selecciono.
### Agregar
al darle click a este boton se abre una ventana con las opciones de tablas donde puede agregar registro al darle click a una de estas opciones se abrira un formulario para insertar los datos y guardarlos
![image](https://github.com/user-attachments/assets/7bec7e2d-0472-4526-8c9f-04e44363e230)
cada tabla tiene un formulario distinto con los datos necesarios para guardar, caso de que haya algun dato mal ingresado que rompa la relacion entre tablas no se podra añadir el registro y se abrira una ventana mostrando un mensaje  de error, caso contrario si todos los datos son correcctos y no rompen la relacion entre tablas se abrira una ventana mostrando un mensaje confirmando que se añadio el registro.
### Modificar
Al usar esta funcion se abrira una ventana que mostrara las opciones de tabla en las que podemos modificar datos al seleccionar alguna de estas se abrira una ventana donde pedira el ID del registro que desea modificar.
![image](https://github.com/user-attachments/assets/ebd6c393-78dc-4705-93b6-ef32390ebb05)



una vez ingresado se abrira un cuestionario para modificar este registro si todo se llena correctamente sin romper la relacion entre tablas y si el id que se ingreso existe, aparecera una ventana confirmando el cambio pero si alguno de los datos rompe la relacion entre tablas o el id q se ingreso no existe, se abrira una ventana mencionando el error
### Eliminar
al ejecutar este boton se abre una ventana mostrando las opciones de tabla para eliminar registros, dependiendo de que tabla elija el usuario se mostrara una ventana pidiendo un ID que varia segun la tabla que se haya elejido si existe un registro con este ID se mostrara una ventana informando que la eliminacion a sido exitosa
### Migrar a MYSQL
cuando se ejecute este boton se van a migrar todas las tablas de ServerSQL con sus respectivos datos a la base de datos hecha en MySQL si se hizo alguna modificacion desde la aplicacion esta igual se pasara

## Diagrama de la Base de Datos
![image](https://github.com/user-attachments/assets/1c329b40-071a-4ddf-8d17-029e7ba8c6ab)
