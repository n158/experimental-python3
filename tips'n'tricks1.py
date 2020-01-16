# Haven't tested this file, use on your own risk.
# Maybe there should be interactive menu for displaying ony of these tips on request.

# Top 5 best oneliners
import random

# N1. All possible combinations of a two lists
A = ['a', 'b', 'c', 'd', 'e', 'f']
B = [1, 2, 3, 4, 5, 6]
combinations = [(a, b) for a in A for b in B]
print(f'All combinations of {str(A)} and {str(B)}:\n{str(combinations)}')

# N2. Distance between two dots
dist = lambda w, v: (sum((wi - vi) ** 2 for wi, vi in zip(w, v))) ** .5

# N3. Vector multiplication by number
def scale(A, x): return [ai * x for ai in A]
scale([3, 4, 5], 2)

# N4. Vector addition by coordinates
A = [1, 2, 3]
B = [5, 8, 10]
def add(A, B): return [ai + bi for (ai, bi) in zip(A, B)]
print(f'Vector A = {str(A)}\nVector B = {str(B)}\nA + B = {str(add(A, B))}')

"""
N4. Matrix transpose
https://matrix.reshish.com/transpose.php
The algorithm of matrix transpose is pretty simple.
    A new matrix is obtained the following way: each [i, j] element of the new matrix gets the value of the [j, i] element of the original one.
    Dimension also changes to the opposite. For example if you transpose a 'n' x 'm' size matrix you'll get a new one of 'm' x 'n' dimension.
"""
a = [[1, 2, 3], [4, 5, 6]]
inverted_a = [list(i) for i in zip(*a)]
print(f'matrix a \t{str(a)}\ntransposed \t{str(inverted_a)}')

# N5. Choose one random element from a list
print(random.choice(['alpha', 'beta', 'gamma', 'delta', 'zeta']))


# https://www.techbeamers.com/top-10-python-coding-tips-for-beginners/
# Ten Essential Python Coding Tips for Beginners
# Python Tutorials | By Meenakshi Agarwal
# 3. Using enumerate() function.
# The enumerate() function adds a counter to an iterable object.
# An iterable is an object that has an __iter__ method which returns an iterator. It can accept sequential indexes starting from zero and raises an IndexError when the indexes are no longer valid.
# A typical example of the enumerate() function is to loop over a list and keep track of the index. For this, we could use a count variable. But Python gives us a nicer syntax for this using the enumerate() function.

# ------
# First prepare a list of strings
subjects = ('Python', 'Coding', 'Tips')

for i, subject in enumerate(subjects):
    print(i, subject)

# Output:
#    0 Python
#    1 Coding
#    2 Tips

# ------
# 4. The data type SET.
# The data type “set” is a kind of collection. It has been part of Python since version 2.4.
# A set contains an unordered collection of unique and immutable objects. It is one of the Python data types which is an implementation of the <sets> from the world of Mathematics.
# This fact explains, why the sets unlike lists or tuples can’t have multiple occurrences of the same element.
# If you want to create a set, use the built-in set() function with a sequence or another iterable object.

# ------
# *** Create a set with strings and perform search in set
objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects))

# Use of "in" keyword.
if "tips" in objects:
    print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
    print("These are the best Python coding tips not Java tips.")

# ** Output
#    {'python', 'coding', 'tips', 'for', 'beginners'}
#    5
#    These are the best Python coding tips.
#    These are the best Python coding tips not Java tips.

# ------
# *** Lets initialize an empty set
items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips")

print(items)

# ** Output
#    {'Python', 'coding', 'tips'}

# ------
# 5. Dynamic typing.
# In Java, C++, and other statically typed languages, you have to specify the data type of the function return value as well as the kind of each function argument. On the other hand, Python is a dynamically typed language. In Python, you don’t explicitly provide the data types. Based on the value you’ve assigned, Python keeps track of the datatype internally. Another good definition of dynamic typing is as follows.
# 
# “Names are bound to objects at run-time with the help of assignment statements. And it is possible to attach a name to the objects of different types during the execution of the program.”
#
# The following example demonstrates how a function can examine its arguments. And do different things depending on their types.

# ------
# Test for dynamic typing.
from types import *

def CheckIt (x):
    if type(x) == IntType:
        print("You have entered an integer.")
    else:
        print("Unable to recognize the input data type.")

# Perform dynamic typing test
CheckIt(999)
# Output:
# You have entered an integer.

CheckIt("999")
# Output:
# Unable to recognize the input data type.

# ------
# 7. Conditional Expressions.
# Python allows for conditional expressions. Here is an intuitive way of writing conditional statements in Python. Please follow the below example.

# ------
# make number always be odd
number = count if count % 2 else count - 1

# ------
# Call a function if the object is not None.
data = data.load() if data is not None else 'Dummy'
print("Data collected is ", data)


# https://www.techbeamers.com/essential-python-tips-tricks-programmers
# 30 Essential Python Tips and Tricks for Programmers
# Python Tutorials | By Meenakshi Agarwal


# Tip #2. Chaining of comparison operators.
# Aggregation of comparison operators is another trick that can come handy at times.

n = 10
result = 1 < n < 20
print(result)
# True

result = 1 >= n <= 9
print(result)
# False


# Tip #3. Use of Ternary operator for conditional assignment.
# Ternary operators are a shortcut for an if-else statement and also known as conditional operators.
# [on_true] if [expression] else [on_false]
# Here are a few examples which you can use to make your code compact and concise.
# The below statement is doing the same what it is meant to i.e. “assign 10 to x if y is 9, otherwise assign 20 to x“. We can though extend the chaining of operators if required.
# x = 10 if (y == 9) else 20
# Likewise, we can do the same for class objects.
# x = (classA if y == 1 else classB)(param1, param2)
# In the above example, classA and classB are two classes and one of the class constructors would get called.
# Below is one more example with a no. of conditions joining to evaluate the smallest number.

def small(a, b, c):
	return a if a <= b and a <= c else (b if b <= a and b <= c else c)
	
print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

#Output
#0 #1 #2 #3

# We can even use a ternary operator with the list comprehension.

print([m**2 if m > 10 else m**4 for m in range(50)])

# [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]


# Tip #4. Work with multi-line strings.
# The basic approach is to use backslashes which derive itself from C language.

multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)

# select * from multi_row where row_id < 5

# One more trick is to use the triple-quotes.

multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)

# select * from multi_row 
# where row_id < 5

# The common issue with the above methods is the lack of proper indentation. If we try to indent, it’ll insert whitespaces in the string.
# So the final solution is to split the string into multi lines and enclose the entire string in parenthesis.

multiStr = ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)

# select * from multi_row where row_id < 5 order by age


# Tip #6. Print the file path of imported modules.
# If you want to know the absolute location of modules imported in your code, then use the below trick.

import threading 
import socket

print(threading)
print(socket)

# <module 'threading' from '/usr/lib/python2.7/threading.py'>
# <module 'socket' from '/usr/lib/python2.7/socket.py'>


# Tip #7. Use the “_” operator in the interactive console.
# It’s a useful feature which not many of us know.
# In the Python console, whenever we test an expression or call a function, the result dispatches to a temporary name, _ (an underscore).
# >>> 2 + 1
# 3
# >>> _
# 3
# >>> print _
# 3
# 
# The “_” references to the output of the last executed expression.


# Tip #8. Dictionary/Set comprehensions.
# Like we use list comprehensions, we can also use dictionary/set comprehensions. They are simple to use and just as effective. Here is an example.

testDict = {i: i * i for i in range(10)} 
testSet = {i * 2 for i in range(10)}

print(testDict)
print(testSet)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

# Note - There is only a difference of <:> in the two statements.


# Tip #9. Debugging scripts.
# We can set breakpoints in our Python script with the help of the <pdb> module. Please follow the below example.

import pdb
pdb.set_trace()

# We can specify <pdb.set_trace()> anywhere in the script and set a breakpoint there. It’s extremely convenient.


# Tip #15. 3 ways to reverse string/list.
# 1.Reverse the list itself.

testList = [1, 3, 5]
testList.reverse()
print(testList)

# Output:
# [5, 3, 1]

# 2.Reverse while iterating in a loop.
for element in reversed([1, 3, 5]): print(element)

# Output:
# 5
# 3
# 1

# 3.Reverse a string/list in line using slicing.
print("Test Python"[::-1])
print([1, 3, 5][::-1])

# Output:
# "nohtyP tseT"
# [5, 3, 1]


# Tip #17. Use of enums in Python.
# We can use the following approach to create enum definitions.

class Shapes:
	Circle, Square, Triangle, Quadrangle = range(4)

print(Shapes.Circle)
print(Shapes.Square)
print(Shapes.Triangle)
print(Shapes.Quadrangle)

# Output:
# 0
# 1
# 2
# 3

# Tip #19. Unpack function arguments using the splat operator.
# The splat operator offers an artistic way to unpack arguments lists. Please refer the below example for clarity.

def test(x, y, z):
	print(x, y, z)

testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

# Output:
# x y z
# 1 2 3
# 10 20 30


Tip #20. Use a dictionary to store a switch.
We can make a dictionary store expressions.

calc = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y
}

print(calc['sum'](9, 3))
print(calc['subtract'](9, 3))

# Output:
# 12
# 6


# Tip #21. Calculate the factorial of any number in one line.

import functools
result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(3)
print(result)

# Output:
# 6


# Tip #24. Check the memory usage of an object.
# A 32-bit integer consumes 28-bytes in Python 3.5. To verify the memory usage, we can call the <getsizeof> method.

import sys
x = 1
print(sys.getsizeof(x))

# Output:
# 28


# Tip #25. Use __slots__ to reduce memory overheads.
# Have you ever observed your Python application consuming a lot of resources especially memory? Here is one trick which uses <__slots__> class variable to reduce memory overhead to some extent.

import sys
class FileSystem(object):

	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices


class FileSystem1(object):
	__slots__ = ['files', 'folders', 'devices']
	
	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices

print(sys.getsizeof(FileSystem))
print(sys.getsizeof(FileSystem1))

# Output:
# 1016
# 888

# Clearly, you can see from the results that there are savings in memory usage. But you should use __slots__ when the memory overhead of a class is unnecessarily large. Do it only after profiling the application. Otherwise, you’ll make the code difficult to change and with no real benefit.


# Tip #27. Create a dictionary from two related sequences.

t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict(zip(t1,t2)))

# Output:
# {1: 10, 2: 20, 3: 30}
