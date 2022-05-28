#!/usr/bin/env python3

import requests
import json
import sys

def checkip():
    endpoint = 'https://api.abuseipdb.com/api/v2/check'
    
    ip = {
            #This argument is the IP address you want to scan.
            'ipAddress': sys.argv[1]
    }

    http_headers = {
            #This argument is your API key from AbuseIPDB.
            'Accept': 'application/json',
            'Key': sys.argv[2]
    }

    r = requests.request(method='GET', url=endpoint, headers=http_headers, params=ip)
    decoded_r = json.loads (r.text)
    print ( json.dumps (decoded_r, sort_keys=True, indent=4) )

checkip()
