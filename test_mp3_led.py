import time
from pygame import mixer
import os

os.system('ls')
os.system('sudo python3 led_test.py')

mixer.init(devicename="snd_rpi_hifiberry_dac")
mixer.music.load("sample-15s.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
