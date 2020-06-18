# shell-guardian
A Python wrapper script that will help you execute scripts / commands effieciently

## What this script does
This script will execute a given command \ script. on execution failure with an exit code != 0 the wrapper will execute again the command \ script after a wait period, if the execution failure continues for a defined repeation the wrapper script will give up trying with a message.

## Usage Examples:
-c: "The command or script to be executed"
```
c:\Users\kpatr\OneDrive\Desktop\scripts\guardian>python guardian.py -c "dir"
2020-06-18 13:55:25.460505 - SUCCESS - STDIN: dir
STDOUT:
  Volume in drive C has no label.
 Volume Serial Number is 36FC-5968

 Directory of c:\Users\kpatr\OneDrive\Desktop\scripts\guardian

18/06/2020  13:55    <DIR>          .
18/06/2020  13:55    <DIR>          ..
18/06/2020  13:55             1,600 guardian.py
               1 File(s)          1,600 bytes
               2 Dir(s)  357,928,259,584 bytes free
```
-w: wait time between execution failures in seconds. default: 30s

-r: maximum times to repeat execution in case of failure. default: 1 repeation
```
c:\Users\kpatr\OneDrive\Desktop\scripts\guardian>python guardian.py -c "dir -a" -w 3 -r 3
2020-06-18 13:56:36.600020 - TRY - 1: FAILURE: dir -a STDERR: File Not Found

2020-06-18 13:56:39.629230 - TRY - 2: FAILURE: dir -a STDERR: File Not Found

2020-06-18 13:56:42.652491 - TRY - 3: FAILURE: dir -a STDERR: File Not Found

2020-06-18 13:56:42.652491 - GIVING UP: Maximum repeations reached for dir -a
```
## How to repeat until successful execution
Giving a negative value for the -r parameters will do the trick because there are no bugs, only features ;)
```
c:\Users\kpatr\OneDrive\Desktop\scripts\guardian>python guardian.py -c "dir -a" -w 3 -r -1
2020-06-18 14:07:27.260575 - TRY - 1: FAILURE: dir -a STDERR: File Not Found

2020-06-18 14:07:30.282983 - TRY - 2: FAILURE: dir -a STDERR: File Not Found

2020-06-18 14:07:33.303639 - TRY - 3: FAILURE: dir -a STDERR: File Not Found
```
