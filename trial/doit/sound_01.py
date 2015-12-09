#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるように準備する

doit.play(18,440)   # 18番のGPIOを使ってドの音を鳴らす
doit.play(18,494)   # 18番のGPIOを使ってレの音を鳴らす

doit.term()         # あとかたづけ

