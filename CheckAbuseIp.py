#!/usr/bin/env python3

import requests
import json
import sys

def check_ip():

    endpoint = 'https://api.abuseipdb.com/api/v2/check'
    file = sys.argv[1]

    with open (file) as ips:
        for ip in ips:

            data = {
                        'ipAddress': ip
            }

            http_headers = {
                    'Accept': 'application/json',
                    'Key': sys.argv[2]
            }

            try:
                r = requests.request(method='GET', url=endpoint, headers=http_headers, params=data)
                decoded_r = json.loads(r.text)
                print(json.dumps(decoded_r, sort_keys=True, indent=3))

            except:
                print('Could not execute the following request.')
                sys.exit()

check_ip()
