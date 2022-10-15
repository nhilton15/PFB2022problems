#!/usr/bin/env python3

import subprocess

subprocess.run(['ls','-l'])

with open('subprocessout.txt','w') as processwrite:
    subprocess.check_call(['ls', '-lF'], stdout=processwrite)

