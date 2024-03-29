# Complete Python Bootcamp
Coursework and notes from [Udemy](https://www.udemy.com/complete-python-bootcamp/)

The exercises of the course are on Github here: [https://github.com/Pierian-Data/Complete-Python-3-Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

### Table of Contents

* [Section 1: Course Overview](#1)
* [Section 2: Python setup](#2)
* [Section 3: Python Object and Data Structure Basics](#3)
* [Section 4: Python Comparison Operators](#4)
* [Section 5: Statements](#5)
* [Section 6: Methods and Functions](#6)
* [Section 7: Milestone Project - 1](#7)
* [Section 8: Object Oriented Programming](#8)
* [Section 9: Modules and Packages](#9)
* [Section 10: Errors and Exceptions Handling](#10)
* [Section 11: Milestone Project - 2](#11)
* [Section 12: Python Decorators](#12)
* [Section 13: Python Generators](#13)
* [Section 14: Advanced Python Modules](#14)
* [Section 15: Web Scraping with Python](#15)
* [Section 16: Working with images in Python](#16)
* [Section 17: Working with PDFs and Spreadsheet CSV Files](#17)
* [Section 18: Emails with Python](#18)
* [Section 19: Final Capstone Project](#19)
* [Section 20: Advanced Python Objects and Data Structures](#20)
* [Section 21: Introduction to GUIs](#21)

* **NOTE:** there are some **interview questions** listed throughout this course. Search on **"interview"** to find them.

* Also pay attention to the **Takeaways**, as they contain useful tips, memory aids, etc.


<a name="1"></a>
## Section 1: Course Overview

#### Lessons 1-4

* No notes taken

<a name="2"></a>
## Section 2: Python Setup

#### Lessons 5 & 6. Installing Python

> I do not install via [Anaconda](https://www.anaconda.com/distribution/), I use homebrew to install Python 3, and then execute [setup-mac.sh](https://gist.github.com/sund0g/3f6f62c4d7f1145ea1070fd9f255a1bc) to install the required modules. This means that the Jupyter notebooks will be started via the command line,

	nohup jupyter notebook &
	
This will start the server, (listening on localhost:8888) and launch a browser instance at the tree root.
	
> for notebook details, reference the [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running)

> I'm using `nohup` and `&` as part of the startup so I  can keep working in the same terminal window. To make shutting down Jupyter easier when done, make a note of the PID. If you don't, you can always use a combination of the `jobs` command to see if the server is running and then `ps` to get the PID, which can then be used to `kill <PID>` the server.

#### Lesson 7. Running Python Code

* Setting up the development environment.

> I do not use PyCharm or Sublime, I use VSCode with the python extension installed. Please refer to [setup-mac.sh](https://gist.github.com/sund0g/3f6f62c4d7f1145ea1070fd9f255a1bc) for details.

* The very first Python file is **helloworld.py**. I do this with every language I learn more out of nostalgia, but also as a base on which my knowledge base is built.

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
	* Type `print('Hello world')` in the cell, and click the **Run** button to execute the line.

		> **shift** + **return** also causes the cell to be executed.
		
	* To change what can be typed in a cell, select the dropdown containing, **Code**, **Markdown**, et al.
	* **.ipynb** files can only be opened via the Jupyter notebook system.
	* To display **function details**, position cursor next to the function name select **SHIFT + TAB**. This is a really cool feature of Jupyter notebooks.

#### Lesson 8. Notebooks and Course Material

* Course notebooks may be downloaded from [GitHub](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

#### Lesson 9. Git and GitHub

* How to use Git and GitHub.

<a name="3"></a>
## Section 3: Python Object and Data Structure Basics

#### Lesson 10. Intro to Data Types and Structures

* Overview of **Data Types**

	Name | Type | Description
	---|---|---
	Integer | int | Whole numbers 
	Floating point | float | Decimals
	String | str | Sequence of characters
	
* Overview of **Data Structures**

	Name | Type | Description
	---|---|---
	List | list | Unordered set of objects
	Dictionary | dict | Unordered set of key:value pairs
	Tuple | tup | Ordered, immutable set of objects
	Set | set | Unordered set of unique objects
	Boolean | bool | True, False
	
#### Lessons 11 & 12. Numbers and Arithmetic Operators

* **Arithmetic operators**

	Name | symbol | Description
	---|---|---
	Addition | + | x + y
	Subtraction | - | x - y
	Multiplication | * | x * y
	Division | / | x / y
	Modulo | % | x % y
	Exponentiation | ** | x ** y
	Orders of Operations | | [PEMDAS](https://www.mathsisfun.com/operation-order-pemdas.html)

> Can use a **Jupyter notebook** with Python as a calculator.

#### Lesson 13. Variable Assignments

* Rules for variable names
	
	* cannot start with a number
	* cannot contain spaces, (use '_')
	* cannot use special characters
	
* Suggestions for variable names
	
	* all lowercase, (exception may be globals)
	* avoid keywords

* Python uses **Dynamic Typing** meaning variables can be reassigned to different data types. There are pros and cons of this,

	* easy and faster to code
	* May result in bugs
	* Can use **type(\<variable\>)** to see the type of the variable.

#### Lessons 14 & 15. Intro to Strings

* **Strings** are sequences of 1 or more characters enclosed by either **''** or **""**.

* **Indexing** provides a method of extracting a character at an specified index, e.g. **[i]**
	> To get the last character in the string, use the index **-1**. This returns the last letter regardless of the string's length.
	
	some examples where mystring = "abcdefgh"
	
		mystring[3]	returns d
		mystring[-1]	returns h
		mystring[-2]	returns g
		
		Can also do this: "abcdefgh"[4] returns e
	
* **Slicing** provides a method of extracting a substring at a specified start and stop indices and step, e.g. **[start:stop:step]**
	> The substring does **not** include the **stop** index.
	
	some examples where mystring = "abcdefgh"
		
		mystring[3:]		returns defgh
		mystring[:3]		returns abc
		mystring[3:6]		returns def
		mystring[::2]		returns aceg
		mystring[2:7:2]	returns ceg
		
		Can also do this: "abcdefgh"[2:5] returns cde
	
---
#### Interview question
	
Reverse a string with a single command,
	
	mystring[::-1]	returns hgfedcba
	
Why? Because we are saying from string beginning to end (::) step backwards through the string.
	
---
	
* The **len(\<string\>)** function returns the length of the string.
	> Spaces count as part of strings.

#### Lessons 16 & 17. String Properties and Methods
		
* **String Properties**

	* Strings are **immutable** in Python, e.g
	
			name = 'Sam'
			name[0] = 'P' 
	won't work.
	
	* **concatenation** using **'+'** and **'\*'**
	
		* To simulate the above, do something like,
	
				last_letters = name[1:] returns "am"
				'P' + last_letters returns "Pam"
				
		* Another example,

				"Hello World" + " it is beautiful" 
			
			returns "Hello World it is beautiful"
			
		* Yet another example,
			
				letter = 'z'
				letter * 10
				
			returns "zzzzzzzzzz"
			
* **String Methods**

	* [Complete list as of v.3.7](https://docs.python.org/3.7/library/stdtypes.html#string-methods)
	* Common examples, where x = "Hello World"
	
			x.upper()	returns "HELLO WORLD"
			x.lower()	returns "hello world"
			x.split()	returns a list ["Hello", "World"]
			x.split('o')	returns ["Hell", " W", "rld"]
			
> '#' denotes a comment in Python

#### Lessons 18 & 19. Print Formatting

* **Basic formatting**

	* **String syntax**: "%s %s" % (variable1, variable2)

	> Not going into detail on this method here.
	
* **.format()**

	* **String syntax**: `"some string {} some other string {}".format(var1, var2)`
	
		examples,
		
			print("This is a string {}".format("INSERTED"))
		returns "This is a string INSERTED"
		
			print ("The {2} {1} {0}".format("fox", "brown", "quick"))
		returns "The quick brown fox" (inserting by **index position**)
		
			print ("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
		returns "The quick brown fox" (inserting by **keywords**)
			
	* **Float syntax**: `"{value:width.precision f}"`

		examples,
		
			result = 100/777
			print (result)
			
		returns 0.1287001287001287
		
			print ("The result was {}".format(result)) or
			print ("The result was {r}".format(r = result))
			
		returns The result was 0.1287001287001287
		
			print ("The result was {r:1.3f}".format(r = result))
			
		returns The result was 0.129
		
			print ("The result was {r:10.3f}".format(r = result))
			
		returns The result was      0.129
		
		> Usually the width will be 1, and is not played around with. the precision is what will be most used.
	
* **f-strings** (new in v.3.6)

	* **String syntax**: f"string {variable}"

		examples,
		
			name = "Scott"
			print(f"Hello, my name is {name}")
			
		returns Hello, my name is Scott
		
			age = 42
			print(f"{name} is {age} years old")
			
		returns Scott is 42 years old
			
---
#### Takeaways

* Additional resource for string formatting: https://pyformat.info/
* [**casefold()**](https://www.geeksforgeeks.org/case-insensitive-string-comparison-in-python/) is preferred over **lower()** and **upper()** when dealing with non-english languages because upper and lower case characters may not be the same, e.g.

		German ‘β’ (upper) is ‘ss’ (lower)

---

#### Lessons 20 & 21. Lists

* [**Lists**](https://docs.python.org/3/library/stdtypes.html?highlight=boolean#lists) are sequences of **ordered** objects.
* `[]` denote a list of `,` separated objects, e.g. `[1,2,3]`, `['STRING', 100, 23.2]`
* **Slicing** and **Indexing** are supported, as are **nesting** and various **methods**, e.g.

	where my_list = ['1','2','3']
	
		print(my_list[0])	returns 1				(indexing)
		print(my_list[1:])	returns ['2', '3']			(slicing)
		len(my_list)		returns 3				(method call)
		my_list + ['4','5']	returns ['1','2','3','4','5']		(concatenation)
		my_list.append('6')	returns ['1','2','3','4','5', '6']	(method call)
		my_list.pop(0)	returns ['2','3','4','5', '6']		(method call)

* List elements are **mutable** unlike string characters.

* [Methods list as of v.3.7](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20object)

> [**Sorting**](https://docs.python.org/3/howto/sorting.html) methods `.sort`, `.reverse`, et al, for lists are **in place** meaning the methods do not return anything, sorting is done on the original string *in place*.
> 
> To return a sorted string, use the **sorted(<list>)** command.

---
### Question

* How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?

* Answer: just **add another set of brackets** for indexing the nested list, for example: my_list[2][1] 

---

#### Lessons 22 & 23. Dictionaries

* [**Dictionaries**](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20object#dictionaries) are sequences of **unordered** objects using **key:value** pairings.
* `{}` denote a set of `:` separated objects and their keys, e.g. `{'key1':'value1','key2':'value2'}`

> **keys** should always be strings

* Differences between **lists** and **dictionaries**

	List|Dictionary
	---|---
	Objects retrieved by **location**|Objects retrieved by **key**
	**Ordered sequence** can be indexed or sliced|**Unordered**, **cannot** be sorted

* To **retrieve** an object from a dictionary,

	where my_dict = {'k1':42,'k2':[0,1,2],'k3':{'insidekey':100},'k4':['a','b','c']}
	
		print(my_dict['k1'])				returns 42
		
* Dictionaries support **any object types** and **multiple stacking**, e.g.

		print (my_dict['k3']['insidekey'])	returns 100
		print (my_dict['k2'][2])		returns 2
		print(my_dict['k4'][2].upper())	returns C
		
* To **add** or **overwrite** an object to a dictionary,

	where my_dict1 = {'k1':100,'k2':200}
	
		my_dict1['k3'] = 300		returns {'k1': 100, 'k2': 200, 'k3': 300}
		my_dict1['k1'] = "NEW VAL"	returns {'k1': 'NEW VAL', 'k2': 200, 'k3': 300}
		
* **Useful methods**

		print(my_dict1.keys())	returns dict_keys(['k1', 'k2', 'k3'])
		print(my_dict1.values())	returns dict_values(['NEW VAL', 200, 300])
		print(my_dict1.items())	returns dict_items([('k1', 'NEW VAL'), ('k2', 200), ('k3', 300)])
		
---
#### Question

* How do I print the values of the dictionary in order?

* Answer: Dictionaries are mappings and do not retain order. If order is needed, use the **ordereddict** object

---

#### Lesson 24. Tuples

* [**Tuples**](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20object#tuples-and-sequences) are similar to **Lists** with the exception that **Tuples** are **immutable**, i.e. once an object is inside a Tuple, it cannot be reassigned.

	> Tuples provide **data integrity**.

* `()` denote a list of `,` separated objects, e.g. `(1,2,3)`
* There are only **2 methods** for tuples, **count** and **index**, e.g.

	where my_tuple = ('a','a','b')
	
		print(my_tuple.count('a'))	returns 2 (number of times 'a' is in the my_tuple)
		print(my_tuple.index('a'))	returns 0 (the index of the FIRST 'a')
		print(my_tuple.index('b'))	returns 2 (the index of 'b')

* If you try to reassign an object inside a tuple, an error will be returned, e.g.

		my_tuple[0] = 'NEW'	returns TypeError: 'tuple' object does not support item assignment
		
---
#### Takeaways

* **Tuples** are very useful when passing objects that are not to be changed.

---

#### Lesson 25. Sets

* [**Sets**](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20object#sets) are **unordered** collections of objects with **unique** values.

* `{}` denote a set of `,` separated objects, e.g. `{1,2,3}`

* The **elements** in a set are **immutable**.

* `set()` is the syntax to create a set, e.g. `my_set = set()`
* Examples,

		my_set = set()		creates an empty set
		my_set.add(1)		adds the number 1 to my_set
		my_set.add(2)		adds the number 2 to my_set
		print(my_set)		returns {1, 2}
		
* To test object **uniqueness**,

		my_set.add(2)		try to add another number 2 to the previous set.
		print(my_set)		returns {1, 2} (set detected there was already a 2 in my_set.)
		
* Adding objects to sets one at a time is not very useful. A better use case is **casting a list** into a set to obtain the lists' **unique values**, e.g.

	where my_list = [1,1,1,2,2,2,3,3,3]
	
		set(my_list)	returns {1, 2, 3}
		
#### Lesson 26. Booleans

* **Booleans** are operators that provide a way to convey **True** or **False**.

> The keyword **None** may be used as a placeholder value as needed, e.g. `b = None`

#### Lesson 27. [File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

* To create a file in a **Jupyter notebook**, enter `%%writefile <yourfilename.ext>`, and then add the lines of content in the same cell before running.

> I'm using MSCode to create files for this course.

* To get started with basic file I/O,
	1. Create a file **myfile.txt** in the working directory.
	2. Add the lines, 
		
			Hello this is a text file
			This is the second line
			This is the third line
			
* To get the working directory in Jupyter, execute `pwd` in a cell, (same as command line.)

* There are a couple of ways to **open** a file,
	1. `myfile = open('myfile.txt')`
	2. `with open('myfile.txt') as myfile: /n/t<code block>`

	> While method 1 works, you have to remember to close the file with .close(). [Method 2](https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for) auto-closes the file.
	>
	> An **ErrorNo 2** will be returned if 1) the file doesn't exist, or 2) The working directory is incorrect.

* [Methods list as of 3.7.2](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* **Method examples**

		myfile.read()			returns the entire file as a single \n-delimited line.
		myfile.seek(0)		resets the file counter to the file head.
		myfile.readlines()		returns the file as a list with the lines as objects.
		myfile.write('<content>')	writes <content> to file.
		myfile.close()		closes the file.		
	> The **.read methods** leave the file counter at the end of the file. It has to be reset before reading the file again using the **.seek(0)** method.
			
* File **modes** and **permissions** are set with the additional syntax, `mode='mode'`, e.g.

	Mode|Description
	---|---
	mode='r'| read only
	mode='w'| write only (will overwrite existing or create new)
	mode='a'| append only
	mode='r+'|read and write
	mode='w+'| read and write (will overwrite existing or create new)
	
* Simple **write** example,

		x = open('myfile1.txt',mode='w')
		x.write('This is a new file and has been created by Python')
		x.close()

* **with "append"** example,

		with open('myfile.txt',mode='a') as myfile:
			myfile.write('\nFOUR ON FOURTH')
		
* **with "read"** example,

		with open('myfile.txt', mode='r') as myfile:
    		print(myfile.read())
			
		returns
		
		Hello this is a text file
		This is the second line
		This is the third line
		FOUR ON FOURTH

---
#### Interview Prep Resources

* [Basic practice](https://codingbat.com/python)
* [Mathematical practice](https://projecteuler.net/archives)
* [More practice](http://www.codeabbey.com/index/task_list)
* [Dailyprogrammer Reddit](https://www.reddit.com/r/dailyprogrammer)
* [Trick and Advanced questions](http://www.pythonchallenge.com/)

---

#### Lessons 28-31. Practice resources and section tests

* download the notebook to take the exam.

<a name="4"></a>
## Section 4: Python Comparison Operators

#### Lesson 32. Comparison Operators

Operator|Description|Example
---|---|---
==|If the values of two operands are equal, then the condition becomes true.|(a == b) is not true.
!=|If values of two operands are not equal, then condition becomes true.|(a != b) is true.
<>|If values of two operands are not equal, then condition becomes true.|(a <> b) is true. This is similar to != operator.
\>|If the value of left operand is greater than the value of right operand, then condition becomes true.|(a > b) is not true.
<|If the value of left operand is less than the value of right operand, then condition becomes true.|(a < b) is true.
/>=|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true|(a >= b) is not true.
<=|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|(a <= b) is true.

#### Lesson 33. Chaining Comparison Operators with Logical Operators

Operator|Description|Example
---|---|---
and/AND|If both the operands are true then condition becomes true.|(a and b) is true.
or/OR|If any of the two operands are non-zero then condition becomes true.|(a or b) is true.
not/NOT|Used to reverse the logical state of its operand.|Not(a and b) is false.


<a name="5"></a>
## Section 5: Statements

> All examples in this section are contained in the Jupyter notebook.

#### Lesson 34. If Elif and Else Statements

* Control flow syntax uses **:** and **indentation (whitespace)**, e.g.

		if condition:
			# code block
		elif:
			# code block
		else:
			# code block

#### Lesson 35. For Loops
			
* Most of **objects** in Python are **iterable**.
* **for** syntax is,
		
		for <every_item> in <some_sequence>:
			# code block

* **'_'** can be subsituted for \<every_item\> if no action is taken on \<every_item\>, e.g.

		for _ in (1, 2, 3):
			print ('Hi!')
			
		returns
		
		'Hi!'
		'Hi!'
		'Hi!'
		
* **Unpacking** or iterating over every data object in another data object can be useful, e.g.

		list_of_tuples = [(1, 2), (3, 4)]
		
		for a,b in my_list1:
			print (f'{a} \n{b}')
			
		returns
		1
		2
		3
		4
		
		---
		
		my_dictionary = {'k1':1, 'k2':'Hello!', 'k3': 3.25}
		
		for item in my_dictionary:
			print (item)
			
		returns
		
		k1
		k2
		k3
		
* Note: this only returns the keys. To return the corresponding values, use the [**.items()**](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) method.
		
		for key,value in my_dictionary.items():
			print (f'key = {key} value = {value}')
			
		returns
		
		key = k1 value = 1
		key = k2 value = Hello!
		key = k3 value = 3.25
		
* To only return the values, use the [**.values()**](https://www.tutorialspoint.com/python/dictionary_values.htm) method.

		for value in my_dictionary.values():
			print (f'value = {value}')
			
		returns
		
		value = 1
		value = Hello!
		value = 3.25
		
* This has nothing to do with **looping**, but if all is needed are the dictionary values, 

		print (f'values = {my_dictionary.values()}')
	
		returns
		
		values = dict_values([1, 'Hello!', 3.25])
		
---

#### Takeaways
* **Unpacking** is common in Python

---

#### Lesson 36. While Loops

* **While** loop syntax uses **:** and **indentation (whitespace)**, e.g.

		while <boolean condition>:
			# code block
		else:
			# code block
			
* There are three **keywords** that can be useful with while loops,

	Keyword|Description
	---|---|---
	**break**|Breaks out of the current closest enclosing loop.
	**continue**|Goes to the top of the closest enclosing loop.
	**pass**|Does nothing. This may be useful when getting the flow logic in place.


> It’s easy to create infinite while loops by forgetting to put in the iterator, e.g. x +=1. If this happens while running the loop in a Jupyter notebook, select **Kernel** and **Interrupt** from the dropdown menu at the top of the notebook.

#### Lesson 37. Useful Operators in Python

* The following are a few useful keywords that don’t really fit into any of the previous categories.

 Operator|Description
	---|---|---
	**range**|Generates a range of items as specified in the parameters.
	**enumerate**|Generates tuples from the items in a iterable.
	**zip**|Combines multiple lists into a single list. **Note** zip does not return an error with uneven lists, it ignores the extra items.
	**in**|Checks if an item is in an iterable.
	**min**|Returns the minimum value in an iterable.
	**max**|Returns the maximum value in an iterable.
	**shuffle**|Randomly shuffles items in an iterable. This is an **in place** function; it doesn’t return anything.
	**randint**|returns a random integer.
	**input**|asks for an input from user. **Note:** input only returns a string. Cast to get a non-string type.
	
> Some of these functions generate data, but do not store it, so can be more efficient. Will discuss in detail in Section 13.

#### Lesson 38. List Comprehensions in Python

* List comprehensions can quickly create a list.
* If you find yourself using a **for** loop with **.append()** to create lists, **list comprehensions** are a great alternative.

> All examples are in the accompanying Jupyter notebook **section-5.ipynb**

* List comprehensions do not save compute time. **They also do not always lend themselves to readability which should always be paramount when writing code.**


#### Lessons 39-40. Python Statements Test and Solutions

* Here is the test: [https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/07-Statements%20Assessment%20Test.ipynb](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/07-Statements%20Assessment%20Test.ipynb)

* Test solutions: [https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/08-Statements%20Assessment%20Test%20-%20Solutions.ipynb](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/08-Statements%20Assessment%20Test%20-%20Solutions.ipynb)

---
#### Interview question

* Classic “FizzBuzz” question
	* Write a program that prints the integers from 1 to 100. 
	* For multiples of three, print “Fizz” instead of the number.
	* For multiples of five, print “Buzz” instead of the number.
	* For numbers which are both multiples of three and five, print “Fizzbuzz” instead of the number.
 

		for num in range(0,101):
			if num%3 == 0 and num%5 == 0:
				print(‘FizzBuzz’)
			elif num%3 == 0:
				print(‘Fizz’)
			elif num%5 == 0:
				print(‘Buzz’)
			else:
				print(num)

* **NOTE: make sure to check for multiples of 3 and 5 FIRST. This keeps the logic correct.**

---

<a name="6"></a>
## Section 6: Methods and Functions

#### Lesson 41. Methods and the Python Documentation

> All examples are in the accompanying Jupyter notebook **section-6.ipynb**

* **Methods** are functions that are built into objects, e.g.

		myList = [1,2,3]
		
		myList.append(4)		# append method adds 4 to the list.
	
		myList.pop()			# pop method removes the last item in the list.
		
* To show the available methods for a particular **iterable** in a **jupyter notebook**, type in the iterable and ‘.’ and *tab*. This will show a dropdown list of available methods. **Note: this doesn’t work for me.**

* To show the method’s **help** syntax in a **jupyter notebook**, type in the method and then *shift + tab*.

* If running in a script or on the Python command line, use

		help(myList.<method>)
		
* The full help documentation is at the [official Python documentation](https://docs.python.org/3/) site.

#### Lesson 42. Introduction to Functions

* **Functions** are blocks of code that can be easily executed many times without needing to rewrite the code each time.

#### Lesson 43. def Keyword

* Syntax: **def function_name():**

> In general, Python uses **snake casing** which means all lowercase words separated by underscores. OO class calls generally use **camel casing**.

* Optionally a **multi-line string** describing the function can be added as follows,

		def my_function():
			‘’’	multi-line ‘docstring’
				function description
			‘’’
			
			function code...
					
> My preference is to use ‘#’ for all comments to maintain consistency. Note this is single-line only, so every comment line must have this at the start of line.

* Everything after the ‘:’ that is part of the function must be indented.

* In general, a function will return a value via the **return** keyword, e.g.

		def add_function(number1, number2):
			return number1 + number2

#### Lesson 44. Basics of Python functions

* Executing a Python function requires appending **()** to the function name. Omitting the **()** simply verifies the function name, e.g.

		> my_function
		>
		> <function __main__.my_function>
		
* The difference between **print** and **return** is that **print** simply prints out a value. **return** assigns the value to a variable which can then be used later by other functions.

* Python is dynamically typed, which can cause issues, (see takeaways), e.g.

		def sum_numbers(number1, number2):
			return number1 + number2
			
		>sum_numbers(10, 20)
		> 30
		>
		>sum_numbers(’10’, ’20’)
		> ‘1020’

> ‘+’ **adds** numbers, and **concatenates** strings.

 ---
#### Takeaways
 
 * Python is dynamically typed, (unlike C or C++ which are statically typed). This means function parameters do not have to be type-checked when passed into the function. However, this can cause unexpected side effects, so adding type checking is a generally accepted principle. An example of how to do this will be shown later.

 * **Another generally accepted principle is to only have a single “return” per function. While having multiple returns, e.g. in an if-else statement will not generate a syntax error, this is considered poor design.**

 ---

#### Lesson 45. Logic with Python Functions

* Checking for even numbers examples are all in the Jupyter notebook, **section-6.ipynb**, lesson 45.

#### Lesson 46. Tuple Unpacking with Python Functions

* Unpacking employee of the month data example is in the Jupyter notebook, **section-6.ipynb**, lesson 46.

#### Lesson 47. Interactions between Python functions

* Create some functions that mimic, [Three Card/Cup Monte](https://en.wikipedia.org/wiki/Three-card_Monte).
	* The example will not show the cards/cups, but will be mimicked with a Python list.
	* The cards/cups will not be shuffled, so the guess will be completely random.

* The shuffle will be mimicked using the Python [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) method from the [random](https://docs.python.org/3/library/random.html) module

* **Step 1**: Mimic the shuffle. [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) is an **in place** function, so have to create a shuffle function.

* **Step 2**: Get the player’s guess.

* **Step 3**: Check the player’s guess, and check if it matches the shuffled list.

* **Step 4**: Create a script that calls all the functions.

---
#### Takeaways

* The **input** function only returns strings, so may have to cast the returned variable if something other than a string is needed.

---

#### Lesson 48. Overview of Quick Function Exercises

* Review only, no notes taken.

#### Lesson 49. \*args and \*\*kwargs in Python

* **\*args** and **\*\*kwargs** provide a method to pass in a variable set of arguments to a function, e.g.

		some_function(a, b)	# a, and b are “positional” arguments, meaning they must be
							# provided in the proper order when calling the function.
							
		some_other_function(*args)	# Any number of variables may be passed into the function.

* [geeksforgeeks](https://www.geeksforgeeks.org/args-kwargs-python/) has a description for these.

* **\*args** builds a tuple out of the variable set of arguments.

* **\*\*kwargs** builds a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) out of the variables passed into the function. 

---
#### Takeaways

* **\*args** returns a [**tuple**](https://www.geeksforgeeks.org/python-tuples/)

* **\*\*kwargs** returns a [**dictionary**](https://www.geeksforgeeks.org/python-dictionary/)

* There is nothing special about *\*args* or *\*\*kwargs*, it can be anything for readability, but it must be denoted by the **\***. However, it is standard convention to use **args**.

* In the first example, [sum()](https://docs.python.org/3/library/functions.html#sum) is used. This function only accepts iterables. Integers are not accepted.

* **\*args** and **\*\*kwargs** are most useful when using external libraries.

#### Lessons 50, 51, 52, 53, 54. Function Practice Exercises

* Course [solutions](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb) for review as needed.

> My solutions to these problems are in the Jupyter notebook **section-6.ipynb**


---
#### Takeaways

* Get in the habit of writing code. Even the simplest problems take forever if you are out of practice.

* The string method [.join](https://www.geeksforgeeks.org/python-string-join-method/) is introduced

* The [absolute value](https://en.wikipedia.org/wiki/Absolute_value) method [abs()](https://www.geeksforgeeks.org/abs-in-python/) is introduced

* Check out the [Euler project](https://projecteuler.net/) for more challenging math problems solved with code.

---

#### Lesson 55. Lambda Expressions, Map, and Filter Functions

> All examples are in the accompanying Jupyter notebook **section-6.ipynb**

* [**Lambda Expressions**](https://docs.python.org/3/reference/expressions.html#lambda) are a way to create what are known as [**anonymous functions**](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)

	> Lambda functions are basically one-time use functions. They are used once and then never referenced again.

* [**map**](https://www.geeksforgeeks.org/python-map-function/) and [**filter**](https://www.geeksforgeeks.org/filter-in-python/) must be understood in order to understand **Lambda** functions.

* [**map(function, iterable)**](https://docs.python.org/3/library/functions.html#map) function takes as inputs a function and an iterable. It then applies the function to each item in the iterable, e.g.

		def square(number):
			return number**2
			
		myNumberList = [1, 2, 3, 4, 5]
		
		list(map(square, myNumberList))
		
		# returns [1, 4, 9, 16, 25]

* [**filter(function, iterable)**](https://docs.python.org/3/library/functions.html#filter) executes a function on each item in an iterable, and returns the items for which the function returns **True**, e.g.

		def check_even(number):
			return number % 2 == 0
			
		myNumbers = [1, 2, 3, 4, 5, 6]

		list(filter(check_even, myNumbers))
		
		# returns [2, 4, 6]
		
	> Functions passed into map() and filter() do not include **()** because map will execute them.
	
* To show how [**Lambda**](https://docs.python.org/3/reference/expressions.html#lambda) functions are useful, and connect **map()**, **filter()**, and **lambdas** together, we will convert one of the previous simple functions to a Lambda function, e.g.

		 
		# Regular function
		
		def square(number):
			return number**2
			
		# Written as a lambda function
		
		lambda number: number ** 2
		
		
* Combining the lambda with map() looks like,

		list(map(lambda number: number**2, [1, 2, 3, 4]))
		
		# returns [1, 4, 9, 16]

* Combining the lambda with filter() looks like,

		list(filter(lambda number: number % 2 == 0, [1, 2, 3, 4, 5, 6]))
		
		# returns [2, 4, 6]
		
	> Lambdas are very useful in single-use scenarios rather than creating a function as shown in the previous examples square() and check_even().
	
---
#### Takeaways

* **Lambda functions** can become quite complex. Keep in mind that not all functions are appropriate to define as lambdas because they will be hard to read.

---

#### Lesson 56. Nested Statements and Scope

* Python variables are given a [**namespace**](https://www.geeksforgeeks.org/namespaces-and-scope-in-python/) and [**scope**](https://www.geeksforgeeks.org/namespaces-and-scope-in-python/)

* The following example demonstrates variable **scope**,

		number = 25
		
		def printNumber():
			number = 50
			return number
			
		print (number)
		
		# What is number?
		#
		# It is 25 because number as defined inside printNumber() has a scope that only
		# exists while inside printNumber(), e.g.
		
		print(printNumber())		# returns 50
		
* Python uses the [**LEGB Rule**](https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/) format to determine scope of variables.

	* **L: Local** - Names assigned in any way within a function (def or lambda) and not declared global in that function.
	* **E: Enclosing function locals** - Names in the local scope of any and all enclosing functions (def or Lambda), from inner to outer.
	* **G: Global (module)** - Names assigned at the top-level of a module file, or declared global in a def within the file.
	* **B: Built-in (Python)** - Names preassigned in the built-in names module, e.g. **open**, **range**, **SyntaxError**, etc.

* Some examples,

		# L: Local
		
		lambda num: num**2	# num is local to the lambda function
		
		# E: Enclosing
		
		name = “This is a global string”
		
		def greet():
		
			name = “Sammy”
			
			def hello():
				print (“hello ”+name)
				
			hello()
			
		greet()					# name is “Sammy”
		
* Sometimes a function may want to modify a global variable. This is done with the [**global**](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-global_stmt), e.g.

		x = 50
		
		def myFunc():
		
			global x
			
			print(f”x = {x}”)
			
			# local reassignment of global variable
			x = 200
			
			print(f”x changed to {x}”)
			
			
		# Calling myFunc() returns,
		#	x = 50
		#	x changed to 200
		
---
#### Takeaways

* Never overwrite **built-in functions/variables**.
* The use of **global** to change global variables inside of functions is not recommended. The general convention is to pass in global variables, operate on them, and **return** them.

	> Using **global** in complex functions can cause global variables to be inadvertently modified, which can be challenging to debug.

---

#### Lessons 57 and 58. Methods and Functions Homework

* Course [solutions](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb) for review as needed.

> My solutions to these problems are in the Jupyter notebook **section-6.ipynb**

---
#### Takeaways

* Use the [**set**](https://www.geeksforgeeks.org/python-set-method/) method to quickly return a list of unique elements in an iterable, (Homework 4).

---

<a name="7"></a>
## Section 7: Milestone Project - 1

> All examples are in the accompanying Jupyter notebook **section-7.ipynb**

#### Lesson 59: Introduction to Warm Up Project Exercises

* Most interactive programs work in this simple idea:

	* Display something visual to the user
	* Let user update via an interaction
	* Update variables in the program
	* Display updated visual

* The following lessons show how to perform these tasks with Python. We will emulate a [tic-tac-toe game](https://en.wikipedia.org/wiki/Tic-tac-toe)

#### Lesson 60. Displaying Information

* Use a **def** custom function along with **print** to show something like a board game to the user.

#### Lesson 61. Accepting User Input

* Using the [input()](https://docs.python.org/3/library/functions.html#input) to accept the user input.

> Note: When executing an **input** command in a **Jupyter notebook** select **shift** + **return**

---
#### Takeaways

* Remember, the **input()** function only returns strings. If int or float are needed, cast the result of the input.

* If the **input** command is executed from a **Jupyter notebook**, and the user doesn’t actually enter a value, all subsequent commands in the notebook will wait until a value is entered before they can be executed. 

* If the user “accidentally” selects **shift** + **return** without entering a value, the Jupyter notebook **kernel** must be restarted via **Kernel** | **Restart** before any subsequent commands can be executed.

	> This will null out all previous values. Select **Cell** | **Run All** to repopulate the variables.

---

#### Lesson 62. Validating User Input

* The next step is to validate the user input to void errors and unintended side effects.

* There are several method to determine if input is valid,
	* (isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit) Using this for the project.
	* [Try|Except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
	* Simple loops

#### Lesson 63. Simple User Interaction

* Put the previous lessons together into a simple user interaction,
	* Display a list
	* Input an index position and a variable
	* replace list value at the index position with the user’s input variable
	* **Also, check if the user wants to exit out at any time**

#### Lessons 64 - 67. First Python Milestone Project

* Take what has been learned in the previous lessons and create a Python program to emulate a tic-tac-toe game for 2 human players.

* The instructor’s solutions can be reviewed [here](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/04-Milestone%20Project%20-%201) on gitHub.

* Objectives for the game are,

	* 2 players should be able to play the game while sitting at the same computer.
	* The board should be updated and displayed after every player move.
	* The program will accept input of player position and place a symbol on the board.
	* The board will emulate a **numpad** for the positions, e.g.

			7|8|9
			4|5|6
			1|2|3
			
* The functions and design comments are all in the Jupyter notebook, **section-7.ipynb**

---
#### Takeaways

* To populate an empty list, do the following,

		myList = [‘ ‘] * <how any elements needed>
		
* The player info, (which player is X and which is O) can be stored as a **tuple** because we don’t want their values to change.

* The solution is implemented with a 1D array, (list). Check out how to do this with a [**2D array, (list)**](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/).

* **DON’T** get messed up with the **0 vs 1** starting index. This will waste hours of time debugging the logic when you get it wrong. Make it simple create a 10 space list, and start the index at 1. This way the index position will never be 0, which will cause issues the first time the logic executes.

---

<a name="8"></a>
## Section 8: Object Oriented Programming

#### Lesson 68. Object Oriented Programming - Introduction

> All examples are in the accompanying Jupyter notebook **section-8.ipynb**

* OOP allows developers to create objects that have methods and attributes.
* These methods act as **functions** that use information about ab object, as well as the object itself, to return results or change the object, e.g **appending to a list** or **counting occurrences of an element in a tuple.**
* In general, OOP provides a way to create code that is **repeatable** and **organized**.
* an exampe of OOP syntax is,

		class NameOfClass():
		
		def __init__(self, param1, param2):
		   self.param1 = param1
		   self.param2 = param2
		
		def some_methods(self):
		   #perform some action
		   print(self.param1)
		   
> **Objects** and **Classes** nomenclature are interchangeable. They mean the same thing.
> **Functions** are called **methods** when they are part of a **class**.

* Breaking down the above example,
	* **def** is called a **method** when inside a class.
	* [**__init__**](https://docs.python.org/3/tutorial/classes.html#class-objects) is the class **constructor**.
	* [**self**](https://docs.python.org/3/tutorial/classes.html#class-objects) is how the instantiated object refers to itself.
	* **self.param** links the passed in parameter to the object instance. 
	* Passing **self** to the class methods tells us the method is not random, but belongs to the class.
 
#### Lesson 69. Object Oriented Programming - Attributes and Class Keyword

* Use the **class** keyword to create a user defined object.
* **Classes** have **attributes** and **methods**, e.g.
	* an **attribute** of **class Dog()** could be **breed**.
	* a **method** of the class could be **walk()**.

* By convention **attributes** are the same name, e.g.

		class Dog():
		  def __init__(self, breed)
		     self.breed = breed
		     
* Attributes can be of any type. 

---
#### Takeaways

* By convention classes are **CamelCase**

> [Here](https://peps.python.org/pep-0008/) is an example style guide for Python.

* Classes and their methods should generally have a [**docstring](https://www.geeksforgeeks.org/python-docstrings/) to help with usage.

---

#### Lesson 70. Object Oriented Programming - Class Object Attributes and Methods

* **Class object attributes** will be the same for any instance of the class, e.g.

		class Dog():
		
		  # Class object attribute
		  # will be the same for any instance
		  # does NOT refer to self because is the same for any instance.
		  genus = “canis”
		
		  def __init__(self, breed)
		     self.breed = breed	
		     
* **Methods** are functions defined inside the body of a class.
	* They are used to perform operations, sometimes on the attributes of the instantiated object.
	* They can also take user arguments

	Example
	
		class Dog():
		
		  def __init__(self, breed)
		     self.breed = breed	
		     
		  def say_number(self, number):
		     print(“WOOF! The number is {}”.format(number))
		     
* **Attributes** can be passed in as parameters, e.g.

		class Circle():
    
    		# Class object attribute
    		pi = 3.14
    
    		# Constructor class
    		def __init__(self, radius=1): # giving radius a default value
        
        	self.radius = radius
        
        	# Example of an attribute passed in as a parameter
        	self.area = self.pi * (radius **2)
        	
* **Class object attributes** may also be reference by their class name, e.g.

		class Circle():
    
		    # Class object attribute
		    pi = 3.14
		    
		    # Constructor class
		    def __init__(self, radius=1): # giving radius a default value
		        self.radius = radius
		    
		    # Class method
		    def get_circumference(self):
		    
		    	 # Class object attribute referenced by class name 
		        return 2 * Circle.pi * self.radius	

---
#### Takeaways

* **Attributes** are informational only. They are not called with **()**.
* By convention, **class object attributes** are referenced by their **class name** because they will always be the same for any instance, and it make it easier for others to read.
* **Methods** will perform an action, and must be called with **()**.

---

#### Lesson 71. Object Oriented Programming - Inheritance and Polymorphism

* [**Inheritance**](https://www.w3schools.com/python/python_inheritance.asp) basically means the ability to create new classes from classes that are already defined.
* A **child** class can **derive** methods and attributes from another class called the **parent** or **base** class, e.g.


		class ParentClass():
			
			def __init__(self):
			
		---
		
		class ChildClass(ParentClass):
		
			def __init__(self):			# Child class constructor
			
				ParentClass.__init__(self)	# also need to create an instance of the derived class


* Another example,
  

		# Base/Parent class
		
		class Animal():
    
    		def __init__(self):
        
        		print("Animal created")
        
	    def who_am_i(self):
	        print(“I am an aminal”)
	        
	    def eat(self):
	        print(“I am eating”)
	    
	    --- 
	        
	    # Derived/Child class
	    
	    class Dog(Animal):				# Class Dog() inherits methods/attributes from class Animal()
	    
	    	def __init__(self):
	    	
	    		Animal.__init__(self)	# Create an instance of the parent class
	    		print(“Dog created”)
	    		
* Child classes can **override** parent class methods and attributes, as needed, e.g.

		# Derived/Child class

		class Dog(Animal):              
	    def __init__(self):
	
	        Animal.__init__(self) 
	        print(“Dog created”)
	    
	    # Parent class method override
	        
	    def who_am_i(self):
	    	print(“I am a dog”)
	    	

* [**Polymorphism**](https://www.geeksforgeeks.org/polymorphism-in-python/) refers to the way that different **object methods** can share the same name.

* A simple example of polymorphism is,

		class Dog():
    
		    def __init__(self, name):
		        self.name = name
		        
		    def speak(self):
		        return f”WOOF! My name is {self.name}”
	
		---
		
		class Cat():
    
		    def __init__(self, name):
		        self.name = name
		        
		    def speak(self):
		        return f”MEOW! My name is {self.name}”
		        
		---
		
* Both classes contain the “speak()” method. Each method is unique to its respective class, but it has the same name. this means the **speak()** method is **polymorphic**.

* [**Abstract classes**](https://www.geeksforgeeks.org/abstract-classes-in-python/) can be used as a **base class** for child classes. **ABS** classes are not instantiated.

> Refer to the ABS example in the Jupyter notebook **section-8.ipynb**.

> A real world example of an **ABS** class could be a **File** class with an **open** method. **Subclasses** based on the file types would then use the ABS class to open files the same way.


---
#### Takeaways

* **Functions** can take in different arguments. **Methods** belong to the **objects** they act on.
* **Sub classes** do not need a **constructor** class if they use an **Abstract class**. They will use the constructor from the **ABS** class.

---

#### Lesson 72. Object Oriented Programming - Special (Magic/Dunder) Methods

* Special methods called [**Magic/Dunder**](https://www.geeksforgeeks.org/dunder-magic-methods-python/) allow us to emulate **built-in** functions with our **user-defined objects**.


#### Lessons 73 and 74. Object Oriented Programming - Homework

* The homework problems are in the coursework [**here**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb)

---
#### Takeaways

* Most class methods will take in **iterables**, so get comfortable,
	* unpacking tuples
	* parsing lists, dictionaries, sets, etc.

---

#### Lessons 75 and 76. Object Oriented Programming - Challenge

* The challenge problem is in the coursework [**here**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/04-OOP%20Challenge.ipynb)

---

<a name="9"></a>
## Section 9: Modules and Packages

#### Lesson 77. Pip Install and PyPi

* [**PyPi**](https://pypi.org/) is a repository for open-source, third-party Python packages, (similar to npm for node.js).
* [**pip**](https://packaging.python.org/en/latest/tutorials/installing-packages/) can be used to install Python packages.
* [**Anaconda**](https://www.anaconda.com/products/distribution) can be used as well, most often with Data Science packages.

> I did not install the [**colorama**](https://pypi.org/project/colorama/) package as shown in the lesson.

---
#### Takeaways

* Type **quit()** to exit the Python command line from a terminal window. (I tend to forget this).

* Use a web-based search to search for Python packages.

---

#### Lesson 78. Modules and Packages

* **Modules** are just **.py scripts** that are called in another .py script.
* **Packages** are a collection of **modules**.

* all example script files can be found in the directory **section-9**.

> Part of the lessons will be to create these files from an editor. I personally use [**vscode**](https://code.visualstudio.com/).

* A simple example of a **module** looks like the following,

		# Module file mymodule.py
		
		def my_func():
		     print(“I am in mymodule.py”)
		     
		---
		
		# Calling file myprogram.py
		
		from mymodule import my_func
		
		print my_func()
		
		---
		Output:
		
		--> python3 ./myprogram.py
		--> I am in mymodule

	> **mymmodule.py** and **myprogram.py** can be reviewed in the directory **section-9**.
		
* As modules become more complex and/or numerous, they can be aggregated into [**packages**](https://docs.python.org/3/tutorial/modules.html#packages)

* An example of how to create a [**package**](https://docs.python.org/3/tutorial/modules.html#packages) looks like,

	1. Create a directory **MyMainPackage**
	2. Create a subdirectory under **MyMainPackage** called **SubPackage**
	3. Create an empty file, **\_\_init\_\_.py** in both **MyMainPackage** and **SubPackage** directories.

			--> touch __init__.py

		> The existence of an **\_\_init\_\_.py** tells the Python interpreter to treat all files in the directory as a **package**.
		
	4. Create a file **some\_main\_script.py** in **MyMainPackage**.
	5. Create the functions inside the scripts.

		> Contents of the scripts can be copied from the directories **MyMainPackage** and **SubPackage**
		
	6. Create a new file in **section-9** called **packagetest.py** that calls the package functions,

			from MyMainPackage              import some_main_script
			from MyMainPackage.SubPackage   import mysubscript
			
			some_main_script.report_main()
			
			mysubscript.sub_report()
	
	7. Execute the **packagetest.py** script as follows,

			--> python3 ./packagetest.py
			
			---
			Output:
			
			I am a function in some_main_script.py
			I am a function in mysubscript.py
	

---
#### Takeaways

* **Packages** are simply collections of **modules** that are often grouped in **directories**.
* Python will interpret any **directory** containing the file **\_\_init\_\_.py** as a **package**.

---

#### Lesson 79. \_\_name\_\_ and “\_\_main\_\_”

* Most Python scripts will have the following line at the end of the script with a block of code to be executed,

		if __name__ == “__main__”:
			# code block

> Review the **README** in **section-9** for a full description of what this does.

* [**\_\_name\_\_**](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy) is a **built-in variable**
* **python** automatically assigns the **\_\_name\_\_** variable to **\_\_main\_\_** any time a python script is executed, e.g.

		--> python3 somefile.py
		
* The **if \_\_name\_\_ == “\_\_main\_\_”:** line is used to organize the code in the script to basically emulate the **main()** structure in other languages.

* An example of how this works is as follows,

	1. Create two files, **one.py** and **two.py** in **section-9**.
	2. Copy the file contents of **one.py** and **two.py** from [**Sund0g’s repo**](https://github.com/sund0g/python-bootcamp/tree/master/section-9)
	3. Execute the following commands from **section-9** to see how all this works,

			-->python3 ./one.py
			
			---
			Output:
			
			Top level in one.py
			one.py is being executed directly
			
			---
			
			--> python ./two.py
			
			--
			Output:
			
			Top level in one.py
			one.py has been imported
			Top level in two.py
			func() in one.py
			two.py is being executed directly


---
#### Takeaways

* **python** doesn’t have the concept of a **main()** function that other languages have. All code at **indentation 0** will be executed.
* **if \_\_name\_\_ == “\_\_main\_\_”:** is a way to **emulate** **main()**.

---

<a name="10"></a>
## Section 10: Errors and Exceptions Handling

#### Lesson 80. Errors and Exception Handling

> Examples of **exception handling** are in the accompanying Jupyter notebook **section-7.ipynb**

* [**Error handling**](https://docs.python.org/3/tutorial/errors.html) is used to attempt to plan for possible errors.

* There are **three keywords** for this:
	
	Keyword|Action
	---|---
	[**try**](https://docs.python.org/3/reference/compound_stmts.html#except)|block of code to be attempted (may lead to an error).
	[**except**](https://docs.python.org/3/reference/compound_stmts.html#except)|block of code to execute if there is an error in the **try** block.
	**else**|a block of code to execute if there is no error.
	[**finally**](https://docs.python.org/3/reference/compound_stmts.html#finally)|a final block of code to execute regardless of an error.
	
* A simple example of a **try/except/else** looks like,

		try:
			result = 10 + “10”
		except:
			print(“you are trying to add an integer type and a string type”)
		else:
			print(result)
			
		---
		Output:
		
		--> you are trying to add an integer type and a string type
		
		---
		Changing “10” to 10 returns
		
		--> 20

* A complete list of **built-in exceptions** can be reviewed int the [**Python docs**](https://docs.python.org/3/library/exceptions.html)

* Handlers can have as many **exceptions** as needed to handle multiple errors, e.g.

		try:
			# block of code
			
		except TypeError:
			print(“There is a TypeError”)
		
		except OSError:
			print(“There is an OSError”)
		
		...
		 
	
---
#### Takeaways

* **Best practice** is to specifically define the exception the **except** will handle. Generic handlers make it more challenging to debug.

---

#### Lessons 81 and 82. Errors and Exceptions Homework

* Course [solutions](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/07-Errors%20and%20Exception%20Handling/03-Errors%20and%20Exceptions%20Homework%20-%20Solution.ipynb) for review as needed.

#### Lessons 83 and 84. Pylint Overview

* **Unit Tests** are a critical function of creating quality code. Unit tests provide a way to automatically re-run and validate code changes.

* There are several testing tools available to accomplish **unit Testing**. We are focusing on,

	* [**pylint**](https://pylint.pycqa.org/en/latest/): a library that provides **static code analysis**
	* [**unittest**](https://docs.python.org/3/library/unittest.html): a built-in library that provides a **unit test framework** for unit testing.

> This lecture includes creating files from an editor. I personally use [**vscode**](https://code.visualstudio.com/).

* To install **pylint**, is not already installed, execute the following from a commandline,

		pip3 install pylint
		
* Create a file in the **section-10** directory that looks like,

		# This file intentionally creates an error condition.
		
		a = 1
		b = 2
		
		print(a)
		
		print(B)
		
* Execute the following command from the commandline in the **section-10** directory,

		pylint simple1.py

* This returns a report of the quality of the code in **simple1.py**

		************* Module simple1
		simple1.py:9:0: C0304: Final newline missing (missing-final-newline)
		simple1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
		simple1.py:4:0: C0103: Constant name “a” doesn’t conform to UPPER_CASE naming style (invalid-name)
		simple1.py:5:0: C0103: Constant name “b” doesn’t conform to UPPER_CASE naming style (invalid-name)
		simple1.py:9:6: E0602: Undefined variable ‘B’ (undefined-variable)
				
		-----------------------------------
		Your code has been rated at 0.00/10

* To get a more verbose report, execute,

		pylint simple1.py -r y
		
 > The results of this can be reviewed in the accompanying file **simple1\_code\_analysis\_report.txt**
 
* Now, clean the script up based on the results in the report.

	1. Create a file **simple1\_clean.py** in the **section-10** directory
	2. Edit the file in an editor, and clean it up based on what the report calls out.
	
		> The accompanying file **simple1\_clean.py** can be copied from [**Sund0g’s repo**](https://github.com/sund0g/python-bootcamp/tree/master/section-10)
	3. execute,

			pylint simple1_clean.py -r y
	4. Review the results, they should now be much closer to 10.0

	
---
#### Takeaways

* **pylint** is very useful when submitting code to a public repo. It gives the code review committee a clear view of the quality of the code.

* Study this as this is a favorite **interview question**.

---

#### Lesson 85. Running tests with the Unittest Library

* A [**Unit Test Framework**](https://www.oreilly.com/library/view/unit-test-frameworks/0596006896/ch01.html) provides a way to,

	* create a **test program** that accepts **test input**
	* execute **tests** from the **test program** using the **test input**
	* analyze the results of the **test run**
	* compare the results and report on deviations from expected results


> This lecture includes creating files from an editor. I personally use [**vscode**](https://code.visualstudio.com/).

* To demonstrate a simple unit test framework, we will do the following,

	1. Create the file **cap.py** This file will capitalize text.
	2. Create the file **test_cap.py** This is the test file.
	
	 > The accompanying files **cap.py** and **test_cap.py** can be copied from [**Sund0g’s repo**](https://github.com/sund0g/python-bootcamp/tree/master/section-10)
	3. Execute the following from the command line in the **section-10** directory,

			python3 ./test_cap.py
			
	4. The unittest report should look something like the following,

			----------------------------------------------------------------------
			Ran 2 tests in 0.003s
			
			FAILED (errors=2)
			➜  section-10 git:(section-10) ✗ python3 ./test_cap.py
			..
			----------------------------------------------------------------------
			Ran 2 tests in 0.000s

---
#### Takeaways

* Writing **unit tests** should start out **simple** and progress to **complex**
* Review the [**assertEqual**](https://www.geeksforgeeks.org/python-unittest-assertequal-function/) method to better understand the **comparison** part of the unit test framework. 

---

<a name="11"></a>
## Section 11: Milestone Project - 2

#### Lesson 86. Introduction to Milestone Project 2 Section Warmup

* As a warm-up exercise, recreate the card game, [**war**](https://en.wikipedia.org/wiki/War_(card_game))

* To construct the game the following **classes** will be created,

	* **Card**
	* **Deck**
	* **Player**
	* **GameLogic**

* The players will be virtual players.

---
#### Takeaways

* **Classes** can be connected to other classes, not singularly via **inheritance**.

---

#### Lesson 87. Card Class

* The **Card** class has three properties,
	* **Suit**: Spade, Heart, Club, Diamond
	* **Rank**: 2-Ace
	* **Value**: Integer value that corresponds to the Rank.

> The **Card** class can be reviewed in the accompanying Jupyter notebook, **section-11.ipynb**

#### Lesson 88. Deck Class

* The **Deck** class does the following,
	* **Create** a new deck
		* Creates all 52 cards
		* Holds the list of the cards

			> This will be a **list of objects**
		
	* **Shuffle** a deck
		* via the **random** **shuffle()** method
	* **Deal** cards from the deck
		* **pop** method to “remove” the cards from the deck as they are dealt

> The **Deck** class can be reviewed in the accompanying Jupyter notebook, **section-11.ipynb**

---
#### Takeaways

* **-1** will get the **last item** in an **iterable**.
* **random.shuffle()** is an **in-place** method, meaning it operates on the original iterable and doesn’t return a new iterable.
* [**pop()**](https://docs.python.org/3/tutorial/datastructures.html#data-structures) called without a parameter, returns the **last item (-1)** in the iterable.

---

#### Lesson 89. Player Class

* The **Player** class does the following,
	* **Holds** the player’s cards, (in a list)
	* **Removes** cards from the player’s “hand” (list of card objects)

* The Class should be able to add and take away multiple cards from their hand.

* The game should understand the concept of **top** and **bottom** of a deck, e.g.

	* Cards will be removed from the **top** of the deck
	* Cards will be added to the **bottom** of the deck.

> The **Player** class can be reviewed in the accompanying Jupyter notebook, **section-11.ipynb**

* Python **lists** go from **left to right**. **Top** = **left** and **bottom** = **right**

	* **pop(0)** will be used to draw from the **top** or **left** of the deck.
	* **append(card)** will be used to add to the **bottom** or **right** of the deck.
	* [**extend()**](https://docs.python.org/3/tutorial/datastructures.html#data-structures) will add **multiple** cards to the **bottom** or **right** of the deck, during a **war**.
		> **append()** cannot be used for multiple cards, because it will append the cards as a **single list** instead of **merging** the two lists.

	> Explore how to do this in a **single** method.

---
#### Takeaways

* **append()** and **extend()** work very differently, e.g.

	* append() **adds**
	* extend() **merges**

			# append() example
			
			list1 = [1, 2, 3]
			list2 = [4, 5, 6]
			
			list1.append(list2) # results in
			
			“[1, 2, 3, [4, 5, 6]]” # nested list
			
			# whereas extend() example does,
			
			list1.extend(list2) # results in 
			
			“[1, 2, 3, 4, 5, 6]” # merged list
			

---

#### Lessons 90, 91, and 92. Game Logic - Parts One, Two, and Three

* In a real-world scenario, the logic and the class structures are developed simultaneously.

> The **game logic** can be reviewed in the accompanying Jupyter notebook, **section-11.ipynb**

* There are three hand scenarios the game logic has to check for,
	* player1’s card < player2’s card
	* player1’s card > player2’s card
	* player1’s card == player2’s card

---
#### Takeaways

* It’s often useful to **visualize** the **game logic** to make the coding easier.

---

#### Lesson 93. - Milestone Project 2

* This OOP project creates a simulated [**Blackjack**](https://en.wikipedia.org/wiki/Blackjack) game.

* This version of the game,
	*  will only have the **computer** as the **dealer** and **one human player**. 
	*  It will ignore actions like **insurance**, **split**, and **double down**. 
	*  The only actions will be **hit** and **stay**.
	*  **Face cards** have a value of **10**.
	*  **Aces** have a value of either **1** or **11** at the choice of the player.

* Combining the logic with the gameplay yields something like,

	* Dealer
	* Player aka card hands
	* Deck
	* Bets
	* Chips

> The **game** can be reviewed in the accompanying Jupyter notebook, **milestone-project-2.ipynb**

* The instructor’s solutions can be reviewed [here](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/03-Milestone%20Project%202%20-%20Complete%20Walkthrough%20Solution.ipynb) on gitHub.

---
#### Takeaways

* The instructor uses [**truthy**](https://www.geeksforgeeks.org/truthy-vs-falsy-values-in-python/) in the **adjust\_for\_aces()** method. This may require a little less memory to process, but I generally don’t use this convention as it can cause confusion for others reading the code.

* You can use the **print(0)** to print all items in an iterable, e.g.

		items = [1, 2, 3]

		# Using a traditional for loop
		
		for item in items:
		    print(f”{item}”)
		    
		# Using the iterator ‘*’ This is very common in Python
		print(“Items: “, *items, sep=“\n”)
		
---

<a name="12"></a>
## Section 12: Python Decorators

#### Lesson 98. Decorators with Python Overview

> All examples are in the accompanying Jupyter notebook **section-12.ipynb**

* **Decorator syntax**: `@decorator` e.g.

		@new_decorator
		def func_needs_decorator():
			print(“I want to be decorated!!”)

* [**Decorators**](https://www.geeksforgeeks.org/decorators-in-python/) provide a way to extend an existing function without permanently modifying it, i.e. the modifications can easily be reverted.

* **Decorators** are widely used in web development with tools like [**Django**](https://www.djangoproject.com/) and [**Flask**](https://flask.palletsprojects.com/).

* **Functions** are **objects** that can be,

	* **assigned to variables** and subsequently be executed from those variables
	* be **returned** from other functions
	* be **passed** as arguments to other functions

---
#### Takeaways

* Think of a **Decorator** as an **on/off switch** that we can use to execute extra code when we want to or not.

* The **assertion** that **Decorators** are **slow** is **misleading**. Decorators by themselves do not create performance impacts. **The decorating code will obviously take longer than the wrapped function**.

* There are many debates about **decorating** versus **sub-classing**. every scenario requires **design thinking** to determine which is more appropriate.

* **Calling** a variable assigned to a function is different than **printing** it, e.g.

		# refer to the hello()/greet()/wlecome() example in the Jupyter notebook
		# for the function details and logic.
		
		--> my_new_func()
		
		# returns
		--> '\tThis is the greet() inside hello()!'
		
		---
		
		--> print(my_new_func())
		
		# returns NOTE the formatting is executed
		--> 	This is the greet() inside hello()
		
* Functions **called from other functions** or **passed in as arguments** should **return something**. Else odd behavior can happen, e.g.

		# function passed in as an argument
		
		def hello():
			print(“Hi!”)
			
		# Calling function
		
		def other(a_func):
			print(a_func)
			
		---
		
		--> other(hello)
		
		# returns
		
		Hi!
		None     # This tells us hello doesn’t return anything.
		
		# The fix
		
		def hello():
			return “Hi!”		

---

#### Lesson 99. Decorators Homework (Optional)

* Review the [**instructor’s homework**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/10-Python%20Decorators/02-Decorators%20Homework.ipynb) on [**Django**](https://www.djangoproject.com/) and [**Flask**](https://flask.palletsprojects.com/) to understand more about how to develop **full stack** web development.

* Websites such as **pinterest** and **reddis** are developed in Python.

---

<a name="13"></a>
## Section 13: Python Generators

> All examples are in the accompanying Jupyter notebook **section-13.ipynb**

#### Lesson 100. Generators with Python

* [**Generator functions**](https://www.geeksforgeeks.org/generators-in-python/) basically provides a method to return a value and subsequently resume where the function returned the value.

* **Generators** provide a way to generate a **sequence** of **values** over **time**.

* The primary difference is the syntax `yield` instead of `return`.

* When generators are **compiled**, they become an **object** that supports an **iteration** protocol and,

	* They do not return a value and exit.
	* They automatically suspend and resume their execution state around the last point of value generation.
	* The **advantage** is instead of having to compute the entire value series up front, they compute a value and wait until the next value is called for.

* The [**range()**](https://docs.python.org/3/library/stdtypes.html#typesseq-range) function works this way. It simply keeps track of the **last** number, and the step size to provide a **flow** of numbers.

	> **loop** objects **for** and **while** are **generators**

* If the **entire** sequence of values is **required up front**, the generator will have to be **transformed** into a **list**, e.g.,

		my_full_list = list(range(0,10))

* **Generator** functions can be used with,

	* [**next()**](https://docs.python.org/3/library/functions.html#next) returns the next value in the series
	* [**iter**](https://docs.python.org/3/library/functions.html#iter) iterates through any **object**

		> **next()** will not work on all objects, e.g. **strings**. Strings are **iterables**, but are not directly **iterators**.
		
* A couple of reasonable generator explanations from **StackOverflow**,

	* [Understanding generators in Python](https://stackoverflow.com/questions/1756096/understanding-generators-in-python)
	* [What does the "yield" keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

---
#### Takeaways

* **Generator** functions generally require less memory to hold a sequence. Unless the **entire list** is **needed**, **general practice** is to use a **generator** function and use it to **iterate** through the **sequence**.

* This is a great example to demonstrate timings and **efficiency** of code.

* **next()** and **iter()** are not commonly used, (they are used in the background). The main takeaway here is how to great **generator functions** with **yield** to make **large sequences memory efficient**.

---

#### Lessons 100 and 101. Generators Homework

* The instructor’s solutions can be reviewed [here](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/11-Python%20Generators/03-Iterators%20and%20Generators%20Homework%20-%20Solution.ipynb) on gitHub.

* **Interview Question**

	* Review my solution for the **list comprehension** (Extra Credit) in  [**section-13.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-13/section-13.ipynb). Basically, use **()s** instead of **[]s** to generate the sequence on the fly instead of putting the values in a list, e.g.,
	
			my_list = [1, 3, 5, 9, 2, 6]
	
			# Creates a list to iterate through
			gencomp = [item for item in my_list if item > 3]
			
			---
			
			# Turns the list comprehension into a list generator
			gencomp = (item for item in my_list if item > 3)
	
		> Here’s a [great explanation](https://stackoverflow.com/questions/364802/how-exactly-does-a-generator-comprehension-work) on **StackOverflow**.

---

<a name="14"></a>
## Section 14: Advanced Python Modules

#### Lesson 103. Intro to Advanced Python Modules

* There are many complex Python modules and packages that are useful in everyday development and engineering.

* **Modules** covered in this section,

	* [**collections**](https://docs.python.org/3/library/collections.html)
	* [**os**](https://docs.python.org/3/library/os.html#module-os)
	* [**shutil**](https://docs.python.org/3/library/shutil.html)
	* [**datetime**](https://docs.python.org/3/library/datetime.html#module-datetime)
	* [**math**](https://docs.python.org/3/library/math.html) and [**random**](https://docs.python.org/3/library/random.html)
	* [**Python Debugger**](https://docs.python.org/3/library/pdb.html)
	* [**re**](https://docs.python.org/3/library/re.html) (regular expressions)
	* [**timeit**](https://docs.python.org/3/library/timeit.html)

	* **Unzipping** and **Zipping Modules**

---

#### Lesson 104. Python Collections Module

> All examples are in the accompanying Jupyter notebook [**section-14-collections-module.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-collections-module.ipynb)

*  The [**collections**](https://docs.python.org/3/library/collections.html) **built-in** module implements specialized **container** types that are alternatives to Python’s general purpose container types, e.g. **list**, **dictionary**, **tuple**, etc.

* Very useful [**collections**](https://www.geeksforgeeks.org/python-collections-module/) methods are,

--
* [**Counter**](https://www.geeksforgeeks.org/python-collections-module/#counters): Returns an **unordered dictionary** of **elements** and their **number of instances** in an **iterable**

	* Some common **patterns** when using **Counter**

		Object|Description
		---|---
		sum(c.values())|total of all counts
		c.clear()|reset all counts
		list(c)|list unique elements
		set(c)|convert to a set
		dict(c)|convert to a regular dictionary
		c.items()|convert to a list of (elem, cnt) pairs
		Counter(dict(list_of_pairs))|convert from a list of (elem, cnt) pairs
		c.most_common()[:-n-1:-1]|n least common elements
		c += Counter()|remove zero and negative counts

--
			
* [**defaultdict**](https://www.geeksforgeeks.org/defaultdict-in-python/): Assigns a **default value** in a scenario where a [**keyError**](https://docs.python.org/3/library/exceptions.html#KeyError) occurs.

	* The **default value** is usually assigned via a **lambda function**, e.g.,
	
			my_defaultdict = defaultdict(lambda: 0) # The lambda could be more complex, if needed.

--

* [**namedtuple**](https://www.geeksforgeeks.org/namedtuple-in-python/): Adds a **key** that is **hashed** to a particular **value** in a tuple.

	> This is useful when there is a tuple that has many elements.
	
	> **namedtuples** behave similarly to **classes**, i.e. using the ‘.’ object syntax
	
* Syntax when declaring a namedtupled is `my_named_tuple = namedtuple(typename, fieldnames)` e.g.,

		dog = namedtuple('Dog', ['age', 'breed', 'name’])

---

#### Lesson 105. Opening and Reading Files and Folders (Python OS Module)

> All examples are in the accompanying Jupyter notebook [**section-14-opening-reading-files-folders.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-opening-reading-files-folders.ipynb)

* This lesson teaches how perform actions on files such as,

	* Open every file in a directory
	* Move files around on the computer

* The [**os**](https://www.geeksforgeeks.org/os-module-python-examples/) **standard utility** module provides methods for interacting with with an **operating system**.

	> The os package should work across operating systems.
	
	* Some common **methods** when using **os**

		Object|Description
		---|---
		[getcwd](https://docs.python.org/3/library/os.html)|get the current working directory
		[listdir()](https://www.geeksforgeeks.org/python-os-listdir-method/)|list a directory. Can take a directory as a parameter


* **Moving files** around the **filesystem** is done with the [**shutil**](https://www.geeksforgeeks.org/shutil-module-in-python/) **standard utility** package.

	* Some common **methods** when using **os** and **shutil**

		Object|Description
		---|---
		shutil.[move](https://www.geeksforgeeks.org/python-shutil-move-method/)|Moves a file from srcdir to destdir
		os.[path](https://docs.python.org/3/library/os.path.html)|Contains useful methods for file/directory tasks.
		os.[remove](https://docs.python.org/3/library/os.html#os.remove)| Removes a file.
		os.[walk](https://www.geeksforgeeks.org/os-walk-python/)| Traverses a directory path returning a **3-tuple (dirpath, dirnames, filenames**)
		
* A note on **deleting files**. The **os** and **shutil** modules provide **3 methods** for deleting files:

	Object|Description
	---|---
	os.unlink(path/file)|Deletes the **file** at **path**
	os.rmdir(path/folder)|Deletes a **folder** (folder must be empty) at path
	shutil.rmtree(path)|Removes **all files and folders** contained in the path
			
	> These methods are **irreversible** and are generally not recommended


* A safer way to remove files and directories is via the [**send2trash**](https://pypi.org/project/Send2Trash/) **external** module. send2trash sends **deleted** files to the **trash/recycle bin** instead of permanent removal.

	* To install this package, execute, 

			pip install send2trash
			
	* More information about send2trash can be reviewed [**here**](https://www.geeksforgeeks.org/how-to-delete-files-in-python-using-send2trash-module/)

* Make sure to review the **os.walk** example in the Jupyter notebook [**section-14-opening-reading-files-folders.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-opening-reading-files-folders.ipynb)

---
#### Takeaways

* Use [**with**](https://www.geeksforgeeks.org/with-statement-in-python/) logic when manipulating **files** as this provides **built-in error handling**, and is easier to read.

* **os.path.expanduser(‘~’)** is an easy way to get the User’s home directory.

---

#### Lesson 106. Python Datetime Module

> All examples are in the accompanying Jupyter notebook [**section-14-datetime-module.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-datetime-module.ipynb)

* The [**datetime**](https://www.geeksforgeeks.org/python-datetime-module/) module provides methods and objects for dealing with **relational time**.

---
#### Takeaways

* **datetime** assumes **24h** time.

* **datetime** does **not combine** the data and time in the **base object**. Use the **datetime** subclass for this, e.g.,

		from datetime import datetime
		
* Datetime **arithmetic** is a very common **use case**.

---

#### Lesson 107. Python Math and Random Modules

> All examples are in the accompanying Jupyter notebook [**section-14-math-and-random-module.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-math-and-random-module.ipynb)

* The **math** module contains most of the commonly used arithmetic functions. These functions can be reviewed by executing,

		--> help(math)

* Some common **methods** when using **random**

	Object|Description
	---|---
	[random.choice()](https://www.geeksforgeeks.org/python-numbers-choice-function/)|Returns a random item from a **list**, **tuple**, or **string**
	[random.choices(population=\<list | tuple | string, k=\<sample size>)](https://www.geeksforgeeks.org/random-choices-method-in-python/)|Returns a random sample that may contain duplicates
	[random.sample(population=\<list | tuple | string\, k=\<sample size>)](https://www.geeksforgeeks.org/python-random-sample-function/)|Returns a random sample that does NOT contain duplicates
	[random.shuffle(sequence)](https://www.geeksforgeeks.org/random-shuffle-function-in-python/)|**in-place** shuffles the sequence.	 

	> When using a [**random seed**](https://en.wikipedia.org/wiki/Random_seed) in a **Jupyter notebook**, the **seed** and **dependent operations** may need to be in the **same cell**.
	
	> Think of this as the **seed** setting the **sequence** for **infinite random numbers**.

---
#### Takeaways

* **help(<modulename>)** provides **documentation** on the module. (Think of the old school **man pages**).

* The [**round**]() built-in method follows the [**even/odd** rounding rule](https://github.com/sund0g/python-bootcamp/blob/master/section-14/rounding-rule.md)

* **Complex** mathematical operations may be best solved with the [**numpy**](https://numpy.org/) package.

---

#### Lesson 108. Python Debugger

> All examples are in the accompanying Jupyter notebook [**section-14-python-debugger.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-python-debugger.ipynb)

* The [**pdb**](https://www.geeksforgeeks.org/python-debugger-python-pdb/) package is the **built-in** Python debugger.

* `pdb.set_trace()` basically acts as a **breakpoint** instead of having to use **print()** statements to debug.

> To quit the interactive session, enter **q** in the dialog box.

---

#### Lessons 109, 110 and 111. Python Regular Expressions

> All examples are in the accompanying Jupyter notebook [**section-14-regular-expressions.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-regular-expressions.ipynb)

* The [**re**](https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/) **built-in** package provides methods for creating specialized search patterns, and search for those patterns in text.

* Some common **methods** when using **re**

	Object|Description
	---|---
	[.search()](https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/)|Returns a **match object** of the **first matched string**
	[.span()](https://www.geeksforgeeks.org/re-matchobject-span-method-in-python-regex/#:~:text=span()%20method%20returns%20a,(%2D1%2C%2D1).&text=Parameters%3A%20group%20(optional)%20By%20default%20this%20is%200.)|Returns a **tuple** containing **starting and ending index** of the **first matched string**
	[.group()](https://docs.python.org/3/library/re.html#re.Match.group)|Returns one or more **subgroups** of the **match**
	[.findall()](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)|Returns a **list** of **all matched strings**
	[.finditer()](https://docs.python.org/3/library/re.html#re.finditer)|Returns an **iterator** yielding **match objects** over **all non-overlapping matches**
	[.compile()](https://docs.python.org/3/library/re.html#re.compile)|Compiles together regex pattern codes. This is very powerful when combined with **.group()**

* **regex character identifiers** are as follows,

	Character|Description|Example Pattern Code|Example Match
	---|---|---|---
	\d|a digit|file_\d\d|file_25
	\w|alphanumeric|\w-\w\w\w|A-b_1
	\s|white space|a\sb\sc|a b c
	\D|non-digit|\D\D\D|ABC
	\W|non-alphanumeric|\W\W\W\W\W|*-+=)
	\S|non-white space|\S\S\S\S|Yoyo
	
* **regex quantifiers** are as follows,

	Character|Description|Example Pattern Code|Example Match
	---|---|---|---
	+|occurs more than once|Version \w-\w+|Version A-b1_1
	{3}|occurs exactly 3 times|\D{3}|abc
	{2,4}|occurs 2 to 4 times|\d{2,4}|123
	{3,}|occurs 3 or more times|\w{3,}|anycharacters
	*|occurs 0 or more times|A\*B\*C\*|AAACC
	?|once or none|plurals?|plural

* **regex syntax**: `r”some pattern`, e.g. `r”\d{3}-\d{3}-\d{4}”`

* **regex pattern codes syntax**: `r()-()-()`, e.g. `r(\d{3})-(\d{3})-(\d{4})`

	> Pattern subgroups are an efficient way of extracting groups of pattern data.

* **Additional regex syntax**

	* Refer to the [**intro to regex**](https://docs.python.org/3/howto/regex.html) and [**full list**](https://docs.python.org/3/library/re.html#regular-expression-syntax) of syntax for additional details.

	> The lesson reviews the **OR |**, **character wildcard .**, **starts/ends with ^$**, **set []** syntax.

---
#### Takeaways

* Regular expressions are notoriously difficult to remember. Rather than trying to memorize them, focus on understanding how to look up the data, and then find the associated regex pattern e.g.,

		phone number: (xxx)-xxx-xxxx
	
		regex: r”(\d\d\d)-\d\d\d-\d\d\d\d” or r”(\d{3})-\d{3}-d{4}”
		
* **Pattern group indexes** start at **1** instead of **0**.

---

#### Lesson 112. Timing Your Python Code

> All examples are in the accompanying Jupyter notebook [**section-14-timing-code.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-timing-code.ipynb.ipynb)

* There are at least **three** ways to time the **efficiency** of code

	1. Track the time elapsed from beginning to end of the code execution.
		* This method is acceptable for small amounts of code.
		* It may not provide granular enough timings to prove the code efficiency.
	
	2. Use [**timeit**](https://www.geeksforgeeks.org/timeit-python-examples/)
		* This **built-in** module is more complex, but it runs code repeatedly to get more granular timings.
		* The syntax is

				timeit(setup, statement, test_repetitions)
				
			> **setup** and **statement** are string inputs. Refer to [**section-14-timing-code.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-timing-code.ipynb.ipynb) for examples how to do this with multi-line strings ‘’’’’’
	
	3. [**%%timeit**](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) for Jupyter notebooks only.

		> The **default** number of **test** iterations is **100000**

---
#### Takeaways

* It is good practice to understand the efficiency of code. Code that executes fine at a small scale may perform poorly at a large scale.

* Timings are are great additions to unit tests.

---

#### Lesson 113. Zipping and Unzipping Files with Python

> All examples are in the accompanying Jupyter notebook [**section-14-zipping-and-unzipping-files.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-zipping-and-unzipping-files.ipynb)

* To programmatically compress files, use the [**zipfile**](https://docs.python.org/3/library/zipfile.html) package.

* Example syntax to create an empty zipfile is,

		compressed_file = zipfile.Zipfile(“compressed_file.zip”, “w”)
		
	> Note: the method **ZipFile()** is **camelcase**.
	
* Example syntax to add a file to a zipfile,

		compressed_file.write(“my_file.txt”, compress_type=zipfile.ZIP_DEFLATED)
		
	> **zipfile.ZIP_DEFLATED** is generally the **standard** compression type.
	
* Example syntax to extract files,

		zip_object = zipfile.ZipFile("compressed_file1.zip", "r")
		
		# Extract a single file
		zip_object.extract(“one_file.txt”, “extracted_files”)
		
		# Extract all files
		zip_object.extractall("extracted_files")
	
* To programmatically **zip** and **unzip** entire **directories**, use the [**shutil**](https://docs.python.org/3/library/shutil.html) package.

---
#### Takeaways

* Refer to additional examples of [**zipfile**](https://www.geeksforgeeks.org/working-zip-files-python/) and [**shutil**](https://www.geeksforgeeks.org/shutil-module-in-python/).
* [**shutil**](https://www.geeksforgeeks.org/shutil-module-in-python/) will probably be the **most used** of the two methods here.

---

#### Lessons 114 and 115. Advanced Python Module Puzzle

> All examples are in the accompanying Jupyter notebook [**section-14-advanced-python-module-exercise.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-14/section-14-advanced-python-module-exercise.ipynb)

---
#### Takeaways

* This puzzle shows how to travers and search directories using [**os.walk()**](https://www.geeksforgeeks.org/os-walk-python/) There are more efficient ways to do this, if you are motivated to research this.

---

<a name="15"></a>
## Section 15: Web Scraping with Python

#### Lesson 116. Introduction to Web Scraping

* **Web scraping** is a general term for techniques involving automating the gathering of data from a website.

* To understand web scraping, it is necessary to understand how a website works, i.e.
	* when a browser **loads** a website, the user sees what is known as the **front-end** of the website. Most modern websites use a combination of **html**, **css**, and **javascript** to manage the front-end.

* There are **three** things that must be understood to effectively web scrape
	1. **Rules** of **web scraping**
	2. **Limitations** of **web scraping**
	3. Basic **html** and **css**

* **Rules** for web scraping
	* Always try to get permission before scraping.
	* Too many attempts to scrap can result in your IP address being blocked from the website.
	* Some sites automatically block scraping software.

* **Limitations** of web scraping
	* Generally every website is unique, so every web scraping script will be unique.
	* Any change to a website may break a scraping script.

* **html** is used to create the basic structure of a web page

* **css** is used for the design and style of a web page, i.e. where elements are placed and how the page looks.

* **javascript** is used to define the interactive elements of the page.

* The following packages will need to be installed for the lessons in this section,

		pip3 install requests
		pip3 install lxml
		pip3 install bs4
		
	> For **Anaconda** distributions, use `conda install` instead of `pip3 install`

---

#### Lesson 117. Setting Up Web Scraping Libraries

> I install the **requests**, **lxml**, and **bs4** packages manually for this section because I generally do not web scrape. I will manually uninstall these packages at the end of the section.

> It is also recommended to use the **Chrome** browser to be able to follow along with the lessons.

* Install the packages from a command prompt as follows,

		pip3 install requests lxml bs4
				
---

#### Lesson 118. Python Web Scraping - Grabbing a Title

> All examples are in the accompanying Jupyter notebook [**section-15-python-web-scraping-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-15/section-15-python-web-scraping-lessons.ipynb)

---
#### Takeaways

* The **.getText()** method returns the **innerText** of an **element**, that is the text which is visible on the page along with its sub-elements. Inner text is the text that is between the opening and closing tags. .getText() ignores all the leading and trailing spaces.

---

#### Lesson 119. Python Web Scraping - Grabbing a Class

> All examples are in the accompanying Jupyter notebook [**section-15-python-web-scraping-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-15/section-15-python-web-scraping-lessons.ipynb)

* Some example syntax for **soup.select()**

	Syntax|Match Results
	---|---
	`soup.select(‘div’)`|All elements with the `<div>` tag
	`soup.select(‘#some_id’)`|The HTML element containing the `id` attribute of some_id
	`soup.select(‘.notice’)`|All the HTML elements with the CSS `class` named `notice`
	`soup.select(‘div span’)`|Any elements named `span` that are within an element named `div` 
	`soup.select(‘div > span’)`|Any elements named `span` that are *directly* within an element named `<div>`, with no other element in between
	
---

#### Lesson 120. Python Web Scraping - Grabbing an Image

> All examples are in the accompanying Jupyter notebook [**section-15-python-web-scraping-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-15/section-15-python-web-scraping-lessons.ipynb)

> Always check copyright permission **before** downloading and using an image from someone else’s website.

---

#### Lessons 121 & 122. Python Web Scraping - Book Examples Parts One and Two

> All examples are in the accompanying Jupyter notebook [**section-15-python-web-scraping-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-15/section-15-python-web-scraping-lessons.ipynb) 

---

#### Lessons 123 & 124. Python Web Scraping - Exercise

> All examples are in the accompanying Jupyter notebook [**section-15-python-web-scraping-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-15/section-15-python-web-scraping-lessons.ipynb) 

* At this point, you may want to uninstall the web scraping packages installed at the beginning of this section,

		pip3 uninstall requests lxml bs4

---

<a name="16"></a>
## Section 16: Working with images in Python

> All examples are in the accompanying Jupyter notebook [**section-16-working-with-images-lessons.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-16/section-16-working-with-images-lessons.ipynb) 

#### Lessons 125 & 126. Introduction to and Working with Images with Python

* In this section we will use the [**pillow**](https://python-pillow.org/) package to interact with image files. 

> I install the **pillow** package manually for this section because I generally do not interact with images. I will manually uninstall it at the end of the section.

> It is also recommended to use the **Chrome** browser to be able to follow along with the lessons.

* Install the packages from a command prompt as follows,

		pip3 install pillow
		
* We will need some **images** to work with in this section, so **download** all the **.png** files from the [**Instructor’s course**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/14-Working-with-Images).

---

#### Lessons 127 & 128. Image Exercises

> All exercises are in the accompanying Jupyter notebook [**section-16-working-with-images-exercises**](https://github.com/sund0g/python-bootcamp/blob/master/section-16/section-16-working-with-images-exercises)

---

<a name="17"></a>
## Section 17: Working with PDFs and Spreadsheet CSV Files

#### Lesson 129. Introduction to PDFs and Spreadsheets with Python

* We will need some **pdf** and **csv** files to work with in this section, so **download** all the **.pdf** and **.csv** files from the [**Instructor’s course**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/15-PDFs-and-Spreadsheets).

---

#### Lesson 130. Working with CSV Files in Python

> All examples are in the accompanying Jupyter notebook [**section-17-working-with-csv-files.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-17/section-17-working-with-csv-files.ipynb)

* Refer to the [**Wikipedia article**](https://en.wikipedia.org/wiki/Comma-separated_values) for an explanation on .csv files.

* This lesson will use the **built-in** package [**csv**](https://docs.python.org/3/library/csv.html).

* Other packages that are very useful are,

	* pandas [**official site**](https://pandas.pydata.org/) & [**GeeksforGeeks**](https://www.geeksforgeeks.org/introduction-to-pandas-in-python/). This is a common and useful tool for **Data Science** tasks.
	* openpyxsl [**official site**](https://openpyxl.readthedocs.io/en/stable/) & [**GeeksforGeeks**](https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/). This module is designed specifically for **Excel** files.
	* Google Sheets API [**official site**](https://developers.google.com/sheets/api/quickstart/python) & [**GeeksforGeeks**](https://www.geeksforgeeks.org/how-to-automate-google-sheets-with-python/). This **API** is designed specifically for **Google Sheets**.

* The **common factor** between these, (and other) packages is that they all **export** to **.csv**.

* **Reading** and **writing** to **csv** files use the **objects**,

	Object|Description
	---|---
	[**csv.reader()**](https://docs.python.org/3/library/csv.html#csv.reader)|Reads data from a .csv file
	[**csv.writer()**](https://docs.python.org/3/library/csv.html#csv.writer)| Writes data to a .csv file

---
#### Takeaways

* Most **file readers**, e.g. **csv.reader()** return **file data** as a **list of lists**.

---

#### Lesson 131. Working with PDF Files in Python

> All examples are in the accompanying Jupyter notebook [**section-17-working-with-pdf-files.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-17/section-17-working-with-pdf-files.ipynb)

* Refer to the [**Wikipedia article**](https://en.wikipedia.org/wiki/PDF) for an explanation on .pdf files.

> Many **pdf** files are **not machine readable** via Python. A **scanned pdf** is most likely **unreadable** by Python.

* This lesson will use the **open-source** package [**pypdf2**](https://pypdf2.readthedocs.io/en/latest/).

> I install the **pypdf2** package manually for this section. I will manually uninstall it at the end of the section.

* Install the package from a command prompt as follows,

		pip3 install pypdf2

---

#### Lessons 132 & 133. PDFs and Spreadsheets Python Puzzle Exercise

> My solution is in the accompanying Jupyter notebook [**section-17-pdfs-spreadsheets-puzzle.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-17/section-17-pdfs-spreadsheets-puzzle.ipynb)

* We will need some **files** to work with in this section, so **download** all the files from the [**Instructor’s course**](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/15-PDFs-and-Spreadsheets/Exercise_Files).

---

<a name="18"></a>
## Section 18: Emails with Python

#### Lesson 134. Introduction to Emails with Python

* The methods learned in this section are dependent on security and administrative settings. They may/may not work depending on how your email account and firewall settings are configured.

* This section will use the **built-in** package [**smtplib**](https://docs.python.org/3/library/smtplib.html) to set up the protocols, connections, login, and sending and receiving emails.

* Refer to the [**Wikipedia article**](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) for an explanation of **SMTP**.

* The lessons will show how to connect to a **gmail** account via **smtp.gmail.com**

* If you use gmail for your normal email, you will have to **generate** an additional **app password** for the lessons, as your usual password will not work for security reasons.

---

#### Lessons 135 & 136. Sending and Receiving Emails with Python

> All examples are in the accompanying Jupyter notebook [**section-18-sending-emails.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-18/section-18-sending-emails.ipynb)
> 
> NOTE: I did not set up the app password for this and the next lesson, as 1) I don’t want to accidentally mess up my gmail account, and 2) I don’t interact with my email programmatically.

---

<a name="19"></a>
## Section 19: Final Capstone Project

#### Lesson 137. Final Capstone Project

* The section contains a [**list of projects**](https://github.com/sund0g/python-bootcamp/blob/master/section-19/final-capstone-project-ideas.ipynb) and [**solutions**](https://github.com/sund0g/python-bootcamp/blob/master/section-19/solution-links.md) to work on as you have time.

* Study these as they contain many favorite **interview questions**.

---

<a name="20"></a>
## Section 20. Advanced Python Objects and Data Structures

#### Lesson 138. Advanced Numbers

* Python has two **built-in** modules for **mathematical** functions

	Module|Description
	---|---
	[**math**](https://docs.python.org/3/library/math.html)|Supports mathematical functions defined by the C standard
	[**cmath**](https://docs.python.org/3/library/cmath.html#module-cmath)|Supports mathematical functions for [**Complex Numbers**](https://en.wikipedia.org/wiki/Complex_number)

* Python also has some standard **built-ins** methods

	Method|Description
	---|---
	[**hex(n)**](https://www.geeksforgeeks.org/python-hex-function/)|Converts a number to Hexadecimal.
	[**bin(n)**](https://www.geeksforgeeks.org/bin-in-python/)|Converts a number to Binary.
	[**pow(x, y, [z])**](https://www.geeksforgeeks.org/pow-in-python/)|Takes 2 or 3 numbers. If 2, raises x to the power of y. If 3, raises x to the power of y and mods the result with z.
	[**abs(n)**](https://www.geeksforgeeks.org/abs-in-python/)|Returns the [**Absolute Value**](https://en.wikipedia.org/wiki/Absolute_value) of a number, (removes the ‘**-**’ if n is negative.)
	[**round(n, p)**]()|Rounds a number to the provided precision (p). Default precision is 0. Returns a **float**.
	
---

#### Lesson 139. Advanced Strings

* There are several **built-in** string methods in Python. Simple examples can be reviewed in the accompanying Jupyter notebook [**section-20-advanced-strings.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-20/section-20-advanced-strings.ipynb)

---

#### Lesson 140. Advanced Sets

* There are several **built-in** set methods in Python. Simple examples can be reviewed in the accompanying Jupyter notebook [**section-20-advanced-sets.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-20/section-20-advanced-sets.ipynb)

---
#### Takeaways

* The **set** data structure is very powerful, but often under-utilized. Keep this in mind when working with sets.

---

#### Lesson 141. Advanced Dictionaries

> Examples can be reviewed in the accompanying Jupyter notebook [**section-20-advanced-dictionaries.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-20/section-20-advanced-dictionaries.ipynb)

---

#### Lesson 142. Advanced Lists

> Examples can be reviewed in the accompanying Jupyter notebook [**section-20-advanced-lists.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-20/section-20-advanced-lists.ipynb)

---

#### Lessons 143 & 144. Advanced Python Objects Assessment Test

> The test with answers can be reviewed in the accompanying Jupyter notebook [**section-20-assessment-test.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-20/section-20-assessment-test.ipynb)

---

<a name="21"></a>
## Section 21: Introduction to GUIs

#### Lessons 145 & 146. Intro to GUIs and Jupyter Widgets

* A complete list of GUI Frameworks is maintained at [**python.org**](https://wiki.python.org/moin/GuiProgramming).

* You might want to use [**pygame**](https://www.pygame.org/hifi.html) for creating **video games**.

* If building **web apps**, it may be better to to use **html**, **css**, and **javascript** for the GUI **front-end**, and [**Flask**](https://flask.palletsprojects.com/en/2.2.x/) or [**Django**](https://www.djangoproject.com/) for **back-end** work.

*  The lessons in this section will use [**ipywidgets**](https://ipywidgets.readthedocs.io/en/latest/index.html) designed for **Jupyter Notebooks**.

	> This type of GUI is best suited for creating **dashboards** for **data/Business analysis** use-cases.

---

#### Lesson 147. Interact Functionality with GUIs

> All examples can be reviewed in the accompanying Jupyter notebook [**section-21-interact.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-21/section-21-interact.ipynb)

---

#### Lesson 148. GUI Widget Basics

> All examples can be reviewed in the accompanying Jupyter notebook [**section-21-widget-basics.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-21/section-21-widget-basics.ipynb)

---

#### Lesson 149. List of Possible Widgets

> All examples can be reviewed in the accompanying Jupyter notebook [**section-21-widget-list.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-21/section-21-widget-list.ipynb)

---

#### Lesson 150. Widget Styling and Layouts

> All examples can be reviewed in the accompanying Jupyter notebook [**section-21-widget-styling.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-21/section-21-widget-styling.ipynb)

---

#### Lesson 151. Example of what a Widget can do!

> Example can be reviewed in the accompanying Jupyter notebook [**section-21-custom-widget.ipynb**](https://github.com/sund0g/python-bootcamp/blob/master/section-21/section-21-custom-widget.ipynb)

---

