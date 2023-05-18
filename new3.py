import tkinter as tk
from tkinter import filedialog
import random
import os
import pygame

pygame.mixer.init()

songs = []

def add_songs():
    filetypes = (("Text Files", "*.txt"), ("All Files", "*.*"))
    filename = filedialog.askopenfilename(title="Select Songs File", filetypes=filetypes)
    if filename:
        with open(filename, "r") as file:
            for line in file:
                song = line.strip()
                if song:
                    songs.append(song)
    update_song_count()

def update_song_count():
    count = len(songs)
    song_count_label.configure(text=f"Total Songs: {count}")

def randomize_song():
    if songs:
        random_song = random.choice(songs)
        song_label.configure(text=random_song)
        play_song(random_song)

def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

window = tk.Tk()
window.title("Song Randomizer")

song_label = tk.Label(window, text="")
song_label.pack(pady=10)

randomize_button = tk.Button(window, text="Randomize", command=randomize_song)
randomize_button.pack(pady=5)

add_songs_button = tk.Button(window, text="Add Songs", command=add_songs)
add_songs_button.pack(pady=5)

song_count_label = tk.Label(window, text="Total Songs: 0")
song_count_label.pack(pady=5)

window.mainloop()

