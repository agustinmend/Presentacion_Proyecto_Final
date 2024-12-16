import tkinter as tk
from PIL import Image, ImageTk

def wallpaper(tkinter_root):
    # Open the wallpaper image
    wllppr = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png")
    
    # Resize it to fit the screen size
    wllppr = wllppr.resize((tkinter_root.winfo_screenwidth(), tkinter_root.winfo_screenheight()))  
    
    # Convert it to a format Tkinter can use
    wllppr = ImageTk.PhotoImage(wllppr)  
    
    # Create a Label widget to display the wallpaper as the background
    label = tk.Label(tkinter_root, image=wllppr)
    label.place(x=0, y=0, relwidth=1, relheight=1)  # Place it to fill the entire window
    
    # Keep a reference to the image to prevent garbage collection
    label.image = wllppr  # This line ensures the image is kept in memory

def label_wallpaper(tkinter_root):
    bc = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png")
    bc_tk = ImageTk.PhotoImage(bc)

    return bc_tk

def label_wallpaper_2(tkinter_root, label):
    # Open the image for the wallpaper
    bc = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png")
    
    # Resize the image to match the size of the label widget
    label_width = label.winfo_width()
    label_height = label.winfo_height()
    bc = bc.resize((label_width, label_height), Image.ANTIALIAS)
    
    # Convert it to a format that Tkinter can use
    bc_tk = ImageTk.PhotoImage(bc)
    
    # Return the resized image (not the label)
    return bc_tk