# Complete Python Bootcamp
Coursework and notes from [Udemy](https://www.udemy.com/complete-python-bootcamp/)

### Table of Contents

* [Section 1: Course Overview](#1)
* [Section 2: Python setup](#2)


<a name="1"></a>
## Section 1: Course Overview

#### Lessons 1-4

* No notes taken

<a name="2"></a>
## Section 2: Python Setup

#### Lessons 5 & 6

* Installing Python

> I do not install via [Anaconda](https://www.anaconda.com/distribution/), I use homebrew to install Python 3, and then execute [setup-mac.sh](https://gist.github.com/sund0g/3f6f62c4d7f1145ea1070fd9f255a1bc) to install the required modules. This means that the Jupyter notebooks will be started via the command line,

	nohup jupyter notebook &
	
This will start the server, (listening on locahost:8888) and launch a browser instance at the tree root.
	
> for notebook details, reference the [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running)

> I'm using `nohup` and `&` as part of the startup so I  can keep working in the same terminal window. To make shutting down Jupyter easier when done, make a note of the PID. If you don't, you can always use a combination of the `jobs` command to see if the server is running and then `ps` to get the PID, which can then be used to `kill <PID>` the server.

#### Lesson 7

* Setting up the development environment.

> I do not use PyCharm or Sublime, I use VSCode with the python extension installed. Please refer to [setup-mac.sh](https://gist.github.com/sund0g/3f6f62c4d7f1145ea1070fd9f255a1bc) for details.

* The very first Python file is **helloworld.py**. I do this with every language I learn more out of nostalgia, but also as a base on which my knowledgebase is built.

> Create the file in VSCode. If the Python extension is installed correctly, syntax highlighting and the Python icon should appear when the file is saved.

* To run a Python file execute,

		-> python <filename>
		
* To execute single lines of Python code, execute,

		-> python
		
This creates a connection to the Python interpreter, from which lines of code can be executed.

* To exit the interpreter execute,

		>>> quit()

> This isn't extremely useful; just saying it can be done.

* Starting **Jupyter notebook**. As noted in *Lessons 5 & 6* above, I start the notebook server from the command line, `nohup jupyter notebook &`

* **Notebook Overview**

	* **Notebook files** are created with a **.ipynb** extension, (IPythonNotebookFle)
	* To create a new notebook, click on **New** | **Python 3**
	* Rename to **MyFirstNotebook**
	* Notebooks use a *cell* input format, i.e. each line is a cell.
	* Type of `print('Hello world')` in the cell, and click the **Run** button to execute the line.

		> **shift** + **return** also causes the cell to be executed.
		
	* To change what can be typed in a cell, select the dropdown containing, **Code**, **Markdown**, et al.
	* **.ipynb** files can only be opened via the Jupyter notebook system.

#### Lesson 8

* How to get the course notebooks from [GitHub](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

#### Lesson 9

* How to use Git and GitHub.
	


