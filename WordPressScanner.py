#!/usr/bin/env python3

import os
import sys
import subprocess
import re

def wpscan():

    file = sys.argv[1]
    api = sys.argv[2]
    out = sys.argv[3]
    paths = [sys.argv[1],sys.argv[3]]

    for path in paths:

        if not os.path.exists(path):
            print('The provided path does not exist.',path)
            sys.exit()

        with open (file) as assets:
            for asset in assets:

                try:
                    f_string = f"wpscan --url {asset} --random-user-agent --disable-tls-checks --detection-mode aggressive --api-token {api} -e vp,vt,dbe --output {out} --format cli"
                    command = re.sub('\?|\!|\'|\n|\'|\;', '', f_string)
                    subprocess.check_output(['bash','-c', command])

                except:
                    print('Could not execute the request')
                    sys.exit()
wpscan()
