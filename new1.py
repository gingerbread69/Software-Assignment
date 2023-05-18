import tkinter as tk
import random
import os
songs = [
]
vid = random.randint(1, 2)
def randomize_song():
    random_song = random.choice(songs)
    song_label.configure(text=random_song)

window = tk.Tk()
window.title("Song Randomizer")

song_label = tk.Label(window, text="")
song_label.pack(pady=10)

randomize_button = tk.Button(window, text="Randomize", command=os.system(f"xdg-open {vid}.mp4"))
randomize_button.pack(pady=5)

window.mainloop()

