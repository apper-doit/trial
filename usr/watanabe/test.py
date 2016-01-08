from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.player.setTilePos(x,y+1,z)

mc.setBlock(x,y,z,57)





mc.postToChat("Hello Player")

