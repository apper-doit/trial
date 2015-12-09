#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるように準備する

for i in range(5):
    doit.on(18)         # 18番のGPIOをONにする
    doit.off(18)

doit.term()         # あとかたづけ

