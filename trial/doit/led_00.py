#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from doit import *  # プログラムを書きやすくするおまじない

init()         # じゅんび（初期化）

setupPin(18)   # 18番のGPIOを使えるようにする

on(18)         # 18番のGPIOをONにする

wait()         # Enter入力まち

off(18)        # 18番のGPIOをOFFにする

term()         # あとかたづけ
