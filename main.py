import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Create the Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("MP3 File Searcher and Player")

# Create a label for the search directory path
path_label = tk.Label(window, text="Search Directory:")
path_label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry field for the search directory path
path_entry = tk.Entry(window, width=50)
path_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a function to browse for the search directory path
def browse_directory():
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, directory)

# Create a button to browse for the search directory path
browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Create a listbox to display the search results
results_listbox = tk.Listbox(window, width=100)
results_listbox.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# Create a function to search for all MP3 files in the specified directory
def search_for_mp3_files():
    results_listbox.delete(0, tk.END)
    directory = path_entry.get()
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    for file in mp3_files:
        results_listbox.insert(tk.END, file)
    if mp3_files:
        play_button.grid(row=2, column=1, padx=5, pady=5)
        pause_button.grid(row=2, column=2, padx=5, pady=5)
        volume_slider.grid(row=2, column=3, padx=5, pady=5)

# Create a button to start the search
search_button = tk.Button(window, text="Search", command=search_for_mp3_files)
search_button.grid(row=2, column=0, padx=5, pady=5)

# Create a function to play the selected MP3 file
def play_mp3_file():
    # Get the selected file path from the listbox
    file_path = results_listbox.get(tk.ACTIVE)
    # Load the MP3 file using Pygame mixer
    pygame.mixer.music.load(file_path)
    # Set the volume to the current value of the volume slider
    pygame.mixer.music.set_volume(volume_slider.get() / 100)
    # Play the MP3 file using Pygame mixer
    pygame.mixer.music.play()

# Create a button to play the selected MP3 file
play_button = tk.Button(window, text="Play", command=play_mp3_file)

# Create a function to pause the currently playing MP3 file
def pause_mp3_file():
    # Pause the currently playing MP3 file using Pygame mixer
    pygame.mixer.music.pause()
    # Remove the "Pause" button
    pause_button.grid_forget()
    # Add the "Resume" button
    resume_button.grid(row=2, column=2, padx=5, pady=5)
    # Remove the volume slider
    volume_slider.grid_forget()

# Create a button to pause the currently playing MP3 file
pause_button = tk.Button(window, text="Pause", command=pause_mp3_file)

# Create a function to resume the currently paused MP3 file
def resume_mp3_file():
    # Resume the currently paused MP3 file using Pygame mixer
    pygame.mixer.music.unpause()
    # Remove the "Resume" button
    resume_button.grid_forget()
    # Add the "Pause" button
    pause_button.grid(row=2, column=2, padx=5, pady=5)
    # Add the volume slider
    volume_slider.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Create a button to resume the currently paused MP3 file
resume_button = tk.Button(window, text="Resume", command=resume_mp3_file)

# Create a function to adjust the volume of the currently playing MP3 file
def adjust_volume(volume):
    # Convert the volume scale from 0-100 to 0.0-1.0
    volume = float(volume) / 100
    # Set the volume of the currently playing MP3 file using Pygame mixer
    pygame.mixer.music.set_volume(volume)

# Create a volume slider to adjust the volume of the currently playing MP3 file
volume_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=adjust_volume)

# Start the Tkinter event loop
window.mainloop()

# Quit Pygame mixer when the window is closed
pygame.mixer.quit()
