#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

oto = [440, 494, 554, 587, 659, 740, 830, 880]

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるように準備する

for i in range(len(oto)):
    doit.play(18,oto[i])   # 18番のGPIOを使ってドの音を鳴らす

doit.term()         # あとかたづけ

