# Project 0x04. Loops, conditions and parsing0x04. Loops, conditions and parsing

## Resources

* [Loops sample](https://www.youtube.com/watch?v=BC2neyc5GcI&feature=youtu.be)
* [Variable assignment and arithmetic](http://tldp.org/LDP/abs/html/ops.html)
* [Comparison operators](http://tldp.org/LDP/abs/html/comparison-ops.html)
* [File test operators](http://tldp.org/LDP/abs/html/fto.html)
* [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

## man or help:

* *env* -  env - run a program in a modified environment. 
* *cut* - remove sections from each line of files
* *for* - The for loop is the first of the three shell looping constructs. This loop allows for specification of a list of values. A list of commands is executed for each value in the list.
* *while* - In most computer programming languages, a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement. The while construct allows for repetitive execution of a list of commands, as long as the command controlling the while loop executes successfully (exit status of zero).
* *until* - The until loop is very similar to the while loop, except that the loop executes until the TEST-COMMAND executes successfully. As long as this command fails, the loop continues.
* *if* - The if loop performs an action if a particular condition is satisfied. 

## Learning Objectives


* How to create SSH keys
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## General Requirements

* All files will be interpreted on Ubuntu 14.04 LTS
* Al files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* The Bash script files must be executable
* The use of awk is forbidden 
* Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all  Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all Bash scripts should be a comment explaining what is the script

## Shellcheck

A tool that helps write proper Bash scripts. It will make recommendations on syntax and semantics and provide advice.
[Here](https://github.com/koalaman/shellcheck#installing) is how to install it.

## TASKS

### Task 0.
Create a RSA key pair.

### Task 1.
Write a Bash script that displays Holberton School 10 times using the for loop.

### Task 2.
Write a Bash script that displays Holberton School 10 times using the while loop.

### Task 3.
Write a Bash script that displays Holberton School 10 times using the until loop.

### Task 4.
Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line using the while loop and the if statement.

### Task 5.
Write a Bash script that loops from 1 to 10 and:
displays bad luck for the 4th loop iteration
    displays good luck for the 8th loop iteration
    displays Holberton School for the other iterations using the while loop and the if, elif and else statements.

### Task 6.
Write a Bash script that displays numbers from 1 to 20 and:
displays 4 and then bad luck from China for the 4th loop iteration
    displays 9 and then bad luck from Japan for the 9th loop iteration
    displays 17 and then bad luck from Italy for the 17th loop iteratio using the while loop. Use the case statement

### Task 7.
Write a Bash script that displays numbers from 1 to 20 and:
In this example, we only display the first 70 lines using the head command.

### Task 8.
Write a Bash script that displays:
The content of the current directory
    In a list format
    Where only the part of the name after the first dash is display using the for loop 
    Do not display hidden files.

### Task 9.
Write a Bash script that gives you information about the holbertonschool file. Use if and, else 
    Your Bash script should check if the file exists and print:
        if the file exists: holbertonschool file exists
        if the file does not exist: holbertonschool file does not exist
    If the file exists, print:
        if the file is empty: holbertonschool file is empty
        if the file is not empty: holbertonschool file is not empty
        if the file is a regular file: holbertonschool is a regular file
        if the file is not a regular file: (nothing).

### Task 10.
Write a Bash script that displays numbers from 1 to 100. Display FizzBuzz when the number is a multiple of 3 and 5
    Displays Fizz when the number is multiple of 3
    Displays Buzz when the number is a multiple of 5
    Otherwise, displays the number
    In a list format.











