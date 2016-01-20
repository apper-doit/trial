#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import RPi.GPIO as GPIO
import wiringpi2 as wiringpi
from time import sleep

##############################
#初期化
#    GPIO
#    WiringPi2
def init():
    GPIO.setmode(GPIO.BCM)
    wiringpi.wiringPiSetupGpio()

##############################
#特定のGPIOを使えるようにする
#   WiringPi softToneCreateも一緒に
def setupPin(pin, io=True):
    mode = GPIO.OUT
    if io == False:
       mode = GPIO.IN
    GPIO.setup(pin, mode)
    wiringpi.softToneCreate(pin)

##############################
#後始末
#   GPIOの片付け
def term():
    GPIO.cleanup()

##############################
#特定のGPIO制御(ON)
#   pin = GPIOの番号
#   delay = ONにした後待つ時間
def on(pin, delay=0.2):
    GPIO.output(pin, True)
    sleep(delay)

##############################
#特定のGPIO制御(OFF)
#   pin = GPIOの番号
#   delay = OFFにした後待つ時間
def off(pin, delay=0.2):
    GPIO.output(pin, False)
    sleep(delay)

##############################
#特定のGPIO制御(softTone)
#   pin = GPIOの番号
#   scale = 周波数
#   delay = 制御時間
def play(pin, scale, delay=0.2):
    wiringpi.softToneWrite(pin, scale)
    sleep(delay*2)
    wiringpi.softToneWrite(pin, 0)
    sleep(delay)

##############################
#Enter入力待ち
def wait():
    try:
        input('Enterを押してください')
    except SyntaxError:
        pass






