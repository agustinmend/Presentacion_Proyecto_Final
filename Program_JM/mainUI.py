import pygame
import sounds
import images
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
import queue
from PIL import Image, ImageTk
import main
from main import connection_to_db  

pygame.init()

music_queue = queue.Queue() 

def start_music():
    sounds.background_music(music_queue, root)

menu_frame = None
current_widget = None
Start_button = None
label_logo = None
holabvnd = None
tables_frame = None
table_frame = None
last_action = None
error_label = None
mysql_frame = None

def configure_menu_grid(frame):
    """Configura pesos para filas y columnas de un marco."""
    for i in range(5):  # cinco filas (botones y espacio)
        frame.rowconfigure(i, weight=1)
    for j in range(2):  # Dos columnas
        frame.columnconfigure(j, weight=1)

# Inicializa la ventala raíz del Tkinter
root = tk.Tk()
root.title("Residencial al cubo")
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=1)
root.geometry("500x500")

frame_wpp = images.label_wallpaper(root)
images.wallpaper(root)

music_thread = Thread(target=start_music, daemon=True)
music_thread.start()


logo_img = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/logo.png") # Abre el logo 
logo_img_tk = ImageTk.PhotoImage(logo_img) # Carga la imagen para Tkinter
label_logo = tk.Label(root, image=logo_img_tk, bd=0) # Cargar la imagen en "root"

holabvnd = tk.Label(root, text="Welcome to", font=("Minecraft", 15), bg="#777777", fg="#ffffff")

def attempt_connection():
    """Attempts to connect to the database and handles errors."""
    global error_label  # To allow dynamic updates to the error message
    sounds.click()# Import connection function

    # Attempt to connect
    connection_result = connection_to_db()

    if connection_result[0]:  # Successful connection
        menu()
    else:  # Connection failed
        # If error label doesn't exist, create it
        if not error_label:
            error_label = tk.Label(root, text="", font=("Minecraft", 12), fg="red", bg="#000000", wraplength=900)
            error_label.grid(row=5, column=0, columnspan=2, pady=10)  # Place below the Start button
        # Update error message
        error_label.config(text=f"Error: {connection_result[1]}")

Start_button = tk.Button(root, 
                        text="Start", 
                        font=("Minecraft", 20),
                        bg="#777777",
                        fg="#ffffff",
                        relief="raise",
                        command=lambda: (sounds.click(), attempt_connection())
                        )

# funcion para mostrar widgets
def init_menu_widgets():
    label_logo.grid(row=1, column=0, sticky="n", padx=20, pady=20)
    holabvnd.grid(row=0, column=0, sticky="n")
    holabvnd.grid_configure(padx=20, pady=20)
    Start_button.place(relx=0.5, rely=0.5, anchor="center")

init_menu_widgets()

"""Función para guardar las acciones del usuario"""
def set_action_and_navigate(action):
    global last_action
    last_action = action
    tables_buttons()

"""Main menu: Menú principal donde se llevan a cabo todas las acciones que el usuario desee"""
def menu():
    global menu_frame, Start_button, label_logo, holabvnd, tm_img

    Start_button.place_forget() #
    label_logo.grid_forget()    # Esconder el menú donde se inicializó (lo que incluye el botón start, el logo y
    holabvnd.grid_forget()      # el texto por encima del logo).

    if menu_frame is None:
        menu_frame = tk.Frame(root)
        configure_menu_grid(menu_frame)
        
        images.wallpaper(menu_frame)                # Cargar el fondo del frame.
        root.grid_rowconfigure(0, weight=1)         # Configurar los ajustes del marco
        root.grid_columnconfigure(0, weight=1)      # de la ventana principal para adaptarse al nuevo menú.
        tm_img = images.label_wallpaper(menu_frame) # cargar el wallpaper del label para que se disuelva en el fondo.
        title_menu = tk.Label(menu_frame, 
                              text="What do you want to do?", 
                              font=("Minecraft", 17), 
                              fg="#ffffff",
                              image=tm_img,
                              compound="center",
                              bd=0,
                              highlightthickness=0,
                              width=5,
                              height=1
                              )
        title_menu.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=300, pady=10)

        """Botones del menú principal"""
        visualize_button = tk.Button(menu_frame,
                                  text="Visualize\nRegisters",
                                  bg="#777777",
                                  fg="#ffffff",
                                  font=("Minecraft", 20),
                                  command=lambda: (sounds.click(), 
                                                   set_action_and_navigate("visualize"))
                                  )
        visualize_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        add_button = tk.Button(menu_frame,
                              text="Add Registers",
                              bg="#777777",
                              fg="#ffffff",
                              font=("Minecraft", 20),
                                  command=lambda: (sounds.click(), 
                                                   set_action_and_navigate("add"))
                              )
        add_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        modify_button = tk.Button(menu_frame,
                               text="Modify\nRegisters",
                               bg="#777777",
                               fg="#ffffff",
                               font=("Minecraft", 20),
                                  command=lambda: (sounds.click(), 
                                                   set_action_and_navigate("modify"))
                               )
        modify_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        delete_button = tk.Button(menu_frame,
                               text="Delete\nRegisters",
                               bg="#777777",
                               fg="#ffffff",
                               font=("Minecraft", 20),
                                  command=lambda: (sounds.click(), 
                                                   set_action_and_navigate("delete"))
                               )
        delete_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        reverse_string_button = tk.Button(menu_frame,
                                          text="Reverse String",
                                          bg="#777777",
                                          fg="#ffffff",
                                          font=("Minecraft", 20),
                                          command=lambda: (sounds.click(),
                                                           set_action_and_navigate("Reverse string"))
                                          )
        reverse_string_button.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        back_button = tk.Button(menu_frame,
                             text="Back",
                             bg="#777777",
                             fg="#f5dc3b",
                             font=("Minecraft", 20),
                             command=lambda: (sounds.click(), go_back())
                             )
        back_button.grid(row=4, column=0, columnspan=1, sticky="nsew", padx=10, pady=10)

        migrate_button = tk.Button(menu_frame,
                                   text="Migrate\nDatabase\nto MySQL",
                                   bg="#777777",
                                   fg="#ffffff",
                                   font=("Minecraft", 20),
                                   command=lambda: (sounds.click(), migrationScreen())
                                   )
        migrate_button.grid(row=4, column=1, columnspan=1, sticky="nsew", padx=10, pady=10)
    menu_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Función para volver al menú principal de arranque
def go_back():
    global current_widget, Start_button, label_logo, holabvnd, menu_frame

    # esconder el menú de las acciones
    if menu_frame is not None:
        menu_frame.grid_forget()
        menu_frame = None
    # restaura la configuración original de la ventana
    root.grid_rowconfigure(0, weight=0)
    root.grid_columnconfigure(0, weight=1)
    # mostrar los widgets iniciales con el que se arrancó el programa otra vez
    init_menu_widgets()

"""Menu de las tablas: Estas permiten elegir que tabla quiere elegir el usuario para cualquier acción"""
def tables_buttons():
    global menu_frame, tables_frame, last_action
    menu_frame.grid_forget()

    if tables_frame is None:
        tables_frame = tk.Frame(root)
        configure_menu_grid(tables_frame)

        images.wallpaper(tables_frame)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        tm_img = images.label_wallpaper(tables_frame)
        title_menu = tk.Label(tables_frame, 
                                text=f"On what do you want to {last_action}?", 
                                font=("Minecraft", 17), 
                                fg="#ffffff",
                                image=tm_img,
                                compound="center",
                                bd=0,
                                highlightthickness=0,
                                width=5,
                                height=1
                            )
        title_menu.image = tm_img
        title_menu.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=300, pady=10)
        
        # Diccionario para guardar la siguiente acción para luego poder ejecutar la tarea requerida
        selected_table = {"first": last_action, "second": None}

        staff_button = tk.Button(tables_frame,
                                 text="Staff",
                                 bg="#777777",
                                 fg="#ffffff",
                                 font=("Minecraft", 20),
                                 command=lambda: (sounds.click(), 
                                                  selected_table.update(second="Staff"),
                                                  action_table(selected_table)
                                                 )
                                 )
        staff_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        payment_button = tk.Button(tables_frame,
                                   text="Payments",
                                   bg="#777777",
                                   fg="#ffffff",
                                   font=("Minecraft", 20),
                                   command=lambda: (sounds.click(), 
                                                    selected_table.update(second="Payment"),
                                                    action_table(selected_table)
                                                   )
                                  )
        payment_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        customer_button = tk.Button(tables_frame,
                                    text="Customers",
                                    bg="#777777",
                                    fg="#ffffff",
                                    font=("Minecraft", 20),
                                    command=lambda: (sounds.click(), 
                                                     selected_table.update(second="Customer"),
                                                     action_table(selected_table)
                                                    )
                                   )
        customer_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        maintinience_button = tk.Button(tables_frame,
                                        text="Maintinience",
                                        bg="#777777",
                                        fg="#ffffff",
                                        font=("Minecraft", 20),
                                        command=lambda: (sounds.click(), 
                                                         selected_table.update(second="Mantinience"),
                                                         action_table(selected_table)
                                                        )
                                       )
        maintinience_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        room_button = tk.Button(tables_frame,
                                text="Rooms",
                                bg="#777777",
                                fg="#ffffff",
                                font=("Minecraft", 20),
                                command=lambda: (sounds.click(), 
                                                 selected_table.update(second="Room"),
                                                 action_table(selected_table)
                                                )
                               )
        room_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        lease_button = tk.Button(tables_frame,
                                 text="Leases",
                                 bg="#777777",
                                 fg="#ffffff",
                                 font=("Minecraft", 20),
                                 command=lambda: (sounds.click(), 
                                                  selected_table.update(second="Lease"),
                                                  action_table(selected_table)
                                                  )
                                )
        lease_button.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

        back_button = tk.Button(tables_frame,
                                text="Back",
                                bg="#777777",
                                fg="#f5dc3b",
                                font=("Minecraft", 20),
                                command=lambda: (sounds.click(), go_back_to_menu())
                               )
        back_button.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    tables_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Función para volver al menu de las acciones
def go_back_to_menu():
    global tables_frame
    # Hide the tables frame and reset the grid configuration
    if tables_frame is not None:
        tables_frame.grid_forget()
        tables_frame = None
    menu()

"""Menú de una acción especifica para una tabla especifica elegida por el usuario (Función que interactua con la base de datos)"""

def action_table(selected_table):
    global tables_frame
    if selected_table['first'] == "visualize":
        # Fetch the data for the selected table
        data = main.show_table(selected_table['second'])  # Call function from the second script

        if data.empty:  # Handle empty data case
            tk.messagebox.showinfo("No Data", f"The {selected_table['second']} table has no data to display.")
            return

        # Create a new window to display the data
        data_window = tk.Toplevel(root)  # Opens a new window
        data_window.title(f"Data from {selected_table['second']} Table")
        data_window.geometry("600x400")  # Set window size

        # Add a Treeview widget
        tree = ttk.Treeview(data_window, columns=list(data.columns), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)  # Adjust column width as needed

        # Insert data into Treeview
        for _, row in data.iterrows():
            tree.insert("", tk.END, values=list(row))

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(data_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Optional: Horizontal scrollbar
        h_scrollbar = ttk.Scrollbar(data_window, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    elif selected_table['first'] == "add":
        # Fetch the table data to check if it's empty
        data = main.show_table(selected_table['second'])

        if data.empty:
            tk.messagebox.showinfo("No Data", f"The {selected_table['second']} table has no data to display.")
            return

        # Create the register window
        register_window = tk.Toplevel(root)
        register_window.title(f"Add data to the {selected_table['second']} table")
        register_window.geometry("600x400")

        # Background image setup
        image_path = "C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png"
        img = Image.open(image_path)

        # Function to resize the image dynamically when the window is resized
        def resize_image(event):
            new_width, new_height = event.width, event.height
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(resized_img)
            bg_label.configure(image=img_tk)
            bg_label.image = img_tk  # Keep a reference to prevent garbage collection

        # Create a Label widget for the background image
        bg_label = tk.Label(register_window)
        bg_label.grid(row=0, column=0, rowspan=100, columnspan=100, sticky="nsew")

        # Bind the window resize event to the resize_image function
        register_window.bind("<Configure>", resize_image)

        # Enable grid layout for the entire window
        register_window.grid_rowconfigure(0, weight=1)
        register_window.grid_columnconfigure(0, weight=1)

        # Fetch column names from the table
        columns = main.get_column_names(selected_table['second'])
        
        entries = {}  # Dictionary to hold references to entry widgets

        for i, column in enumerate(columns):
            label = tk.Label(register_window, text=column, bg="#777777", fg="#ffffff", font=("Minecraft", 16))
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

            reg_entry = tk.Entry(register_window)
            reg_entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="ew")
            entries[column] = reg_entry  # Save entry reference with column name as key

        # Function to handle data insertion
        def handle_insert():
            sounds.click()
            values = {column: entry.get() for column, entry in entries.items()}
            success = main.insert_data(main.con, selected_table['second'], values)
            if success:
                sounds.succed_task()
                register_window.destroy()
            else:
                tk.messagebox.showerror("Error", "Failed to insert data.\nPK exists")

        # Submit button to add data
        submit_button = tk.Button(register_window, 
                                  text="Add", 
                                  command=handle_insert, 
                                  bg="#4CAF50", 
                                  fg="#ffffff", 
                                  font=("Minecraft", 14))
        submit_button.grid(row=len(columns) + 1, column=1, padx=10, pady=10, sticky="e")
    
    elif selected_table['first'] == "modify":
        # Fetch the table data to check if it's empty
        data = main.show_table(selected_table['second'])

        if data.empty:
            tk.messagebox.showinfo("No Data", f"The {selected_table['second']} table has no data to display.")
            return

        # Create the register window
        modify_window = tk.Toplevel(root)
        modify_window.title(f"Modify data in the {selected_table['second']} table")
        modify_window.geometry("600x400")

        # Background image setup
        image_path = "C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png"
        img = Image.open(image_path)

        # Function to resize the image dynamically when the window is resized
        def resize_image(event):
            new_width, new_height = event.width, event.height
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(resized_img)
            bg_label.configure(image=img_tk)
            bg_label.image = img_tk  # Keep a reference to prevent garbage collection

        # Create a Label widget for the background image
        bg_label = tk.Label(modify_window)
        bg_label.grid(row=0, column=0, rowspan=100, columnspan=100, sticky="nsew")

        # Bind the window resize event to the resize_image function
        modify_window.bind("<Configure>", resize_image)

        # Enable grid layout for the entire window
        modify_window.grid_rowconfigure(0, weight=1)
        modify_window.grid_columnconfigure(0, weight=1)

        # Fetch column names from the table
        columns = main.get_column_names(selected_table['second'])
        treeview = ttk.Treeview(modify_window, columns=columns)
        entries = {}  # Dictionary to hold references to entry widgets

        for i, column in enumerate(columns):
            label = tk.Label(modify_window, text=column, bg="#777777", fg="#ffffff", font=("Minecraft", 16))
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

            mod_entry = tk.Entry(modify_window)
            mod_entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="ew")
            entries[column] = mod_entry  # Save entry reference with column name as key
            new_values: list = mod_entry.get()

        # Function to handle data update
        def handle_update():
            sounds.click()

            # Fetch primary key column name
            PK_mod_table = main.getTablePK(selected_table['second'])

            # Gather all updated values from the entries
            new_values = [mod_entry.get() for mod_entry in entries.values()]  # Obtener valores de las entradas
            
            # Asegúrate de agregar el valor para la clave primaria (último parámetro esperado por la consulta)
            pk_value = entries[PK_mod_table].get()  # Asegúrate de que la clave primaria esté incluida
            new_values.append(pk_value)

            success = main.update_data(selected_table['second'], PK_mod_table, list(entries.keys()), new_values)

            if success:
                sounds.succed_task()
                modify_window.destroy()  # Cerrar la ventana de modificación
            else:
                tk.messagebox.showerror("Error", "Failed to modify data.")
        
        # Submit button to modify data
        submit_button = tk.Button(modify_window, 
                                text="Modify", 
                                command=handle_update, 
                                bg="#777777", 
                                fg="#ffffff", 
                                font=("Minecraft", 14))
        submit_button.grid(row=len(columns) + 1, column=1, padx=10, pady=10, sticky="e")

        tip = tk.Label(modify_window,
                        text="TIP: The minimun amount of rows is 16\nif you want to\nclear data, you can\nuse this option\nto delete data\nby leaving blank all entries\nexcept the Table PK\n(EX: 101 to 116 or 1 to 16)",
                        bg="#777777",
                        fg="#ffffff",
                        font=("Minecraft", 12),
                        compound="center")
        tip.grid(row=len(columns) + 2, column=1, padx=10, pady=10, sticky="e")

    elif selected_table['first'] == "delete":
        data = main.show_table(selected_table['second'])

        if data.empty:
            tk.messagebox.showinfo("No Data", f"The {selected_table['second']} table has no data to display.")
            return

        # Create the register window
        delete_window = tk.Toplevel(root)
        delete_window.title(f"Modify data in the {selected_table['second']} table")
        delete_window.geometry("600x400")

        # Background image setup
        image_path = "C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png"
        img = Image.open(image_path)

        # Function to resize the image dynamically when the window is resized
        def resize_image(event):
            new_width, new_height = event.width, event.height
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(resized_img)
            bg_label.configure(image=img_tk)
            bg_label.image = img_tk  # Keep a reference to prevent garbage collection

        # Create a Label widget for the background image
        bg_label = tk.Label(delete_window)
        bg_label.grid(row=0, column=0, rowspan=100, columnspan=100, sticky="nsew")

        # Bind the window resize event to the resize_image function
        delete_window.bind("<Configure>", resize_image)

        # Enable grid layout for the entire window
        delete_window.grid_rowconfigure(0, weight=1)
        delete_window.grid_columnconfigure(0, weight=1)
        
        Primary_key = main.getTablePK(selected_table['second'])

        label = tk.Label(delete_window, text=f"{selected_table['second']}ID", bg="#777777", fg="#ffffff", font=("Minecraft", 16))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        del_entry = tk.Entry(delete_window)
        del_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")


        def handle_delete():
            sounds.click()
            success = main.delete_data(selected_table['second'], Primary_key, del_entry.get())

            if success:
                sounds.succed_task()
            else:
                tk.messagebox.showerror("Error", "Failed to delete data.\nImportant row or non-existent")
            
        submit_button = tk.Button(delete_window, 
                            text="Delete", 
                            command=handle_delete, 
                            bg="#ff2450", 
                            fg="#ffffff", 
                            font=("Minecraft", 14))
        submit_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
    
    elif selected_table['first'] == "Reverse string":
        data = main.show_table(selected_table['second'])
        if data.empty:
            tk.messagebox.showinfo("No Data", f"The {selected_table['second']} table has no data to display.")
            return

        success = main.clone_reversed_columns(selected_table['second'])
        if success:
            sounds.succed_task()
        else:
            tk.messagebox.showerror("Error", "Failed to clone reversed columns")

"""Migracion a MySQL"""
def migrationScreen():
    global menu_frame, mysql_frame
    menu_frame.grid_forget()
    if mysql_frame is None:
        mysql_frame = tk.Frame(root)
        configure_menu_grid(mysql_frame)

        images.wallpaper(mysql_frame)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        tm_img = images.label_wallpaper(mysql_frame)
        title_menu = tk.Label(mysql_frame, 
                                text="Do you want to migrate the database to mySQL?", 
                                font=("Minecraft", 17), 
                                fg="#ffffff",
                                image=tm_img,
                                compound="center",
                                bd=0,
                                highlightthickness=0,
                                width=7,
                                height=1
                            )
        title_menu.image = tm_img
        title_menu.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=300, pady=10)

        yes_button = tk.Button(mysql_frame,
                               text="Yes",
                               font=("Minecraft", 30),
                               fg="#ffffff",
                               bg="#777777",
                               command=lambda: (sounds.click(), main.connection_to_mySQL(), (main.migrar_datos()))
                               )
        yes_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        no_button = tk.Button( mysql_frame,
                               text="No",
                               font=("Minecraft", 30),
                               fg="#ffffff",
                               bg="#777777",
                               command=lambda: (sounds.click(), go_back_from_mysql())
                               )
        no_button.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    mysql_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

def go_back_from_mysql():
    global mysql_frame
    # Hide the tables frame and reset the grid configuration
    if mysql_frame is not None:
        mysql_frame.grid_forget()
        mysql_frame = None
    menu()

root.mainloop()