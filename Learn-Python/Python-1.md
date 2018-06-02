#  How to Get Started With Python?

Python is a cross-platform programming language, meaning, it runs on multiple platforms like Windows, Mac OS X, Linux, Unix and has even been ported to the Java and .NET virtual machines. It is free and open source.

Even though most of today’s Linux and Mac have Python preinstalled in it, the version might be out-of-date. So, it is always a good idea to install the most current version. You can download the latest version of Python and install it.

### Starting The Interpreter

After installation, the python interpreter lives in the installed directory.

By default it is `/usr/local/bin/pythonX.X ` in Linux/Unix and  `C:\PythonXX` in Windows, where the `'X'` denotes the version number. To invoke it from the shell or the command prompt we need to add this location in the search path.

Search path is a list of directories (locations) where the operating system searches for executables. For example, in Windows command prompt, we can type `set path=%path%; c:\python33`(python33 means version 3.3, it might be different in your case) to add the location to path for that particular session.

In Mac OS we need not worry about this as the installer takes care about the search path.

Now there are various ways to start Python.

#### 1. Immediate mode

Typing `python` in the command line will invoke the interpreter in immediate mode. We can directly type in Python expressions and press enter to get the output.
```python
>>> 
```
Is the python prompt. It tells us that the interpreter is ready for our input. Try typing in `1 + 1` and press enter. We get `2` as the output. This prompt can be used as a calculator. To exit this mode type `exit()` or `quit()` and press enter.

#### 2. Script mode

This mode is used to execute Python program written in a file. Such a file is called a **script**. Scripts can be saved to disk for future use. Python scripts have the extension `.py`, meaning that the filename ends with `.py`.

>`For example: helloWorld.py`

To execute this file in script mode we simply write `python helloWorld.py` at the command prompt.

### Integrated Development Environment (IDE)

We can use any text editing software to write a Python script file.

We just need to save it with the `.py` extension. But using an IDE can make our life a lot easier. IDE is a piece of software that provides useful features like code hinting, syntax highlighting and checking, file explorers etc. to the programmer for application development.

Using an IDE can get rid of redundant tasks and significantly decrease the time required for application development.

IDEL is a graphical user interface (GUI) that can be installed along with the Python programming language and is available from the official website.

We can also use other commercial or free IDE according to our preference. We have used the ***PyScripter*** IDE for our testing and we recommend the same. It is free and open source.

### Hello World Example

Now that we have Python up and running, we can continue on to write our first Python program.

Type the following code in any text editor or an IDE and save it as `helloWorld.py`

```python
print("Hello world!")
```

Now at the command window, go to the loaction of this file. You can use the `cd` command to change directory.

To run the script, type `python helloWorld.py` in the command window. We should be able to see the output as follows:

>**Hello world!**

If you are using PyScripter, there is a green arrow button on top. Press that button or press `Ctrl+F9` on your keyboard to run the program.

In this program we have used the built-in function `print()`, to print out a string to the screen. String is the value inside the quotation marks, i.e. Hello world! . Now try printing out your name by modifying this program.

Congratulations! You just wrote your first program in Python.

As we can see, it was pretty easy. This is the beauty of Python programming language.