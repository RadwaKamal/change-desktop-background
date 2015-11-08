'''
Simple python script to change desktop background on startup and every 12 hours.
'''
import urllib
import os
import time

def get_image():
    '''
    Get an image from Unsplash Source <https://source.unsplash.com/>
    and save it locally on the current user's home
    '''
    img_api_url = urllib.urlopen("https://source.unsplash.com/category/nature")
    #download the image
    img_path = os.path.expanduser('~') + '/Pictures/bg.jpg'
    img_file = open(os.path.expanduser('~') + '/Pictures/bg.jpg', 'wb')
    img_file.write(img_api_url.read())
    img_file.close()
    return img_path

def change_background():
    '''
    - Set the image using command-line
    - Change background every 12 hr
    '''
    img = get_image()
    cmd = 'gsettings set org.gnome.desktop.background picture-uri'
    os.system("{0} file://{1}".format(cmd, img))

    while True:
        change_background()
        #change background every 12 hrs
        time.sleep(1)

if __name__ == "__main__":
    try:
        change_background()
    except KeyboardInterrupt:
        #print a message when using CTRL+C to exit
        print 'exit'
