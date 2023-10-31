# Cheatsheet Tigerjython

## Syntax
- Functions and control structures are structured using indentation of code blocks
- Comments start with a '#'
- Python is case sensitive, `Name` and `name` are two different variables.

## Control Structures
### Loops
```python
repeat n:
	Block of statements

for i in range(n):
	Block of statements
	
for x in list:
	Block of statements

while condition:
	Block of statements
```

### Conditional Statements
```python
if condition:
	Block of Statements

if condition:
	Block of statements
else:
	Block of statements

if condition:
	Block of statements
elif condition:
	Block of statements
else:
	Block of Statements
```
#### Combine conditions (examples)
```python
if x < 10 and x != 5:
if x == 2 or x == 5:
```


## Functions
### Definition
```python
def name(parameter):   # parameters ony when required
	Block of statements
	return value   # the return statement and a value are optional.
```

### Call the function
```python
name(parameter)
```
Functions can have several parameters, the paranthesis are always required.

### Example
```python
def maximum(x, y):
	if x >= y:
		return x
	else:
		return y

x = 5
def f():
	global x   # a global variable can be changed inside a function if referrecd to
	x += 1
```

## Data Types
Variables have no type and are referencing/pointing to values. Each value has a defined type.


- `bool` Boolean value, either `True` or `False`
- `int` Integer, whole number Ex. 234, 56, 0, 1
- `float` Decimal number *Ex. 12.0 23.234 6.023e+12*
- `complex` complex number *complex(2, 3)*
- `str` string, text with characters *"Hello" 'See you'*
- `list` mutable list of values, array *[1,2,'Hi']*
- `tuple` immutable list of values, array *(1, 2, 'Hi')*
- `dictionary` mutable key-value pairs *{"Wan Chai":345, "North Point",34}*


## Mathematical Operations
- `+ - * /` Basic operations
- `// %` Integer division, Division *6//4 -> 1*, Remainder of integer division *6%4 -> 2*
- `**` to express exponents

Many mathematical functions are defined inside the module `math`, you need to import it when used.

```python
from math import sqrt, pi
print sqrt(3)
print("Pi =", pi)

import math
print math.sqrt(3)
print("Pi =", math.pi)
```

## Random numbers
You need to import the modul `random`, for example with `import random`

```python`
random.random()   # gets random float in the range 0 <= z < 1
random.randint(a, b)   # gets random int in the range of a <= z <= b
```


## Basic operations with lists
```python
li = [2, 4, 6]
li[0]   # -> 2 first element

range(5)   # -> [0, 1, 2, 3, 4]
range(5, 8)   # -> [5, 6, 7]
range(5, 12, 3)   # -> [5, 8, 11]

len(list)   # -> returns the number of Elements of list
list.append(Element)   # -> attaches Element at the end of the list
list.index(Element)   # -> returns the location of Element in the list with its index
list.insert(index Elementl)   # -> inserts Element at the position given by index
list.remove(Element)   # -> removes Element from the list
list.sort()   # -> sort the elements of the list
x in list   # -> returns `True` if x is in the list, otherwise `False`
```
