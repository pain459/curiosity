## What is nohup?

nohup stands for **no hang up**. It is a Linux command used to run processes in the background, immune to the SIGHUP (signal hang up) signal. Normally, when you log out or disconnect from a terminal session, processes tied to that terminal receive the SIGHUP signal and terminate. The nohup command prevents this by allowing the process to continue running even if the terminal is closed.

## Uses of nohup:

1. Run Long-Running Processes: To keep processes running `uninterrupted`, even after logging out from the terminal.
2. Background Execution: It enables running processes in the background, freeing up the terminal for other tasks.
3. Logging Outputs: It redirects the standard output and standard error of the command to a file `(nohup.out)` by default, ensuring you don’t lose logs when the terminal is closed.
4. Detached Tasks: Useful in running tasks that take a long time, such as data processing, backup scripts, or server tasks.
5. Remote Connections: Ideal for maintaining processes in remote SSH sessions that might disconnect.

### How to use nohup?

#### Basic Syntax:
```bash
nohup <command> [arguments] &
```

#### Examples:
1. Running a command in the background
```bash
nohup python3 long_script.py &
```
  - runs the script `long_script.py` in the background.
  - Output is redirected to a file named `nohup.out`

2. Specifying output file
```bash
nohup python3 long_script.py > output.log 2>&1 &
```
  - Redirects both standard output `(stdout)` and standard error `(stderr)` to `output.log`

3. Running a shell script
```bash
nohup ./my_script.sh &
```

4. Checking the Process ID (PID):
  - When the command is run with nohup, it prints the PID of the process.
    ```bash
    [1] 12345
    ``` 
  - Use the `ps` or `top` command to monitor or manage the process
    ```bash
    ps -p 12345
    ```

