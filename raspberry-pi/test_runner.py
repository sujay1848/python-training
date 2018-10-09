'''
Created on Oct 9, 2018

@author: sanjankar
'''
import time
from paramiko import SSHClient
from paramiko import AutoAddPolicy


def main():
    file_name = '/home/dh_sujay/user_' + str(int(round(time.time() * 1000))) + '.txt'
    s = SSHClient()
    s.set_missing_host_key_policy(AutoAddPolicy())
    s.connect("10.242.1.141", 22, username="dh_sujay", password='DF$infocepts16', timeout=4)
    sftp = s.open_sftp()
    print('Begin copying: ' + file_name)
    sftp.put('test.txt', file_name)
    print('Finished copying.')


main()
