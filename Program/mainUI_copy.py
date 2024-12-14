import pygame
import sounds
import images
import tkinter as tk
from tkinter import ttk
from threading import Thread
import queue
from PIL import Image, ImageTk
import main
from dataclasses import dataclass, field

pygame.init()

music_queue = queue.Queue()

def start_music():
    sounds.background_music(music_queue, root)

@dataclass
class MenuConfig:
    frame: tk.Frame = None
    start_button: tk.Button = None
    label_logo: tk.Label = None
    holabvnd: tk.Label = None
    last_action: str = None
    current_widget: tk.Widget = None

@dataclass
class TablesConfig:
    frame: tk.Frame = None
    last_action: str = None
    selected_table: dict = field(default_factory=dict)

@dataclass
class RootConfig:
    root: tk.Tk = field(default_factory=tk.Tk)
    logo_img_tk: ImageTk.PhotoImage = None
    menu: MenuConfig = field(default_factory=MenuConfig)
    tables: TablesConfig = field(default_factory=TablesConfig)

root_config = RootConfig()
root = root_config.root
root.title("Residencial al cubo")
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=1)
root.geometry("500x500")

frame_wpp = images.label_wallpaper(root)
images.wallpaper(root)

music_thread = Thread(target=start_music, daemon=True)
music_thread.start()

logo_img = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/logo.png")
logo_img_tk = ImageTk.PhotoImage(logo_img)
root_config.menu.label_logo = tk.Label(root, image=logo_img_tk, bd=0)

root_config.menu.holabvnd = tk.Label(root, text="Welcome to", font=("Minecraft", 15), bg="#777777", fg="#ffffff")

root_config.menu.start_button = tk.Button(
    root, 
    text="Start", 
    font=("Minecraft", 20),
    bg="#777777",
    fg="#ffffff",
    relief="raise",
    command=lambda: (sounds.click(), menu())
)

def configure_menu_grid(frame):
    """Configura pesos para filas y columnas de un marco."""
    for i in range(5):  # cinco filas (botones y espacio)
        frame.rowconfigure(i, weight=1)
    for j in range(2):  # Dos columnas
        frame.columnconfigure(j, weight=1)

def init_menu_widgets():
    root_config.menu.label_logo.grid(row=1, column=0, sticky="n", padx=20, pady=20)
    root_config.menu.holabvnd.grid(row=0, column=0, sticky="n")
    root_config.menu.holabvnd.grid_configure(padx=20, pady=20)
    root_config.menu.start_button.place(relx=0.5, rely=0.5, anchor="center")

init_menu_widgets()

def set_action_and_navigate(action):
    root_config.menu.last_action = action
    tables_buttons()

def menu():
    root_config.menu.start_button.place_forget() 
    root_config.menu.label_logo.grid_forget()    
    root_config.menu.holabvnd.grid_forget()

    if root_config.menu.frame is None:
        root_config.menu.frame = tk.Frame(root)
        configure_menu_grid(root_config.menu.frame)
        
        images.wallpaper(root_config.menu.frame)
        root.grid_rowconfigure(0, weight=1)        
        root.grid_columnconfigure(0, weight=1)      
        tm_img = images.label_wallpaper(root_config.menu.frame)
        title_menu = tk.Label(
            root_config.menu.frame, 
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

        visualize_button = tk.Button(
            root_config.menu.frame,
            text="Visualize\nRegisters",
            bg="#777777",
            fg="#ffffff",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), 
                             set_action_and_navigate("visualize"))
        )
        visualize_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        add_button = tk.Button(
            root_config.menu.frame,
            text="Add Registers",
            bg="#777777",
            fg="#ffffff",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), 
                             set_action_and_navigate("register"))
        )
        add_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        modify_button = tk.Button(
            root_config.menu.frame,
            text="Modify\nRegisters",
            bg="#777777",
            fg="#ffffff",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), 
                             set_action_and_navigate("modify"))
        )
        modify_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        delete_button = tk.Button(
            root_config.menu.frame,
            text="Delete\nRegisters",
            bg="#777777",
            fg="#ffffff",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), 
                             set_action_and_navigate("delete"))
        )
        delete_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        back_button = tk.Button(
            root_config.menu.frame,
            text="Back",
            bg="#777777",
            fg="#f5dc3b",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), go_back())
        )
        back_button.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=10, pady=10)

        migrate_button = tk.Button(
            root_config.menu.frame,
            text="Migrate\nDatabase\nto MySQL",
            bg="#777777",
            fg="#ffffff",
            font=("Minecraft", 20),
            command=lambda: (sounds.click())
        )
        migrate_button.grid(row=3, column=1, columnspan=1, sticky="nsew", padx=10, pady=10)
    root_config.menu.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

def go_back():
    global root_config
    if root_config.menu.frame is not None:
        root_config.menu.frame.grid_forget()
        root_config.menu.frame = None
    root.grid_rowconfigure(0, weight=0)
    root.grid_columnconfigure(0, weight=1)
    init_menu_widgets()

def tables_buttons():
    global root_config
    root_config.menu.frame.grid_forget()

    if root_config.tables.frame is None:
        root_config.tables.frame = tk.Frame(root)
        configure_menu_grid(root_config.tables.frame)

        images.wallpaper(root_config.tables.frame)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        images.wallpaper(root_config.tables.frame)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        tm_img = images.label_wallpaper(root_config.tables.frame)
        title_menu = tk.Label(
            root_config.tables.frame, 
            text=f"On what do you want to {root_config.menu.last_action}?", 
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

        selected_table = {"first": root_config.menu.last_action, "second": None}

        staff_button = tk.Button(
            root_config.tables.frame,
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

        back_button = tk.Button(
            root_config.tables.frame,
            text="Back",
            bg="#777777",
            fg="#f5dc3b",
            font=("Minecraft", 20),
            command=lambda: (sounds.click(), go_back_to_menu())
        )
        back_button.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    root_config.tables.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

def go_back_to_menu():
    global root_config
    if root_config.tables.frame is not None:
        root_config.tables.frame.grid_forget()
        root_config.tables.frame = None
    menu()

def action_table(selected_table):
    # Introduce the code for actions here
    pass

root.mainloop()