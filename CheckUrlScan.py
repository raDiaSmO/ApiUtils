#!/usr/bin/env python3

import requests
import json
import sys

def check_url():
    
    endpoint = 'https://urlscan.io/api/v1/scan' 
    file = sys.argv[1]
    api = sys.argv[2]

    with open (file) as urls:
        for url in urls:

            d = {
                    'url': url,
                    'visibility': "public"
            }

            http_headers = {
                    'API-Key': api,
                    'Content-Type': 'application/json'
            }

            try:
                r = requests.post(endpoint, headers=http_headers, data=json.dumps(d))
                r_dict = (r.json())
                print('The following link will be accessible in a few minutes and will contain the scan result.\n\n', r_dict['result'], end='\n\n')

            except:
                print('Could not execute the following request.')
                sys.exit()

check_url()
