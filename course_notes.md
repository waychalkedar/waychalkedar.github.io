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

## Day 5: 15-05-25

From the example ``,
```python
data = [
    ["Foo Bar", 42],
    ["Bjorg", 12345],
    ["Roza", 7],
    ["Long Name Joe", 3],
    ["Joe", 12345677889],
]

for entry in data:
	print("{} {}".format(entry[0], entry[1]))

print('-' * 16)

for entry in data:
	print("{<:8}|{:>7}".format(entry[0], entry[1]))
```
this gives
```python
Foo Bar 42 
Bjorg 12345 
Roza 7 
Long Name Joe 3 
Joe 12345677889 
----------------
Foo Bar |     42 
Bjorg   |  12345 
Roza    |      7 
Long Name Joe|      3
Joe     |12345677889
```
`<:8` left aligns the string, and pads it on the right if the string is <8 characters. `:>7` pads to the left and aligns to the left. You can change these numbers if needed - you can see `Long Name Joe` gets printed in a somewhat undesirable way.

You can use slices with steps. `slice.py` is:
```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::])       # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::1])      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::2])      # ['a', 'c', 'e', 'g', 'i']

print(letters[1::2])     # ['b', 'd', 'f', 'h', 'j']

print(letters[2:8:2])    # ['c', 'e', 'g']

print(letters[1:20:3])   # ['b', 'e', 'h']

print(letters[20:30:3])  # []

print(letters[8:3:-2])   # ['i', 'g', 'e']
```
Even though you give indices outside the list's scope like in the 2nd and 3rd last examples, they don't throw errors. Interesting to note.

An example of list assignment:
```python
fruits = ['apple', 'banana', 'peach', 'kiwi']
salad = fruits
fruits[0] = 'orange'
print(fruits)   # ['orange', 'banana', 'peach', 'kiwi']
print(salad)    # ['orange', 'banana', 'peach', 'kiwi']
```
This happens because copying a list this way still makes it so that they access the same memory location. An analogy is, a person has a name but also a nickname. When you say "`Name`, walk around", `Nickname` also moves around.

The reasoning behind this decision, according to Gabor, is to save memory. This becomes relevant for very large (and realistic) lists. Say a list has a million entries. When you do an assignment, you don't want there to be two million-length lists.

Workaround:
```python
fruits = ['apple', 'banana', 'peach', 'kiwi']
salad = fruits[:] # You copy the list by "slicing" the entire original list
fruits[0] = 'orange'
print(fruits)   # ['orange', 'banana', 'peach', 'kiwi']
print(salad)    # ['apple', 'banana', 'peach', 'kiwi']
```
This is not perfect:
```python
fruits = ['apple', ['banana', 'peach'], 'kiwi']
print(fruits)        # ['apple', ['banana', 'peach'], 'kiwi']
print(fruits[0])     # apple
print(fruits[1][0])  # banana

salad = fruits[:]

fruits[0] = 'orange'
fruits[1][0] = 'mango'

print(fruits)  # ['orange', ['mango', 'peach'], 'kiwi']
print(salad)   # ['apple', ['mango', 'peach'], 'kiwi']
```
The `:` approach is called making a shallow copy. The `deepcopy()` function is what you need in such cases:
```python
from copy import deepcopy

fruits = ['apple', ['banana', 'peach'], 'kiwi']
print(fruits)        # ['apple', ['banana', 'peach'], 'kiwi']
print(fruits[0])     # apple
print(fruits[1][0])  # banana

salad = deepcopy(fruits)

fruits[0] = 'orange'
fruits[1][0] = 'mango'

print(fruits)  # ['orange', ['mango', 'peach'], 'kiwi']
print(salad)   # ['apple', ['banana', 'peach'], 'kiwi']
```
<b>Internal Clock</b>
> Computers use a certain amount of bits for their "units of memory". For a long time, it was 32-bit, but now many PCs use 64-bit.
> For a PC, the internal clock stores the date. It does it by counting in seconds from 1 January 1970 (why???)
> The 32-bit internal clock will run out of capability to count after the year 2038. And so, many computers and/or programs that rely on the 32-bit nature will be screwed
> This is the [year 2038 problem/Y2K38](https://en.wikipedia.org/wiki/Year_2038_problem)

`join.py` has useful examples of combining information from lists. The CSV example is important.

<b>The `map()` function</b>:
Takes two arguments: another function itself, and a list.
It prints a list containing the results of the function output on each element of the given list.
Example:
```python
b = ["x", 2, "y"]

print(":".join(map(str, b)))       # x:2:y
# Using list comprehension
print(":".join(str(x) for x in b)) # x:2:y
```
`remove()` removes an element by value. `pop()` removes an element by index. You can also assign an empty list to a slice to remove multiple elements, like `list[1:3] = []`.

<b>FIFO</b>: First In, First Out - Like a queue \
<b>LIFO</b>: Last In, First Out - Like a stack

<b>Calculator exercise</b>: \
`2 + 3 * 7`\
A regular calculator, where the operators are "infixed" between the operands \
`+ * 2 3 7`\
A Polish calculator, here the operators are "prefixed" before the operands. \
`2 3 7 * +`\
A reverse Polish calculator. Note the suffixed operators, and how the operators are in a "reverse" direction. The idea is that it is implemented via a stack, so the last operator is used in the expression first (not calculated first, you follow BODMAS order for the actual calculation).

From the [Wikipedia](https://en.wikipedia.org/wiki/Reverse_Polish_notation), 
>The advantage of reverse Polish notation is that it removes the need for order of operations and parentheses that are required by [infix notation](https://en.wikipedia.org/wiki/Infix_notation "Infix notation") and can be evaluated linearly, left-to-right. For example, the infix expression (3 + 4) × (5 + 6) becomes 3 4 + 5 6 + × in reverse Polish notation.

You can supply a function to a list to act on the elements using the `key` argument inside `sort()` to sort the list according to some feature. The example below sorts the list in descending order purely by magnitude. 
```python
numbers = [7, 2, -4, 19, 8]
numbers.sort(key = abs, reverse = True)
print(numbers) # [19 8 7 -4 2]
```
The `sorted()` method creates a shallow copy of the list, leaving the original intact. 

Tuple: Immutable.

Go through the [tuples chapter](https://slides.code-maven.com/python/tuples.html), many new things.

The `sort_by_two_keys.py` example:
```python
print(sorted(planets1, key = lambda w: (len(w), w)))
```
Here, your `key` is the function that changes each element `w` in `planets1` to a tuple containing its length and value. So, like how tuples are sorted, the first tuple entry across all elements is checked, and then the second entry. Basically, you convert the elements to tuples to sort according to multiple criteria in some sequence.

Try doing more [exercises](https://slides.code-maven.com/python/exercise-dna-sequencing.html) from this chapter.

## Day 6: 22-05-25
You can, interestingly, open an image file or something else absurd in Notepad - it'll just show up as unreadable stuff.

Python Image Library (PIL): Installed as `pip install pillow` but you use it as `PIL` inside code.

<b>YAML file</b> /
Used as configuration files to store some kind of structure in a human-readable way. /
YAML and JSON are different. YAML is more human-readable; it's made for configuration files to be read and edited. JSON is more suitable to communicate data across applications

<i>File handler</i> /
A general name for processes that connect the program to the file location. It does not imply reading/loading the file into memory

`str.strip(arg)`: Strips a string of the chara `arg` and returns the modified string. By default when you don't pass an argument, the function removes whitespaces.

The `read_report.py` example is a good basic example at text file handling.

Why you should use the `with` method to open files: /
Often, people forget the `fh.close()` line, so files are kept open throughout. Here, open = connect to the file location, not load it. Your computer can only open so many files (is relevant when you want to loop over a large list of files or just open a ton of different files). The `with` way makes sure the file is closed after the required processing is done.

`str.rstrip("\n")`: Removes a new line by recognizing the newline escape sequence from the right side of the string. You don't need to have the character in your text file, it's internally recognized since a new line is encoded with that escape sequence.

For the `try except` block, you can circumvent having to give the specific error by using `except Exception`:
```python
filename = 'examples/files/unicorns.txt'

try: 
	with open(filename, 'r') as fh:
		lines = fh.readlines()
except Exception as err:
	print("There is an error in operation")
	print(err)					# [Errno 2] No such file or directory: 'examples/files/unicorns.txt'
	print(type(err).__name__)	# FileNotFoundError
```
A better example of this in `average_from_files.py`:
```python
import  sys

def main():
    for filename in sys.argv[1:]:
        try:
            do_some_stuff(filename)
        except Exception as err:
            print(f"trouble with '{filename}': Error: {err}")

def do_some_stuff(filename):
    with open(filename) as fh:
        total = 0
        count = 0
        for line in fh:
            number = float(line)
            total += number
            count += 1
        print("Average: ", total/count)

main()
```
If
1. a loaded file does not exist: You get a FileNotFoundError, reported as such
2. a loaded file is empty: the internal `for` loop in `do_some_stuff()` never executes, so you have a division by 0. That is a ZeroDivisionError, reported as such. 

It's good practice to read files into memory (`open(filename, "r")`), do some changes, and then read the file again for writing (`open(filename, "w"`) and then write out the entire changed file. When working on the physical disk itself, you can't shuffle data around. If you want to replace a word with a longer word, you need to read the file, write the file till just before the word, write the changed word, and then write out the rest of the file. But, shuffling around things can be done easily in the memory. So, it's more ideal to work on files in the memory (which is what `open(filename, "r")` does) rather than working on the physical disk itself (which is what `open(filename, "w")` does).

Using this kind of reading files with `open()` is called <i>low level reading</i>.

<b>Serializing/marshalling</b>: Converting data into a single dictionary for JSON.
