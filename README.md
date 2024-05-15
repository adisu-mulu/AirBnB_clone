This project is the first of the projects that will build up to a complete full stack web.The web application is a clone of the AirBnb website.
The command interpreter is written in the module called pythonShell. It is used to interact with the application during development, debugging and testing features.

How to start it:
The command interpreter (pythonShell.py) can be started by running it with the python3 pythonShell.py or since it has been made executable, you can just type ./pythonShell.py

How to use it:
The command interpreter (pythonShell.py) can be used in two modes.
    1. Interactive mode
       In this mode you will first run the program using ./pythonShell.py or python3 pythonShell.py. This will open up a terminal where you can type in your command	   s and it will be executed accordingly. The whole program runs in a loop that willl exitwith the command quit.
    2. Non-interactive mode
       In this mode, you can directly pipe the output of other programs as input to the pythonShell. For example, echo "help" | ./pythonShell.py. This will first ou	   tput help to the stdout, the content of the stdout, i.e., help is then fed as input to the stdin of the pythonShell.py module. This approach will however exe       cute once. It will not continue in loop like the interactive mode.
