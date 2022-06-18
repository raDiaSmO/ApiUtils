#!/usr/bin/env python3

import os
import sys
import subprocess
import re

def wpscan():

    file = sys.argv[1]
    api = sys.argv[2]

    if os.path.exists(file):
        print ('The following list will be used', os.path.abspath(file))

    else:
        print ('The provided path does not exist.')
        sys.exit()

    with open (file) as assets:
        for asset in assets:

            try:
                fstring = f"wpscan --url {asset} --random-user-agent --disable-tls-checks --detection-mode aggressive --api-token {api} -e vp,vt,dbe --output ~/wpscanresult --format cli"
                command = re.sub('\?|\!|\'|\n|\'|\;', '', fstring)
                subprocess.check_output(['bash','-c', command])

            except:
                print ('Could not execute the request')
                sys.exit()
wpscan()
