import requests

### Parameters ###
api_login = 'Administrator'
api_password = 'kismstr'
api_iserver = '10.10.5.170:8080'
project_id = '09CB082811E8A750096D0080EF45715A'
base_url = "http://" + api_iserver + "/MicroStrategyLibrary/api/"
datasetId = "5B71C89C11E7B2B4137B0080EFD5FBAC" # Cube ID
tableId = "sensor_data_table"
cube_structure_json = '{"name": "sensor_data","tables": [{"data": "e30=","name": "sensor_data_table","columnHeaders": [{"name": "timestamp","dataType": "STRING"},{"name": "driverId","dataType": "STRING"},{"name": "accel_X","dataType": "DOUBLE"},{"name": "accel_Y","dataType": "DOUBLE"},{"name": "accel_Z","dataType": "DOUBLE"},{"name": "gyro_X","dataType": "DOUBLE"},{"name": "gyro_Y","dataType": "DOUBLE"},{"name": "gyro_Z","dataType": "DOUBLE"},{"name": "humidity","dataType": "DOUBLE"},{"name": "pressure","dataType": "DOUBLE"},{"name": "temperature","dataType": "DOUBLE"}]}],"metrics": [{"name": "accel_X","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.accel_X"}]},{"name": "accel_Y","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.accel_Y"}]},{"name": "accel_Z","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.accel_Z"}]},{"name": "gyro_X","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.gyro_X"}]},{"name": "gyro_Y","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.gyro_Y"}]},{"name": "gyro_Z","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.gyro_Z"}]},{"name": "humidity","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.humidity"}]},{"name": "pressure","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.pressure"}]},{"name": "temperature","dataType": "DOUBLE","expressions": [{"formula": "sensor_data_table.temperature"}]}],"attributes": [{"name": "driverId","attributeForms": [{"category": "ID","expressions": [{"formula": "sensor_data_table.driverId"}],"dataType": "STRING"}]},{"name": "timestamp","attributeForms": [{"category": "ID","expressions": [{"formula": "sensor_data_table.timestamp"}],"dataType": "DATETIME"}]}]}'

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
        
def create_cube(base_url, auth_token, cookies, project_id, cube_structure_json):
    headers_cc = {'X-MSTR-AuthToken': auth_token,
                  'Content-Type': 'application/json',#IMPORTANT!
                  'Accept': 'application/json',
                  'X-MSTR-ProjectID': project_id}
    print("\nCreating new cube...")
    r = requests.post(base_url + "datasets", headers=headers_cc, data=cube_structure_json, cookies=cookies)
    if r.ok:
        print("Error: " + str(r.raise_for_status()) + "   ||   HTTP Status Code: " + str(r.status_code))
        print("\nCube CREATED successfully")
        print("\nCube ID:     " + r.json()['datasetId'])
        print("Cube Name:   " + r.json()['name'])
        print("Table ID:    " + r.json()['tables'][0]['id'])
        print("Table Name:  " + r.json()['tables'][0]['name'])
        print("\nRemember to copy and note down Cube ID (dataset ID) and Table ID. Enter those values in the Python script 'Parameters' section")
    else:
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))  
        
def main():
    token, cookies = login(base_url,api_login,api_password);
    create_cube(base_url, token, cookies, project_id, cube_structure_json)
    
main()
