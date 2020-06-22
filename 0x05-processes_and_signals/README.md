# Project 0x05. Processes and signals

## Resources

* [Linux PID](http://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)

### man or help

* ps - report a snapshot of the current processes
* pgrep -  pgrep, pkill - look up or signal processes based on name and other attributes
* pkill -  pgrep, pkill - look up or signal processes based on name and other attributes
* kill -  The default signal for kill is TERM.  Use -l or -L to list available signals.  Particu‐
       larly useful signals include HUP, INT, KILL, STOP, CONT, and 0.  Alternate signals  may
       be  specified in three ways: -9, -SIGKILL or -KILL.  Negative PID values may be used to
       choose whole process groups; see the PGID column in ps command output.  A PID of -1  is
       special; it indicates all processes except the kill process itself and init.
* exit - cause normal process terminationv
* trap - rap defines and activates handlers to be run when the shell receives signals or other special conditions.

## General Reaquirements
  
* All  files will be interpreted on Ubuntu 14.04 LTS
* All  files should end with a new line
* All Bash script files must be executable
* Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all Bash scripts should be a comment explaining what is the script doing

## TASKS

### Task 0.
Write a Bash script that displays its own PID.

### Task 1.
Write a Bash script that displays a list of currently running processes.

### Task 2.
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

### Task 3. 
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash

### Task 4.
Write a Bash script that displays To infinity and beyond indefinitely. 

### Task 5.
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that kills 4-to_infinity_and_beyond process.

### Task 6.
Write a Bash script that kills 4-to_infinity_and_beyond process.

### Task 7. 
Write a Bash script that displays:
    To infinity and beyond indefinitely
    With a sleep 2 in between each iteration
    I am invincible!!! when receiving a SIGTERM signal

### Task 8
Write a Bash script that kills the process 7-highlander


