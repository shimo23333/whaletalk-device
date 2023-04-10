# !/usr/bin/python 
# coding:utf-8 


import time
from LedControl import LedControl

led = LedControl()

led.boot()
time.sleep(1)

led.fetching()
time.sleep(5)

led.fetching()
time.sleep(5)

led.fetching()