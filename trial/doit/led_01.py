#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from doit import *  # プログラムを書きやすくおまじない

PIN = 18

init()         # じゅんび（初期化）

setupPin(PIN)   # 18番のGPIOを使えるようにする

for i in range(5):
    on(PIN)         # 18番のGPIOをONにする
    off(PIN)        # 18番のGPIOをOFFにする

term()         # あとかたづけ

