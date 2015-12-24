#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるようにする

doit.play(18,440)   # 18番のGPIOを使ってドの音をならす
doit.play(18,494)   # 18番のGPIOを使ってレの音をならす

doit.term()         # あとかたづけ

