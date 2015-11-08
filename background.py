import urllib
import os
import time

def change_background ():
	img = urllib.urlopen("https://source.unsplash.com/category/nature")

	#download the image, don't forget to change the path 
	f = open('/home/radwakamal/Pictures/bg.jpg','wb')
	f.write(img.read())
	f.close()
 
	os.system ("gsettings set org.gnome.desktop.background picture-uri file:///home/radwakamal/Pictures/bg.jpg")

while True:
	change_background()
	#change background every 12 hrs
	time.sleep(43200)