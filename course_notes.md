## Day 1: 27/03/2025

<b>Git</b> \
A version-control system that tracks changes. Github is a website where you can share files with the git version-control tracking changes online

[PyPI](https://pypi.org/): A database of all Python packages that exist

### Programming 

Files created: 
* hello.py
* number.py

I made a conda environment `wis-python` using Anaconda Prompt. You can’t name environments using VS Code or locally access the environment to install packages specifically for the environment with `$ pip install openpyxl`. So, I installed openpyxl through Anaconda Prompt.

## Day 2: 03-04-2025

To suggest changes to things online w/o needing to clone the repo locally, you can _fork_ the repository to your account, make the change, and submit a _pull request_ to incorporate the change.

exercism.org - A platform where you can download programming assignments and get feedback on your solutions.

`openpyxl` - A Python module that allows working with Excel files

### Programming

Using `input()` \
Pro VS Code tip: Pressing F2 while the cursor is on a variable pulls up a text input field which allows you to rename all instances of that variable name in the script.

Another cool thing is selecting a string of code and press any bracket or quote key which encloses that string in that kind of brackets/quotes 

## Day 3: 10-04-25

There's a notion of using number value types (`int8`, `int32`, `float32`, etc) to optimize memory usage. If you have lots of positive integers but they are all below 255, it might be better to specify and use the `int8` type.

Some syntax errors in Python are caught before the program runs, and some are caught only when the program begins running.

You can actually assign methods to variables in Python. For example,
```python
import random

rnd = random.random
print(rnd) # <built-in method random of Random object at 0x00000153D9B27DA0>
print (rnd()) # some random floating point number between 0-1
```

The `random.py` and `rnd.py` slide: \
The error came about because, when Python saw `import random`, it first looks for files named `random.py` in the same directory. When it's not there, it looks for the same in other places - namely, the correct place where the module is actually installed. 

### Programming

What Gabor does: defines a function `main()` which he uses to run the "main code". \
Standard recommendation: 4 spaces for every level (same as 1 tab space)

Q. What was the __name__ in `conditional_main.py` example? \
A. Double underscores on both sides indicate some internal variable. 

Q. I've seen code with double underscores just on the start of names - does that also designate some internal variable the user-written code uses, but keeps it separate from the Python internal variable? \
A. It is used to keep users from not messing with that particular variable, yes

The `input()` function always takes in a string

In `elif.py`, Gabor says it's not good code. It's better (more readable and easily interpretable) if you use an f-string:
```python
print(f"{a} is greater than {b}")
``` 
is better than: 
```python
print(a + " is greater than " + b)
```

#### `sys.argv`: 
This is a list made from the command line input. The first element is the 0th element, and it refers to the script itself. Then, if you supply further arguments, it takes that in the list. For example, say you have `cli.py` which prints sys.argv and its first 3 elements. So,
```python
python cli.py a b c d
```
will print 
```python
['.\\cli.py', 'a', 'b', 'c']
.\cli.py
a
b
```
If my input instead only gave 1 entry like 
```python 
python cli.py a
```
it will throw an error

## Day 4: 08-05-25

For comparing strings (e.g. ```if "Snake" < "Stake":```), Python compares the Unicodes of the characters of the same index. So here, "S" with "S", then "n" with "t"; here, the Unicode for "n" is smaller than that of "t", so the statement is `True`.

Good example for this:
```python
print(2 < 11)		# True
print("2" < "11")	# False
```
You can chain `if age > 0 and age <= 18:` into `if 0 < age <= 18:`

<u>Flag</u>: You press a "top" button, and it has one value. You push the "bottom' button, and it now has another value.
<u>Toggle</u>: Value switches on the same button
Example of a toggle statement is:
```python
machine_is_on = True
if(machine_is_on):
	<do something>
	...
	machine_is_on = not machine_is_on # the toggle statement
else:
	<do something else>
	...
	machine_is_on = not machine_is_on # toggle statement again
```
<u>Idea of a short circuit</u>: Say you have `if A or B:`. In some languages, B is checked ONLY when A is `False`. Because, in an OR statement, if the first condition is `True`, you don't necessarily need to check the 2nd condition because the OR will be `True` regardless. This is an issue when the 2nd condition is a check that's required and is used in the code block following the conditional statement. This can be circumvented by:
```python
def A():
	return conditionA
def B():
	return conditionB
while True:
	A_check = A()
	B_check = B()
	if A_check or B_check:
		...
```
You can feed anything to an `if`. Anything corresponding to zero or null (like `0` for numbers, `"", [], {}, None` for corresponding data types) is `False`. 
An example where this is somewhat illustrated:
```python
if status_code == 401 or 302:
```
is actually read as
```python
if (status_code == 401) or 302:
```
where `302` is taken as the 2nd condition to the `if` for the OR. And because it is a "not-empty" value, it is considered as `True`.

Multi-line strings: 
```python
text1 = "J: 23\nK: 25"
text2 = """
J: 23
K: 25
"""
```
These two encode the same multi-line string

Very cool way to have the exact number of hyphens under a title:
```python
title = "Some grandiose title"
print(title)
print('-' * len(title))
```

Taking slices does not include the end element. So, `[1:4]` will take the 2nd to the 4th element (not the 5th element which is indexed as 4). Similar idea for the `range()` function.

You can't update a string's value (i.e. you can't change some character inside them). They're <b>immutable</b>, and you need to reassign it completely.
Example:
```python
text = "abcd"
print(text)		# abcd

text = text[:2] + 'Y' + text[3:]
print(text)		# abYd
```

Functions vs methods: You feed an argument to the function, but the method acts on an argument without being fed it. 
```python
a = "xYz"
len(a)		# a function
a.upper()	# a method
```
Using the `dir()` function with a variable lists all the methods that variable can have. We can do `dir(a)` to see all the methods a string can have. As an example, Python uses the hidden method `__add__` to carry out the string concatenation operation with `+`.

`ord('火')` will give 28779
`chr(28779)` will give 火

Alternate solution for ROT13, where you can condense the code:
```python
for char in original:
	code = ord(char)
	# using letters instead of Unicode is clearer to read
	if 'a' <= char <= 'z': # small letters
		new_char = chr((code - ord('a') + 13) % 26 + ord('a'))
	elif 'A' <= char <= 'Z': # capital letters
		new_char = chr((code - ord('A') + 13) % 26 + ord('A'))
	else:
		new_char = char
	encoded += char
```
DRY: Don't Repeat Yourself. The notion is that, if you're having to write the same code more than once (twice, to be conservative), then it's not good. That's because, say you copy-paste the code in multiple places. Something comes up (there's a bug or there's a feature you or someone else wants to add/modify), and only one copy is replaced. The other instances are still unchanged which can cause issues that become headaches to debug.