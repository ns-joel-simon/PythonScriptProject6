import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch tracks from Jamendo API
def fetch_tracks():
    url = "https://api.jamendo.com/v3.0/tracks?client_id=69c41af2&format=json&limit=10"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Function to display tracks in the GUI
def display_tracks(tracks):
    for track in tracks:
        # Create a frame for each track
        track_frame = ttk.Frame(root)
        track_frame.pack(fill=tk.X, padx=5, pady=5)

        # Track details
        track_label = ttk.Label(track_frame, text=f"Track: {track['name']} by {track['artist_name']}, Duration: {track['duration']} seconds")
        track_label.pack(side=tk.LEFT)

        # Play button
        play_button = ttk.Button(track_frame, text="Play", command=lambda audio=track['audio']: play_audio(audio))
        play_button.pack(side=tk.RIGHT)

# Dummy function for playing audio (to be implemented)
def play_audio(audio_url):
    print(f"Playing audio from: {audio_url}")

# Create the main window
root = tk.Tk()
root.title("Jamendo Tracks")

# Fetch and display tracks
tracks = fetch_tracks()
display_tracks(tracks)

# Start the Tkinter event loop
root.mainloop()

