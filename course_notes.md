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
```ruby
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
```ruby
print(f"{a} is greater than {b}")
``` 
is better than: 
```ruby
print(a + " is greater than " + b)
```

#### `sys.argv`: 
This is a list made from the command line input. The first element is the 0th element, and it refers to the script itself. Then, if you supply further arguments, it takes that in the list. For example, say you have `cli.py` which prints sys.argv and its first 3 elements. So,
```ruby
python cli.py a b c d
```
will print 
```ruby
['.\\cli.py', 'a', 'b', 'c']
.\cli.py
a
b
```
If my input instead only gave 1 entry like 
```ruby 
python cli.py a
```
it will throw an error