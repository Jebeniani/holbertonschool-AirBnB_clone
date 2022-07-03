![alt](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220703%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220703T210747Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f12fce841ddc2fc30f3ee7cbb96bd80efd96990a8a16a5550c57ac90c64085e4)
##Welcome to the AirBnB clone project!

**What’s a command interpreter?
	
Do you remember the Shell? It’s exactly the same but limited to a specific use-case.
In our case, we want to be able to manage the objects of our project:

-Create a new object (ex: a new User or a new Place)
-Retrieve an object from a file, a database etc…
-Do operations on objects (count, compute stats, etc…)
-Update attributes of an object
-Destroy an object

##General
-How to create a Python package
-How to create a command interpreter in Python using the cmd module
-What is Unit testing and how to implement it in a large project
-How to serialize and deserialize a Class
-How to write and read a JSON file
-How to manage datetime
-What is an UUID
-What is *args and how to use it
-What is **kwargs and how to use it
-How to handle named arguments in a function

###Execution
Your shell should work like this in interactive mode:
```python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
#Usage
##Interactive Mode
To begin interactive mode, run ```./console.py``` from the command line

COMMAND | DECRIPTION
----|----
```(hbnb) quit``` | Quits console
```(hbnb) EOF``` | Quits console
```(hbnb) help <command>``` | Display help for <command>
```(hbnb) create <class>``` |Create object and print id
```(hbnb) show <class> <id>``` | Show information
```(hbnb) destroy <class> <id>``` | Destroy object
```(hbnb) all <class>``` | Show all instances of a class
```(hbnb) update <class> <id> <attribute name> <attribute value>``` | Creates or updates the attribute of a class


The commands create, show, detroy, all, and update can be ran with the following syntax:
```<class>.<command>(<optional id>, <optional arguments>)```
