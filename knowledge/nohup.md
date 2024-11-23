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

