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

fetch_timespan = 3

api_host = "https://whaletalk.tw/api/"
msg_url = "https://whaletalk.tw/api/Message/GetMyList?uid=grass&wid=w001"

led = LedControl()


def check_new_messages():
    global url
    try:
        r = requests.get(msg_url, timeout=3)
        return r.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def preview_content(content):
    limit = 20
    if len(content) <= limit:
        return content.replace("\n", " ")[:limit]
    else:
        return content.replace("\n", " ")[:limit]+"..."

def print_message_list(list):
    for m in list:
        typ = ""
        if m['type'] == 1: typ = colored("text", "cyan")
        if m['type'] == 2: typ = colored("voice", "magenta")
        print("ID:{}\t[{}] {}  {}  {}".format(m['id'], typ, m['create_at'], m['schedule_time'], preview_content(m['content'])))


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
        print("\nplay...")
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)

def play_mp3(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(1)
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

def start():
    global t, fetch_timespan
    msgList = check_new_messages()
    if msgList == None:
        print("cannot fetch, retry in ",fetch_timespan,"sec...")
        t = Timer(fetch_timespan, fetch)
        t.start()
        return
    
    if len(msgList) <= 0:
        print("no message, retry in ",fetch_timespan,"sec...")
        t = Timer(fetch_timespan, fetch)
        t.start()
        return
    
    print("got", len(msgList), "datas:")
    print_message_list(msgList)
    play_msg(msgList[0])

    
    print("wait ",fetch_timespan,"sec...")
    t = Timer(fetch_timespan, fetch)
    t.start()


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
    time.sleep(1)

    # play message
    print("play message")
    time.sleep(1)

    # wait
    print("wait")
    time.sleep(3)
    


# led.fetching()

# fetch()
# def print_counter():
#     global t
#     print("hihi")

#     t = Timer(2, print_counter)
#     t.start()


# t = Timer(2, print_counter)
# t.start()


# mixer.init()
# mixer.music.load("sample-15s.mp3")
# mixer.music.play()
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)
