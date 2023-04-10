# !/usr/bin/python 
# coding:utf-8 

# API responce
# [
#   {
#     "id": 58,
#     "wid": "w001",
#     "uid": "grass",
#     "type": 2, // 1:text, 2:voice
#     "content": "uploads/voice/v-63d1586f96aed3.63499389.mp3",
#     "create_at": "2023-01-26 00:27:27",
#     "schedule_time": null
#   },
#   {
#     "id": 30,
#     "wid": "w001",
#     "uid": "grass",
#     "type": 1,
#     "content": "teset1234",
#     "create_at": "2022-11-26 20:51:38",
#     "schedule_time": null
#   },
#   ...
# ]

import time
import requests
import tempfile
import wget
from pygame import mixer
from threading import Timer
from termcolor import colored
from gtts import gTTS
import board
import neopixel
from LedControl import LedControl
import os
#from pydub import AudioSegment

fetch_timespan = 3

uid = "grass"
wid = "w001"

api_host = "https://whaletalk.tw/api/"
url_fetch_msg = "https://whaletalk.tw/api/Message/GetUnreadList?uid={}&wid={}".format(uid, wid)
url_msg_read = "https://whaletalk.tw/api/Message/SetRead"

led = LedControl()


def fetch_new_messages():
    cmd("led_fetch.py")
    try:
        r = requests.get(url_fetch_msg, timeout=10)
        return r.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def set_message_read(id):
    try:
        r = requests.get(url_msg_read+"?id={}".format(id), timeout=10)
        return r.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def play_msg(msg):
    print("play ID: {}".format(msg['id']))
    if msg['type'] == 1: play_msg_tts(msg['content'])
    if msg['type'] == 2: play_msg_mp3(api_host + msg['content'])


def play_msg_tts(sentence):
    print("[{}]: {}".format(colored("text", "cyan"), sentence.replace("\n", " ")))
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-tw')
        tts.save('{}.mp3'.format(fp.name))
        print("play...")
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)


def play_msg_mp3(url):
    print("[{}]: {}".format(colored("voice", "magenta"), url))
    print("downloading mp3...")
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        wget.download(url, '{}.mp3'.format(fp.name))

        #print("\nloudify...")
        #song = AudioSegment.from_mp3('{}.mp3'.format(fp.name))
        #louder_song = song + 12
        #louder_song.export('{}.mp3'.format(fp.name), format='mp3')

        print("\nplay...")
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.set_volume(2.5)
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)

def play_mp3(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(1)
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)


def cmd(filename):
    os.system("sudo python3 {}".format(filename))


def boot_action():
    cmd("led_boot_start.py")
    play_mp3("sounds/boot.mp3")
    cmd("led_boot_end.py")
    

boot_action()

while(True):
    # fetch new message
    print("fetching...")
    msgList = fetch_new_messages()

    if msgList and len(msgList) > 0:
    
        # play message
        for m in msgList:
            print("play: ({}) {}".format(m['id'], m['content']))
            play_msg(m)

            # set message as read
            set_message_read(m['id'])

            # wait for next message
            time.sleep(1)


    # wait for next fetch
    print("wait")
    time.sleep(5)
