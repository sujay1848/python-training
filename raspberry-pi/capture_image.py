'''
Created on Oct 9, 2018
@author: sanjankar
'''

import time
import picamera
from sense_hat import SenseHat
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from push_sensor_data import trigger
from push_sensor_data import stop_data_push

sense = SenseHat()
picture_taken = False
stop_run = False

def take_picture(picture_taken):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.rotation = (180)
        image_file_name = 'user_' + str(int(round(time.time() * 1000))) + '.jpg'
        sense.show_letter('A', text_colour = [255, 0, 0])
        print('Image: ' + image_file_name)
        while True: 
            for event in sense.stick.get_events():
                if event.action == 'released' and event.direction == 'up':
                    print("The joystick was {} {}".format(event.action, event.direction))
                    camera.capture(image_file_name)
                    picture_taken = True
                    #copy_image(image_file_name) -  removed because showing error
                    sense.show_letter('<', text_colour = [0, 255, 0])
                    trigger(image_file_name,sense)
                    return

def copy_image(image_file_name):
    s = SSHClient()
    destination_path = '/usr/local/tomcat/webapps/MicroStrategy/images/STELS/IOT/' + image_file_name
    s.set_missing_host_key_policy(AutoAddPolicy())
    s.connect("10.10.5.170", 22, username="root", password="info@999", timeout=10)
    sftp = s.open_sftp()
    print('Begin copying: ' + image_file_name + ' to: ' + destination_path)
    sftp.put(image_file_name, destination_path)
    print('Finished copying.')
    
def stop_run():
    sense.clear()
    sense.show_letter('O', text_colour = [255, 0, 0])
    stop_data_push()
    return

def start_run():
    while picture_taken != True:
        for event in sense.stick.get_events():
            sense.show_letter('P', text_colour = [0, 100, 255])
            if event.action == 'released' and event.direction == 'down':
                print("The joystick was {} {}".format(event.action, event.direction))
                take_picture(picture_taken)
                return
                
while True:
    print("\n\n Beginning")
    sense.show_letter('v', text_colour = [0, 255, 255])
    time.sleep(0.1)
##    sense.stick.direction_right = stop_run
##    sense.stick.direction_middle = start_run
    event= sense.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction))
    if event.direction == 'middle':
        start_run()







