# What is Python (Programming)? - The Basics

Before getting started, lets get familiarized with the language first.

Python is a general-purpose language. It has wide range of applications from Web development (like: Django and Bottle), scientific and mathematical computing (Orange, SymPy, NumPy) to desktop graphical user Interfaces (Pygame, Panda3D).

The syntax of the language is clean and length of the code is relatively short. It's fun to work in Python because it allows you to think about the problem rather than focusing on the syntax.

### More information on Python Language:

#### History of Python
Python is a fairly old language created by Guido Van Rossum. The design began in the late 1980s and was first released in February 1991.

#### Why Python was created?
In late 1980s, Guido Van Rossum was working on the Amoeba distributed operating system group. He wanted to use an interpreted language like ABC (ABC has simple easy-to-understand syntax) that could access the Amoeba system calls. So, he decided to create a language that was extensible. This led to a design of new language which was later named Python.

#### Why the name Python?
No. It wasn't named after a dangerous snake. Rossum was fan of a comedy series from late seventies. The name "Python" was adopted from the same series "Monty Python's Flying Circus".

### Release Dates of Different Versions

|Version	|Release  |Data   |
| ----------- |:---------:|:-------:|
|**Python 1.0**   | (first standard release) |January 1994|
|**Python 1.6**   | (Last minor version)	 |September 5, 2000|
|**Python 2.0**  | (Introduced list comprehensions) | October 16, 2000|
|**Python 2.7**  | (Last minor version) | July 3, 2010 |
|**Python 3.0**  | (Emphasis on removing duplicative constructs and module) | December 3, 2008 |
|**Python 3.5**  | (Last updated version)	| September 13, 2015 |


### Features of Python Programming
- **A simple language which is easier to learn**
Python has a very simple and elegant syntax. It's much easier to read and write Python programs compared to other languages like: C++, Java, C#. Python makes programming fun and allows you to focus on the solution rather than syntax.
If you are a newbie, it's a great choice to start your journey with Python.

- **Free and open-source**
You can freely use and distribute Python, even for commercial use. Not only can you use and distribute softwares written in it, you can even make changes to the Python's source code.
Python has a large community constantly improving it in each iteration.

- **Portability**
You can move Python programs from one platform to another, and run it without any changes.
It runs seamlessly on almost all platforms including Windows, Mac OS X and Linux.

- **Extensible and Embeddable**
Suppose an application requires high performance. You can easily combine pieces of C/C++ or other languages with Python code.
This will give your application high performance as well as scripting capabilities which other languages may not provide out of the box.

- **A high-level, interpreted language**
Unlike C/C++, you don't have to worry about daunting tasks like memory management, garbage collection and so on.
Likewise, when you run Python code, it automatically converts your code to the language your computer understands. You don't need to worry about any lower-level operations.

- **Large standard libraries to solve common tasks**
Python has a number of standard libraries which makes life of a programmer much easier since you don't have to write all the code yourself. For example: Need to connect MySQL database on a Web server? You can use MySQLdb library using `import MySQLdb`.
Standard libraries in Python are well tested and used by hundreds of people. So you can be sure that it won't break your application.

- **Object-oriented**
Everything in Python is an object. Object oriented programming (OOP) helps you solve a complex problem intuitively.
With OOP, you are able to divide these complex problems into smaller sets by creating objects.

### Applications of Python
- **Web Applications**
You can create scalable Web Apps using frameworks and CMS (Content Management System) that are built on Python. Some of the popular platforms for creating Web Apps are: Django, Flask, Pyramid, Plone, Django CMS.
Sites like Mozilla, Reddit, Instagram and PBS are written in Python.

- **Scientific and Numeric Computing**
There are numerous libraries available in Python for scientific and numeric computing. There are libraries like: SciPy and NumPy that are used in general purpose computing. And, there are specific libraries like: EarthPy for earth science, AstroPy for Astronomy and so on.
Also, the language is heavily used in machine learning, data mining and deep learning.

- **Creating software Prototypes**
Python is slow compared to compiled languages like C++ and Java. It might not be a good choice if resources are limited and efficiency is a must.
However, Python is a great language for creating prototypes. For example: You can use Pygame (library for creating games) to create your game's prototype first. If you like the prototype, you can use language like C++ to create the actual game.

- **Good Language to Teach Programming**
Python is used by many companies to teach programming to kids and newbies.
It is a good language with a lot of features and capabilities. Yet, it's one of the easiest language to learn because of its simple easy-to-use syntax.

 

### 4 Reasons to Choose Python as First Language

- **Simple Elegant Syntax**
Programming in Python is fun. It's easier to understand and write Python code. Why? The syntax feels natural. 
Take this source code for an example:

```python
a = 2
b = 3
sum = a + b
print(sum)
```
Even if you have never programmed before, you can easily guess that this program adds two numbers and prints it.

- **Not overly strict**
You don't need to define the type of a variable in Python. Also, it's not necessary to add semicolon at the end of the statement.Python enforces you to follow good practices (like proper indentation). These small things can make learning much easier for beginners.

- **Expressiveness of the language**
Python allows you to write programs having greater functionality with fewer lines of code. Here's a link to the source code of Tic-tac-toe game with a graphical interface and a smart computer opponent in less than 500 lines of code. This is just an example. You will be amazed how much you can do with Python once you learn the basics.

- **Great Community and Support**
Python has a large supporting community. There are numerous active forums online which can be handy if you are stuck. 
Some of them are:
- [Learn Python Subreddit](https://www.reddit.com/r/learnpython)
- [Google Forum for Python](https://groups.google.com/forum/#!forum/comp.lang.python)
- [Python Questions- Stack Overflow](http://stackoverflow.com/tags/python)


### Run Python on Your Operating System

You will find the easiest way to run Python on your computer (Windows, Mac OS X or Linux) in this section.

#### Install and Run Python in Mac OS X

- Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).

- When the download is complete, open the package and follow the instructions. You will see "The installation was successful" message when Python is successfully installed.

- It's recommended to download a good text editor before you get started. If you are a beginner, I suggest you to download Sublime Text. It's free.

- The installation process is straight forward. Run the Sublime Text Disk Image file you downloaded and follow the instructions.

- Open Sublime Text and go to **File > New File** (Shortcut: **Cmd+N**). Then, save (**Cmd+S** or **File > Save**) the file with **.py** extension like: `hello.py` or `first-program.py`

- Write the code and save it again. For starters, you can copy the code below:
```python
print("Hello, World!")
```
- This simple program outputs "Hello, World!"

- Go to Tool > Build (Shortcut: Cmd + B). You will see the output at the bottom of Sublime Text.Congratulations, you've successfully run your first Python program.

#### Install and Run Python in Linux (Ubuntu)

- Install the following dependencies:

```bash
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```
- Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).

- In the terminal, go to the directory where the file is downloaded and run the command:

```$ tar -xvf Python-3.6.0.tgz```

- This will extract your zipped file. 
**Note: The filename will be different if you've downloaded a different version. Use the appropriate filename.**

- Go to the extracted directory.

```$ cd Python-3.6.0```

- Issue the following commands to compile Python source code on your Operating system.
```
$ ./configure
$ make
$ make install
```
- We recommend you to install Sublime Text if you are a newbie. To install Sublime Text in **Ubuntu (on 14.04)**. 

- Issue following commands.
```
$ sudo add-apt-repository -y ppa:webupd8team/sublime-text-2
$ sudo apt-get update
$ sudo apt-get install sublime-text
```

- Open Sublime text. To create a new file, go to **File > New File (Shortcut: Ctrl+N)**.
Save the file with `.py` file extension like: **`hello.py`** or **`first-program.py`**

- Write the code and save it **(Ctrl+S or File > Save)** . For starters, you can copy the code below:
```python
print("Hello, World!")
```
>This simple program outputs **"Hello, World!"**

- Go to *Tool > Build (Shortcut: Ctrl+B)*. You will see the output at the bottom of Sublime Text.

>Congratulations, you've successfully run your first Python program.

#### Install and Run Python in Windows

- Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).

- When the download is completed, double-click the file and follow the instructions to install it.

- When Python is installed, a program called IDLE is also installed along with it. It provides graphical user interface to work with Python.

- Open IDLE, copy the following code below and press enter.

```python
print("Hello, World!")
```

- To create a file in IDLE, go to **File > New Window (Shortcut: Ctrl+N)**.

- Write Python code (you can copy the code below for now) and save **(Shortcut: Ctrl+S)** with `.py` file extension like: `hello.py` or `your-first-program.py`

```python
print("Hello, World!")
```
- Go to **Run > Run module (Shortcut: F5)** and you can see the output.
>Congratulations, you've successfully run your first Python program.
 

### Your First Python Program

Often, a program called **"Hello, World!"** is used to introduce a new programming language to beginners. A **"Hello, World!"** is a simple program that outputs **"Hello, World!"**.

However, Python is one of the easiest language to learn, and creating "Hello, World!" program is as simple as writing 

```python
print("Hello, World!")
```

So, we are going to write a different program.

**Program to Add Two Numbers**

#### Add two numbers

```python
num1 = 3
num2 = 5
sum = num1 + num2
print(sum)
```

**How this program works?**

- Line 1: Add two numbers

Any line starting with (#) in Python programming is a **comment**.

Comments are used in programming to describe the purpose of the code. This helps you as well as other programmers to understand the intent of the code. Comments are completely ignored by compilers and interpreters.

- Line 2: num1 = 3

Here, num1 is a variable. You can store a value in a variable. Here, 3 is stored in this variable.

- Line 3: num2 = 5

Similarly, 5 is stored in num2 variable.

- Line 4: sum = num1+num2

The variables num1 and num2 are added using + operator. The result of addition is then stored in another variable sum.

- Line 5: print(sum)

The ``print()`` function prints the output to the screen. In our case, it prints 8 on the screen.

**Few Important Things to Remember**

To represent a statement in Python, newline (enter) is used. The use of semicolon at the end of the statement is optional (unlike languages like C/C++, JavaScript, PHP). In fact, it's recommended to omit semicolon at the end of the statement in Python.

Instead of **curly braces { }**, **indentations** are used to represent a block.

```python
   im_a_parent:
    im_a_child:
        im_a_grand_child
    im_another_child:
        im_another_grand_child
```


**Programiz Main reference
Edited and Written in Markdown text by Amir Mohammad Safari**