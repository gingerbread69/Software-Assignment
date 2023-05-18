import random
import os
import time


random_video = random.randint(1, 2)

os.system(f"xdg-open {random_video}.mp4")
os.kill(f"{vid}.mp4")

