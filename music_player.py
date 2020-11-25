#coding:utf-8

""" A music player programm by Baimam Boukar Jean Jacques """

from pygame import mixer
from tkinter import *


mixer.init()

mixer.music.load("song.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

print("[WELCOMING]: Muzicker Player")
while True:
	print("PRESS P TO PAUSE")
	print("PRESS R TO RESUME")
	print("PRESS V TO SET VOLUME")
	print("PRESS E TO EXIT")

	pressed = input("['P', 'R', 'V', 'E']")

	if(pressed == "P"):
		mixer.music.pause()
	elif pressed == 'R':
		mixer.music.unpause()
	elif pressed == 'V':
		volume = float(input("Please specify the volume set to apply: "))
		mixer.music.set_volume(volume)
	elif pressed == 'E':
		mixer.music.stop()
		break