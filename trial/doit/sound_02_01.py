#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from doit import *  # プログラムを書きやすくするおまじない

oto = [ 440, 494, 554, 587, 659, 740, 830, 880 ]

init()         # じゅんび（初期化）

setupPin(18)   # 18番のGPIOを使えるようにする

for i in range(len(oto)):   # 「oto」に入っているデータ分だけくりかえす
    play(18,oto[i])    # 18番のGPIOを使ってドの音をならす

term()         # あとかたづけ

