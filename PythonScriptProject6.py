import json
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Load JSON data
with open("C:/Users/user/Desktop/PythonScriptProject6/JsonProject6.Json", "r") as f:
    songs = json.load(f)

# Initialize the song index
song_index = 0

# Initialize playback progress
is_playing = True  # Placeholder for play/pause control

# Function to update the progress bar
def update_progress_bar(duration_seconds):
    scale_progress.config(to=duration_seconds)  # Set the max value for Scale
    scale_progress.set(0)  # Reset the scale to the start

    # Simulate progress update only if the song is playing
    def progress():
        if is_playing:
            current_value = scale_progress.get()
            if current_value < duration_seconds:
                scale_progress.set(current_value + 1)  # Increment by 1 second
                root.after(1000, progress)  # Update every second

    progress()  # Start updating the progress

# Function to handle manual change on progress bar
def on_scale_change(event):
    new_time = scale_progress.get()
    # Here, you would typically set the playback position to `new_time`.
    # For now, we are simulating this by updating the scale without real audio.

# Update song display
def display_song(index):
    song = songs[index]

    # Update song details
    title_label.config(text="Title: " + song['title'])
    desc_label.config(text="Description: " + song['description'])
    duration_label.config(text="Duration: " + song['duration'])

    # Reset and start the progress bar
    duration_in_seconds = int(song['duration'].split()[0]) * 60  # Assuming duration format is "X mins"
    update_progress_bar(duration_in_seconds)

    # Update favorite icon
    if song['favorite']:
        favorite_label.config(image=fav_icon)
    else:
        favorite_label.config(image=non_fav_icon)

    # Update album art
    img = Image.open(song['image'])
    img = img.resize((150, 150), Image.LANCZOS)
    album_art = ImageTk.PhotoImage(img)
    image_label.config(image=album_art)
    image_label.image = album_art  # Keep a reference to avoid garbage collection

# Button commands
def next_song():
    global song_index
    song_index = (song_index + 1) % len(songs)
    display_song(song_index)

def prev_song():
    global song_index
    song_index = (song_index - 1) % len(songs)
    display_song(song_index)

# Tkinter setup
root = tk.Tk()
root.title("Spotify Style Music Player")
root.configure(bg="black")  # Set the main window background color to black

# Labels for song details with black background and white text
title_label = Label(root, text="", font=("Helvetica", 16, "bold"), bg="black", fg="white")  # Increased font size
desc_label = Label(root, text="", font=("Helvetica", 14), bg="black", fg="white")  # Increased font size
duration_label = Label(root, text="", font=("Helvetica", 14), bg="black", fg="white")  # Increased font size
favorite_label = Label(root, bg="black")

# Album art display with black background
image_label = Label(root, bg="black")

# Load favorite icon
fav_img = Image.open("C:/Users/user/Desktop/projectpictures/arrietty.jpg")  # Path to favorite icon image
fav_img = fav_img.resize((30, 30), Image.LANCZOS)  # Adjust size as needed for the icon
fav_icon = ImageTk.PhotoImage(fav_img)

# Use the same image for non-favorite icon as a placeholder
non_fav_icon = fav_icon  # Use favorite icon as a placeholder for non-favorite icon

# Create the Scale widget for interactive progress control with black background
scale_progress = tk.Scale(root, from_=0, to=100, orient="horizontal", length=400, showvalue=False,  # Increased length
                          bg="black", fg="white", troughcolor="gray", sliderrelief="flat", highlightthickness=0)
scale_progress.bind("<B1-Motion>", on_scale_change)  # Enable scrubbing when dragging

# Arrange Labels and Image
image_label.pack(pady=20)
title_label.pack(pady=10)  # Added padding for better spacing
desc_label.pack(pady=5)  # Added padding for better spacing
duration_label.pack(pady=5)  # Added padding for better spacing
favorite_label.pack(pady=10)
scale_progress.pack(pady=10)  # Add the progress Scale below duration label

# Buttons for song navigation with black background and white text
prev_button = Button(root, text="<< Prev", command=prev_song, bg="black", fg="white", font=("Helvetica", 14))  # Increased font size
next_button = Button(root, text="Next >>", command=next_song, bg="black", fg="white", font=("Helvetica", 14))  # Increased font size
prev_button.pack(side=tk.LEFT, padx=20, pady=20)  # Added padding for better spacing
next_button.pack(side=tk.RIGHT, padx=20, pady=20)  # Added padding for better spacing

# Display the first song
display_song(song_index)

root.mainloop()
