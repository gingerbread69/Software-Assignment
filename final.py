import tkinter as tk
import random
import vlc

songs = ["1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav", "10.wav", "11.wav", "12.wav", "13.wav", "14.wav", "15.wav", "16.wav", "17.wav", "18.wav", "19.wav", "20.wav"]

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



def stop_song():
    player.stop()

def pause_song():
    player.pause()

def resume_song():
    player.play()

window = tk.Tk()
window.geometry("420x420")
window.title("Song Randomizer")

song_label = tk.Label(window, text="")
song_label.pack(pady=10)

randomize_button = tk.Button(window, text="Randomize", command=randomize_song)
randomize_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop", command=stop_song)
stop_button.pack(pady=5)

song_count_label = tk.Label(window, text=f"Total Songs: {len(songs)}")
song_count_label.pack(pady=5)

pause_button = tk.Button(window, text="Pause", command=pause_song)
pause_button.pack(pady=5)

resume_button = tk.Button(window, text="Resume", command=resume_song)
resume_button.pack(pady=5)

#if vlc.EventType.MediaPlayerEndReached:
#    print("end")
#    randomize_song()


window.mainloop()

