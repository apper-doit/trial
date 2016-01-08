#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from doit import *  # プログラムを書きやすくするおまじない

init()         # じゅんび（初期化）

setupPin(18)   # 18番のGPIOを使えるようにする

play(18,440)   # 18番のGPIOを使ってドの音をならす
play(18,494)   # 18番のGPIOを使ってレの音をならす

term()         # あとかたづけ

