# Complete Python Bootcamp
Coursework and notes from [Udemy](https://www.udemy.com/complete-python-bootcamp/)

The exercises of the course are on Github here: [https://github.com/Pierian-Data/Complete-Python-3-Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

### Table of Contents

* [Section 1: Course Overview](#1)
* [Section 2: Python setup](#2)
* [Section 3: Python Object and Data Structure Basics](#3)
* [Section 4: Python Comparison Operators](#4)
* [Section 5: Statements](#5)


* **NOTE:** there are some **interview questions** listed throughout this course. Search on **"interview"** to find them.


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
### Takeaway

* Additional resource for string formatting: https://pyformat.info/

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
#### Takeaway

* **Tuples** are very useful when passing objects that are not to be changed.

---

#### Lesson 25. Sets

* [**Sets**](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20object#sets) are **unordered** collections of objects with **unique** values.
* `set()` is the syntax to create a set, e.g. `my_set = set()`
* Examples,

		my_set = set()	creates an empty set
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

#### Takeaway
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
* 

		for num in range(0,101):
			if num%3 == 0 and num%5 == 0:
				print(‘FizzBuzz’)
			elif num%3 == 0:
				print(‘Fizz’)
			elif num%5 == 0:
				print(‘Buzz’)
			else:
				print(num)

**NOTE: make sure to check for multiples of 3 and 5 FIRST. This keeps the logic correct.**

