#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

"""
プログラム本体

"""
PIN = 18

doit.init()         # じゅんび（初期化）

doit.setupPin(PIN)   # 18番のGPIOを使えるようにする

for i in range(5):
    doit.on(PIN)         # 18番のGPIOをONにする
    doit.off(PIN)        # 18番のGPIOをOFFにする

doit.term()         # あとかたづけ

