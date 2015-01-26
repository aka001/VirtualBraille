import os
from pytesser import *
import sys
import picamera
import PIL
import time

def tts(text):
      return os.system("espeak  -s 155 -a 200 "+text+" " )
cnt=1
while(1):
	camera=picamera.PiCamera()
	camera.capture('image.jpg')
	#img_file=raw_input()
	img_file='image.jpg'
	image=Image.open(img_file).convert('RGB')
	text=image_to_string(image)
	print text
	text='\''+text+'\''
	tts(text)
	cnt+=1
	camera.close()
	time.sleep(0.1)
