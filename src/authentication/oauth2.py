import requests
import requests.auth
import os
import time
import json

import definitions
from authentication import hidden



def request_new_token():

    hidden_data = hidden.read_hidden_data()
    client_auth = requests.auth.HTTPBasicAuth(hidden_data['client_id'], hidden_data['client_secret'])
    post_data = {"grant_type": "password", "username": hidden_data['username'], "password": hidden_data['password']}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data)
    return response.json()



def save_new_token(access_json):
    if 'expires_in' in access_json:
        expires_in = int(access_json['expires_in'])
        expires_in += int(time.time())
        access_json['expires_in'] = str(expires_in)
        json_string = json.dumps(access_json)
        access_file = open(definitions.ROOT_DIR + "/" + definitions.ACCESS_FILENAME, 'w')
        access_file.write(json_string + "\n")
    else:
        raise Exception("ERROR : corrupt access_json : " + json.dumps(access_json))



def get_access_token():

    access_json = None
    if not os.path.exists(definitions.ROOT_DIR + "/" + definitions.ACCESS_FILENAME):
        access_json = request_new_token()
        save_new_token(access_json)
    else:
        access_file = open(definitions.ROOT_DIR + "/" + definitions.ACCESS_FILENAME)
        line = access_file.readline()
        access_json = json.loads(line)
        if int(access_json['expires_in']) <= int(time.time()):
            access_json = request_new_token()
            save_new_token(acces_json)
    return access_json
