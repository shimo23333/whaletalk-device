# API 回傳格式：
# [
#   {
#     "id": 58,
#     "wid": "w001",
#     "uid": "grass",
#     "type": 2, // 1:文字, 2:語音
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

# 取得訊息的時間間隔
fetch_timespan = 3

# api 網址
api_host = "https://suc.tw/"
msg_url = "https://suc.tw/Message/GetMyList?uid=grass&wid=w001"


# 由 api 取得訊息資料
def check_new_messages():
    global url
    try:
        print("正在由 api 取得訊息: ", colored(msg_url, "green"))
        r = requests.get(msg_url, timeout=3)
        return r.json()
    except requests.exceptions.RequestException as e:
        print(colored("[錯誤]", "red"), " 無法取得 api 資料，請檢查下方錯誤訊息:")
        print(e)
        return None

# 取得預覽訊息內容
def preview_content(content):
    limit = 20
    if len(content) <= limit:
        return content.replace("\n", " ")[:limit]
    else:
        return content.replace("\n", " ")[:limit]+"..."


# 印出預覽訊息列表
def print_message_list(list):
    for m in list:
        typ = ""
        if m['type'] == 1: typ = colored("文字", "cyan")
        if m['type'] == 2: typ = colored("語音", "magenta")
        print("ID:{}\t[{}] {}  {}  {}".format(m['id'], typ, m['create_at'], m['schedule_time'], preview_content(m['content'])))


# 播放訊息
def play_msg(msg):
    print("播放訊息 ID: {}".format(msg['id']))
    if msg['type'] == 1: play_msg_tts(msg['content'])
    if msg['type'] == 2: play_msg_mp3(api_host + msg['content'])


# 播放文字訊息(tts)
def play_msg_tts(sentence):
    print("[{}]: {}".format(colored("文字", "cyan"), sentence.replace("\n", " ")))
    print("開始轉換文字為聲音檔...")
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-tw')
        tts.save('{}.mp3'.format(fp.name))
        print("轉換完畢，開始播放...")
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
    print("播放結束")


# 播放 mp3 訊息
def play_msg_mp3(url):
    print("[{}]: {}".format(colored("語音", "magenta"), url))
    print("開始下載語音檔mp3...")
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        wget.download(url, '{}.mp3'.format(fp.name))
        print("\n下載完畢，開始播放...")
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
    print("播放結束")


# 取得新訊息列表
def fetch():
    global t, fetch_timespan
    msgList = check_new_messages()
    if msgList == None:
        print("無法取得訊息，等待 ",fetch_timespan," 秒後重試...")
        t = Timer(fetch_timespan, fetch)
        t.start()
        return
    
    if len(msgList) <= 0:
        print("沒有新訊息，等待 ",fetch_timespan," 秒後重試...")
        t = Timer(fetch_timespan, fetch)
        t.start()
        return
    
    print("已取得", len(msgList), "筆資料:")
    print_message_list(msgList)
    play_msg(msgList[0])

    print("標記 xxx 已播放過")
    
    print("等待 ",fetch_timespan," 秒後重新獲取...")
    t = Timer(fetch_timespan, fetch)
    t.start()




# 開始
print("-----------------------")
print(colored("WhaleTalk", "yellow"), "啟動")
time.sleep(1)

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