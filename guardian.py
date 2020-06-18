#!/usr/bin/env python
import os
import sys
import time
import argparse
import subprocess
from datetime import datetime

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-c", "--command",
    required = True,
    help     = "Command to execute.")

    parser.add_argument("-r", "--repeat",
    type    = int,
    default = 1,
    help    = "Times to repeat on fail.")

    parser.add_argument("-w", "--wait",
    type    = int,
    default = 30,
    help    = "Wait between repeations (seconds)")

    options = parser.parse_args()

    cmd     = options.command
    repeat  = options.repeat
    wait    = options.wait
    
    tries = 0
    while(True):
        tries += 1
        process = subprocess.Popen(cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,)
        stdout_value, stderr_value = process.communicate()
        dt = datetime.now()
        if process.returncode == 0:
            print('%s - SUCCESS - STDIN: %s '%(dt,cmd))
            stdout_value = stdout_value.decode("utf-8")
            print('STDOUT:\n %s'%(stdout_value))
            sys.exit()
        else:
            stderr_value = stderr_value.decode("utf-8")
            print('%s - TRY - %s: FAILURE: %s STDERR: %s'%(dt,tries,cmd,stderr_value))
            if tries == repeat:
                print('%s - GIVING UP: Maximum repeations reached for %s'%(dt,cmd))
                sys.exit()
            else:
                time.sleep(wait)          
