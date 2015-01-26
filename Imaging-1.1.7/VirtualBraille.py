from PIL import Image
import webcolors
import numpy as np
import picamera
import os

def tts(text):
      return os.system("espeak  -s 155 -a 200 "+text+" " )

camera=picamera.PiCamera()
camera.capture('image.jpg')
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return closest_name


image_recieved=Image.open("image.jpg")
print image_recieved
image_array=np.asarray(image_recieved)
r=0
g=0
b=0
cnt=0
for i in range(image_recieved.size[0]/2-10,image_recieved.size[0]/2+10):
    for j in range(image_recieved.size[1]/2-10,image_recieved.size[1]/2+10):
	a,b,c=image_recieved.getpixel((i,j))
        r+=a
        g+=b
        b+=c
        cnt+=1
r=r/cnt
g=g/cnt
b=b/cnt
recog_color=get_colour_name((r,g,b))
print recog_color
tts(recog_color)
