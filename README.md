# MP3_manager

This is a Python program that creates a simple graphical user interface (GUI) using the Tkinter library. The program allows the user to search for MP3 files in a specified directory, display the search results in a listbox, and play the selected MP3 file.

The program uses the os module to search for MP3 files in the specified directory and the pygame module to play the MP3 files. The Pygame mixer is initialized at the beginning of the program and is quit when the Tkinter event loop is exited.

The GUI contains a label and an entry field for the search directory path, a button to browse for the search directory path, a button to start the search, a listbox to display the search results, a button to play the selected MP3 file, a button to pause the currently playing MP3 file, a button to resume the currently paused MP3 file, and a volume slider to adjust the volume of the currently playing MP3 file.

When the user clicks the "Search" button, the program searches for all MP3 files in the specified directory and displays the file paths in the listbox. If the listbox is not empty, the "Play" and "Pause" buttons and the volume slider are displayed. When the user clicks the "Play" button, the program loads and plays the selected MP3 file using Pygame mixer. The "Pause" button pauses the currently playing MP3 file, and the "Resume" button resumes the currently paused MP3 file. The volume slider adjusts the volume of the currently playing MP3 file.
