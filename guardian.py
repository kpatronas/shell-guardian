#!/usr/bin/env python3
import os
import sys
import time
import argparse
import subprocess
from datetime import datetime

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--command",   required = True,  help = "Command to execute.")
    parser.add_argument("-e", "--exit_code", required = False, type = int, default = 0,  help = "desired exit code.")
    parser.add_argument("-r", "--repeat",    required = False, type = int, default = 1,  help = "Times to repeat on fail.")
    parser.add_argument("-w", "--wait",      required = False, type = int, default = 30, help = "Wait between repeations (seconds)")
    parser.add_argument("-s", "--success",   required = False, help = "Command to execute on success.")
    parser.add_argument("-f", "--fail",      required = False, help = "Command to execute on fail.")

    options = parser.parse_args()

    cmd       = options.command
    exit_code = options.exit_code
    repeat    = options.repeat
    wait      = options.wait
    success   = options.success
    fail      = options.fail

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
        if process.returncode == exit_code:
            print('%s - SUCCESS - STDIN: %s '%(dt,cmd))
            stdout_value = stdout_value.decode("utf-8")
            print('STDOUT:\n %s'%(stdout_value))
            if success:
                success_process = subprocess.Popen(success, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
                success_stdout_value, success_stderr_value = success_process.communicate()
                success_stdout_value = success_stdout_value.decode("utf-8")
                print("ON SUCCESS STDIN: %s"%(success))
                if success_stdout_value:
                    print("ON SUCCESS STDOUT: %s"%(success_stdout_value))
                if success_stderr_value:
                    print("ON SUCCESS STDERR: %s"%(success_stderr_value))
            sys.exit(exit_code)
        else:
            stderr_value = stderr_value.decode("utf-8")
            print('%s - TRY - %s: FAILURE: %s STDERR: %s'%(dt,tries,cmd,stderr_value))
            if fail:
                fail_process = subprocess.Popen(fail, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
                fail_stdout_value, fail_stderr_value = fail_process.communicate()
                print("ON FAIL STDIN: %s"%(fail))
                fail_stdout_value = fail_stdout_value.decode("utf-8")
                if fail_stdout_value:
                    print("ON FAIL STDOUT: %s"%(fail_stdout_value))
                if fail_stderr_value:
                    print("ON FAIL STDERR: %s"%(fail_stderr_value))
            if tries == repeat:
                print('%s - GIVING UP: Maximum repeations reached for %s'%(dt,cmd))
                sys.exit(process.returncode)
            else:
                time.sleep(wait)
