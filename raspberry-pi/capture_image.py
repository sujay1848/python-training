'''
Created on Oct 9, 2018

@author: sanjankar
'''

import time
import picamera
from sense_hat import SenseHat
from paramiko import SSHClient
from paramiko import AutoAddPolicy

def take_picture():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)
        image_file_name = 'user_' + str(int(round(time.time() * 1000))) + '.jpg'
        camera.capture(image_file_name)
        copy_image(image_file_name)
        
def copy_image(image_file_name):
    s = SSHClient()
    destination_path = '/usr/local/tomcat/webapps/MicroStrategy/images' + image_file_name
    s.set_missing_host_key_policy(AutoAddPolicy())
    s.connect("10.10.5.170", 22, username="root", password="info@999", timeout=4)
    sftp = s.open_sftp()
    print('Begin copying: ' + image_file_name + ' to: ' + destination_path)
    sftp.put(image_file_name, destination_path)
    print('Finished copying.')
    
    
sense = SenseHat()
while True:
    for event in sense.stick.get_events():
        print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'released' and event.direction == 'middle':
            take_picture()