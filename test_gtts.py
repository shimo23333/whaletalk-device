import time
from gtts import gTTS
from pygame import mixer
import tempfile

text = "鄰居房子的側面木板墻，正對著我家餐室的窗戶。木板墻上有個小小的洞，每年春天，總有好多只麻雀飛來，從那洞里進進出出、嘰嘰喳喳的，似商量又似爭吵，顯然它們是在木板墻的夾縫中做窩。想來那里面的天地一定相當開闊，築巢其中，倒是風雨不動安如山呢。"

def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)

speak(text, 'zh-tw')