import time
from pygame import mixer


mixer.init()
mixer.music.load("20a96-32nbe.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
