import time
from pygame import mixer

mixer.init(devicename="snd_rpi_hifiberry_dac")
mixer.music.load("sample-15s.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
