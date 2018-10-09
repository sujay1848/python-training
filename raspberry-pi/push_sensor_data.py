'''
Created on Sep 30, 2018

@author: sanjankar
'''

import requests
import base64
import datetime
import time
from sense_hat import SenseHat

### Parameters ###
api_login = 'Administrator'
api_password = 'kismstr'
api_iserver = '10.10.5.170:8080'
project_id = '09CB082811E8A750096D0080EF45715A'
base_url = "http://" + api_iserver + "/MicroStrategyLibrary/api/"
datasetId = "D2529F2411E8C4A9343C0080EFE5BC8B" # Cube ID
tableId = "sensor_data_table"
driverId = "Ketan"
sense = SenseHat()

def login(base_url,api_login,api_password):
    print("Getting token...")
    data_get = {'username': api_login,
                'password': api_password,
                'loginMode': 1}
    r = requests.post(base_url + 'auth/login', data=data_get)
    if r.ok:
        auth_token = r.headers['X-MSTR-AuthToken']
        cookies = dict(r.cookies)
        print("Token: " + auth_token)
        return auth_token, cookies
    else:
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))

def get_sensor_data():
    acceleration = sense.get_accelerometer_raw()
    gyro = sense.get_gyroscope_raw()
    print('[{ "timestamp":"' + str(datetime.datetime.now()) +'","driverId":"' + driverId +'","accel_X":' + str(acceleration.get("x")) +',"accel_Y":' + str(acceleration.get("y")) +',"accel_Z":' + str(acceleration.get("z")) + ',"gyro_X":' + str(gyro.get("x")) +',"gyro_Y":' + str(gyro.get("y")) +',"gyro_Z":' + str(gyro.get("z")) +',"humidity":' + str(sense.get_humidity()) +',"pressure":' + str(sense.get_pressure()) +',"temperature":' + str(sense.get_temperature()) +' }]')
    return '[{ "timestamp":"' + str(datetime.datetime.now()) +'","driverId":"' + driverId +'","accel_X":' + str(acceleration.get("x")) +',"accel_Y":' + str(acceleration.get("y")) +',"accel_Z":' + str(acceleration.get("z")) + ',"gyro_X":' + str(gyro.get("x")) +',"gyro_Y":' + str(gyro.get("y")) +',"gyro_Z":' + str(gyro.get("z")) +',"humidity":' + str(sense.get_humidity()) +',"pressure":' + str(sense.get_pressure()) +',"temperature":' + str(sense.get_temperature()) +' }]'

def push_data(update_policy, auth_token, cookies, project_id, dataset_id, table_id):
    raw_data = get_sensor_data()
    pushed_data = base64.b64encode(bytes(raw_data, 'utf-8')).decode('ascii')
    push_url = base_url + "datasets/" + dataset_id + "/tables/" + table_id
    headers_push = {'X-MSTR-AuthToken': auth_token,
                    'Content-Type': 'application/json',#IMPORTANT!
                    'X-MSTR-ProjectID': project_id,
                    'updatePolicy': update_policy
                    }
    insert_data = '{ "name": "sensor_data_table","columnHeaders": [{"name": "timestamp","dataType": "STRING"},{"name": "driverId","dataType": "STRING"},{"name": "accel_X","dataType": "DOUBLE"},{"name": "accel_Y","dataType": "DOUBLE"},{"name": "accel_Z","dataType": "DOUBLE"},{"name": "gyro_X","dataType": "DOUBLE"},{"name": "gyro_Y","dataType": "DOUBLE"},{"name": "gyro_Z","dataType": "DOUBLE"},{"name": "humidity","dataType": "DOUBLE"},{"name": "pressure","dataType": "DOUBLE"},{"name": "temperature","dataType": "DOUBLE"}], "data":"' + pushed_data + '"}'
                   
    print("\nPushing data...")
    print(insert_data)
    r = requests.patch(push_url, headers=headers_push, data=insert_data, cookies = cookies)
    if r.ok:
        print("Pushed successfully...")
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))
    else:
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))
        
def main():
    i = 0;
    while True:
        if i > 12 or i == 0:
            token, cookies = login(base_url,api_login,api_password)
            i = 0
        time.sleep(5)
        push_data("Upsert", token, cookies, project_id, datasetId, tableId)
        i = i + 1

main()
