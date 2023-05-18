import tkinter as tk
from tkinter import filedialog
import random
import vlc

songs = ["1.mp4", "2.mp4"]

player = vlc.MediaPlayer()

def update_song_count():
    count = len(songs)
    song_count_label.configure(text=f"Total Songs: {count}")

def randomize_song():
    if songs:
        random_song = random.choice(songs)
        song_label.configure(text=random_song)
        play_song(random_song)

def play_song(song):
    player.stop()  
    media = vlc.Media(song)
    player.set_media(media)
    player.play()

window = tk.Tk()
window.title("Song Randomizer")

song_label = tk.Label(window, text="")
song_label.pack(pady=10)

randomize_button = tk.Button(window, text="Randomize", command=randomize_song)
randomize_button.pack(pady=5)
song_count_label = tk.Label(window, text="Total Songs: 0")
song_count_label.pack(pady=5)

window.mainloop()

