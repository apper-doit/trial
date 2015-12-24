#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

oto = [440, 494, 554, 587, 659, 740, 830, 880]

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるようにする

doit.play(18,oto[0])    # 18番のGPIOを使ってドの音をならす
doit.play(18,oto[1])    # 18番のGPIOを使ってレの音をならす
doit.play(18,oto[2])    # 18番のGPIOを使ってミの音をならす
doit.play(18,oto[3])    # 18番のGPIOを使ってファの音をならす
doit.play(18,oto[4])    # 18番のGPIOを使ってソの音をならす
doit.play(18,oto[5])    # 18番のGPIOを使ってラの音をならす
doit.play(18,oto[6])    # 18番のGPIOを使ってシの音をならす
doit.play(18,oto[7])    # 18番のGPIOを使ってドの音をならす

doit.term()         # あとかたづけ

