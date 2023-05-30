#!/usr/bin/env python3

import sys
import hashlib
import requests
import json
import time
import argparse


# Parse command line arguments
parser = argparse.ArgumentParser(description='Retrieve the NOC list from BADSEC server.')
parser.add_argument('--base_url', default='http://localhost:8888', help='The base URL of the BADSEC server')
parser.add_argument('--max_retries', type=int, default=2, help='The maximum number of retries for each request')

args = parser.parse_args()

BASE_URL = args.base_url
MAX_RETRIES = args.max_retries


HEADERS = {
    'User-Agent': 'BADSEC-Agent',
}
####Function to request token from server####
def get_auth_token():

    for i in range(MAX_RETRIES + 1):
        try:
            response = requests.get(f'{BASE_URL}/auth', headers=HEADERS)
            #if response is not 200, raise exception
            response.raise_for_status()
            return response.headers['Badsec-Authentication-Token']
                  
        except requests.exceptions.RequestException:
            #wait 1 second before retrying
            time.sleep(1)
    return None

####Function to request user list from server####
def get_users(token):
    
    ### Calculate checksum and add to header to request user list
    checksum = hashlib.sha256((token + '/users').encode()).hexdigest()
   
    HEADERS['X-Request-Checksum'] = checksum

    for r in range(MAX_RETRIES + 1):
        # loopcontrol = r     
        # print("retry number {} ".format(loopcontrol) + 'of ' + str(MAX_RETRIES))
        try:
            response = requests.get(f'{BASE_URL}/users', headers=HEADERS)
            response.raise_for_status()
            
            return response.text.split('\n')
        except requests.exceptions.RequestException:
            #wait 1 second before retrying
            time.sleep(1)
    return None

def main():
    ###1. call /auth endpoint to get an authentication token
    token = get_auth_token()
    if not token:
        print("Failed to authenticate.", file=sys.stderr)
        exit(1)
    ###2. Request user list from server
    users = get_users(token)
    if not users:
        print("Failed to retrieve user list.", file=sys.stderr)
        exit(1)

    print(json.dumps(users))

if __name__ == '__main__':
    main()