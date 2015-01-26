from PIL import Image,ImageFilter
import picamera
import RPi.GPIO as GPIO

camera = picamera.PiCamera()
pin=7

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin,False)
def checkit(calc):
	if(calc>100):
		return 1
	else:
		return 0

while(1):
	camera.capture('image.jpg')
	print 'captured1'
	img=Image.open('image.jpg').convert('RGB')
	for i in range(img.size[0]/2-40,img.size[0]/2+40):
		for j in range(img.size[1]/2-40,img.size[1]/2+40):
			r,g,b=img.getpixel((i,j))
			r1,g1,b1=img.getpixel((i+1,j))
			r2,g2,b2=img.getpixel((i+1,j+1))
			r3,g3,b3=img.getpixel((i,j+1))
			r4,g4,b4=img.getpixel((i-1,j+1))
			val=(r+g+b)/3
			val=checkit(val)
			val1=(r1+g1+b1)/3
			val1=checkit(val1)
			val2=(r2+g2+b2)/3
			val2=checkit(val2)
			val3=(r3+g3+b3)/3
			val3=checkit(val3)
			val4=(r4+g4+b4)/3
			val4=checkit(val4)
			x=(val1+val2+val3+val4)-4*val
			if(x==0):
				test_vibr=0
			else:
				test_vibr=1
				break
		if(test_vibr):
			break
			'''if ((r+g+b)/3>100):
				img.putpixel((i,j),(255,255,255))
			else:
				img.putpixel((i,j),(0,0,0))'''
	'''
	print 'captured2'
	img=img.filter(ImageFilter.FIND_EDGES)
	test_vibr=0
	for i in range(img.size[0]/2-75,img.size[0]/2+75):
		for j in range(img.size[1]/2-75,img.size[1]/2+75):
			r,g,b=img.getpixel((i,j))
			if(r>127 and g>127 and b>127):
				test_vibr=1
				break
		if(test_vibr):
			break
	'''
	print test_vibr
	if(test_vibr):
		GPIO.output(pin,True)
	else:
		GPIO.output(pin,False)
