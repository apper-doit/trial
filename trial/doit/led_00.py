#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doit         # プログラムを書きやすくするおまじない

"""
プログラム本体

"""
doit.init()         # じゅんび（初期化）

doit.setupPin(18)   # 18番のGPIOを使えるようにする

doit.on(18)         # 18番のGPIOをONにする

doit.wait()         # Enter入力まち

doit.off(18)        # 18番のGPIOをOFFにする

doit.term()         # あとかたづけ

