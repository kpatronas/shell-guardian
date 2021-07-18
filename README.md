# shell-guardian

## What is shell-guardian?

Shell guardian is a tool that enhances the execution of shell commands by adding the following capabilities

* Repeat a command untill success or until a defined number of failed command executions
* Execute a follow up command in case of a successfull or failed command execution
* Set a wait timer between failed executions

## Examples:
_Execute a command and do nothing_
```
$ ./guardian.py -c "ls ./test"
2021-07-18 21:20:17.808577 - SUCCESS - STDIN: ls ./test
STDOUT:
a.txt
b.txt
```
_Execute a command that will fail, repeat command two times and wait 3 seconds before every try, the desired exit code of command lsa is 0, anything else will considered as a fail_

I know that lsa is a command that does not even exist, but the logic is the same the command could be anything fail prone
like scp, ssh or whatever
* -r: number of repeats, enter -1 to repeat untill success
* -w: the number of seconds to wait between failed command executions
* -e: the desired exit code of the command,can be ommited 0 is the default one
```
$ ./guardian.py -c "lsa ./test" -r 2 -w 3 -e 0
2021-07-18 21:22:23.041339 - TRY - 1: FAILURE: lsa ./test STDERR: /bin/sh: 1: lsa: not found

2021-07-18 21:22:26.223534 - TRY - 2: FAILURE: lsa ./test STDERR: /bin/sh: 1: lsa: not found

2021-07-18 21:22:26.223534 - GIVING UP: Maximum repeations reached for lsa ./test
```
_Execute a command that might fail or might success, execute an follow on command on each case_
* -s: the command executed on success
* -f: the command executed on each failed atempt

Both arguments can be optional
```
./guardian.py -c "ls ./test" -f "echo 'fail'" -s "echo 'success'"
2021-07-18 21:45:32.856868 - SUCCESS - STDIN: ls ./test
STDOUT:
a.txt
b.txt

ON SUCCESS STDIN: echo 'success'
ON SUCCESS STDOUT: success

./guardian.py -c "lsa ./test" -f "echo 'fail'" -s "echo 'success'"
2021-07-18 21:45:38.132180 - TRY - 1: FAILURE: lsa ./test STDERR: /bin/sh: 1: lsa: not found

ON FAIL STDIN: echo 'fail'
ON FAIL STDOUT: fail

2021-07-18 21:45:38.132180 - GIVING UP: Maximum repeations reached for lsa ./test
```
