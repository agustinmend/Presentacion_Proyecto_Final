import pygame
import random
import time # asegurar que no se sobresature la cpu
import queue  # Import queue here as it's used in the module

# Flag to stop music thread
music_running = True

def click():
    click_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/mcbuttonsound.mp3")
    click_sound.play()

def succed_task():
    xp_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/minecraft_xp_sound.mp3")
    xp_sound.play()

def background_music(music_queue, root):  # Add root as an argument
    # Initialize mixer if not already initialized
    pygame.mixer.init()

    music_list = {
        1: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Cat.mp3",
        2: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Danny.mp3",
        3: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Haggstorm.mp3",
        4: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Living_Mice.mp3",
        5: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Minecraft.mp3",
        6: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Moog_City.mp3",
        7: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Oxygene.mp3",
        8: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Subwoofer_Lullaby.mp3",
        9: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Sweden.mp3",
        10: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Wet_Hands.mp3",
        11: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/Pigstep.mp3",
        12: "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/Jack_black_song.mp3"
    }

    song_keys = list(music_list.keys())
    odds = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.1]

    def play_random_song():
        selected_key = random.choices(song_keys, weights=odds, k=1)[0]
        selected_song = music_list[selected_key]
        pygame.mixer.music.load(selected_song)

    def music_loop():
        while music_running:
            play_random_song()
            music_queue.put(True)  # Signal the main thread to play music
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)  # Wait until the music finishes

            time.sleep(1)  # Wait before playing the next song
    
    def handle_music():
        if not music_queue.empty():
            music_queue.get()  # Remove any old messages
            pygame.mixer.music.play()  # Play music (only from main thread)

    root.after(100, handle_music)  # Keep checking every 100ms

    # Start the music loop in a separate thread
    music_loop()

    # Define a function to stop the music when the program is closing
    def on_closing():
        global music_running
        music_running = False  # Stop the music thread
        pygame.mixer.music.stop()  # Stop any music playing
        root.destroy()  # Close the Tkinter window

    # Set the Tkinter window close event
    root.protocol("WM_DELETE_WINDOW", on_closing)