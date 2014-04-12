# Keywords Review #2
#
# Most explanations came form PyDoc but some came from http://zetcode.com/lang/python/keywords/ as well.

# and
# a boolean operator that evaluates to True is both LHS and RHS are True
print "True and True == True? %r" % (True and True)
print "True and False == False? %r" % (True and False)

# print - output a string to stdout
# del   - deletes a variable from the namespace
# if	- a conditional test that executes the statements within if True
# else	- the catch all statement for an if-statement
name = "exists"
print "before del"
if 'name' in locals():
	print "name exists"
else:
	print "name does not exist"
del name
print "after del"
if 'name' in locals():
	print "name exists"
else:
	print "name does not exist"

# from
# import _from_ a module
from sys import argv

# not
# boolean operator to negate
print "True is %r" % True
print "not(True) is %r" % (not(True))
print "False is %r" % False
print "not(False) is %r" % (not(False))

# elif	- multiple if-statement
# while - a loop that evaluates the statements within if the statement is True
while_loop = True
while_loop_count = 0
print "Will loop 10 times until loop count is 10 or user says cancel."
while while_loop:
	if while_loop_count < 10:
		while_loop_prompt = "Loop #%d Contunue? [Y/n] " % (while_loop_count + 1)
		while_loop_input = raw_input(while_loop_prompt)
		if while_loop_input == 'n':
			while_loop = False
	else:
		while_loop = False
	while_loop_count += 1

if while_loop_count == 1:
	print "Looped 1 time."
elif while_loop_count == 2:
	print "Looped 2 times."
else:
	print "Looped %d times." % while_loop_count 

# import - find a module and import the symbols
# as 	 - defines an alias for an imported module
import random as rnd
print "rnd.randint(1, 10) = %r" % rnd.randint(1,10)

# def    - define a function
# global - required in order to modify variables outside of a function
x = 10
def test_no_global():
#	global x
	x = 0
	print "inside: x = %r" % x
print "Without \"global\""
test_no_global()
def test_global():
	global x
	x = 0
	print "inside: x = %r" % x
print "outside: x = %r" % x
print "With \"global\""
test_global()
print "outside: x = %r" % x

# or
# boolean operator that evaluates to true if either LHS or RHS is True
print "True or False = %r" % (True or False)

# with
# http://docs.python.org/whatsnew/2.6.html#pep-343-the-with-statement
# groups commands that normally execute together and have a cleanup section
# the following will always call close() on f because it is defined
# as the __exit__() method for this object.
# with open('output.txt', 'w') as f:
#     f.write('Hi there!')

# assert
# ? a convenient way to insert debug assertions

# pass
# http://docs.python.org/2/tutorial/controlflow.html#pass-statements
# the pass statement does nothing, it can be used when a statement is required
# syntactically but the program requires no action.
def busy_wait():
	pass # busy-wait loop

print '== yield =='
# yield	- like return but function will return a generator
# http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained
# in	- operator to test for collectin membership
genenable = True
def gen():
	print 'Observe that this is not printed when first called'
	if genenable:
		yield 1
		yield 2
		yield 3
	else:
		yield 0
mygen = gen();
raw_input('Print 3 times:')
for i in mygen:
	print(i)
raw_input('Print 0 times now that it is empty:')
for i in mygen:
	print(i)
raw_input('Print 1 time:')
genenable = False
mygen = gen()
for i in mygen:
	print(i)

print '== break =='
# break out of a loop

for break_i in range(0,6):
	print "%i, " % break_i,
	if break_i == 3:
		print "break!"
		break;

# exec
# dynamically execute a string, open file object, a code object, or a tuple
# it supports an optional scope parameter as well
exec_string = "print 'exec string'"
exec(exec_string)

# class
# a definition of a logical grouping of variables and functions
class MyClass:
	"""A simple example class"""
	i = 12345
	def f(self):
		return self.i
# instanciate
myclass = MyClass()
# call a method in MyClass
print 'myclass.f() = %d' % myclass.f()

print '== try/except =='
# try		- defines a clause that has clean-up actions if an exception occurs
# except	- clause to execute in the event of an exception
# raise		- throw an exception
# finally	- a clause that is always executed after a try statment and before any unhandled exception
# http://docs.python.org/2/tutorial/errors.html#handling-exceptions
while True:
	try:
		x_try = int(raw_input('Enter an non-integer (0 to break): '))
		if ( 0 == x_try ):
			break
		else:
			raise
	except ValueError:
		print 'Oops! That was not an integer. Try again...'
	except:
		print 'Something else raised an exception! Try again...'
	finally:
		print 'executing finally clause'

# continue	- end current iteration in a loop but don't break out
for i in range(0,5):
	if ( 3 == i ):
		continue
	print i

# is	- compare object identify
a = MyClass()
b = a
print 'a is b ? %r' % (a is b)

# return
# return execution to the calling function and optionally return an object from the callee
def test_return():
	return 10
print "the function returned: %r" % test_return()

# for
# loop a specified number of times
print "loop 6 times: ",
for i in range(0,6):
	print "%d, " % i,
print ""

# lambda
# lambda expressions formm anonymous functions
mul2 = lambda a, b: a * b
add2 = lambda a, b: a + b
print "mul2(2, 3) =", mul2(2, 3)
print "add2(2, 3) =", add2(2, 3)

## Data Types

# True, False
# boolean
print "bool(True) =", bool(True)
print "bool(False) =", bool(False)
print "bool(\"text\") =", bool("text")
print "bool(\"\") =", bool("")
print "bool(' ') =", bool(' ')
print "bool(0) =", bool(0)
print "bool() =", bool()
print "bool(3) =", bool(3)
print "bool(None) =", bool(None)

# None
# the null object (not known or empty)
def fNone():
	pass
print fNone()

# strings
# ASCII 
ascii_string = "0123456789abcdefghijklmnop"
print ascii_string

# numbers
# 1, 2, 3, 4, ...
num_int = 2
print "int", num_int

# floats
# 1.0, 1.1, ... 
num_float = 1.1
print "float", num_float
print "int * float", num_float * num_int

# lists
list_ex = [ 1, 2, 3, 'four']
print "list[ ",
for list_i in list_ex:
	print "%r " % list_i,
print "]"


## String Escape Sequences

# %d
# %i
# %u
# signed integer decimal

# %o
print "octal value: %o is decimal %d" % (0100, 0100)

# %x
print "signed hex (lowercase): %x" % 0xFF

# %X
print "signed hexidecimal (uppercase): %X" % 0xff

# %e
print "floating point exponential (lowercase): %e" % 0.00000000012

# %E
print "floating point exponential (uppercase): %E" % 0.00000000012

# %f
print "floating point decimal: %f" % 123.45

# %F
print "floating point decimal: %F" % 123.45

# %g
print "floating point exponental if exponent < -4 or > precision, o.w. decimal (lowercase): %g" % 1.2e-4

# %G
print "floating point exponental if exponent < -4 or > precision, o.w. decimal (uppercase): %G" % 1.2e-5

# %c
print "single character: %c" % 'c'

# %r
print "string (converts using repr()): %r" % True

# %s
print "string (converts using str()): %s" % oct(011)

# %%
print "percent character: %%"

## Operators

# Arithmetic

# +
print "Addition %d" % (1 + 2)

# -
print "Subtraction %d" % (3 - 2)

# *
print "Multiplication %d" % (2 * 3)

# **
print "Exponent %d" % (2**3)

# /
print "Division %d" % (9 / 3)

# //
print "Floor Division %d" % (9 // 2)

# %
print "Modulus %d" % (9 % 2)

# Comparison

# <
print "Less than %r" % (1 < 2)

# >
print "Greater than %r" % (1 > 2)

# <=
print "Less than or equal %r" % (1 <= 2)

# >=
print "Greater than or equal %r" % (1 >= 2)

# ==
print "Equal to %r" % (1 == 2)

# !=
# <>
print "Not equal %r" % (1 != 2)

# Special Syntax

# ()
# function(arguments)

# []
# list[]

# {}
# dictionary {'key':'value'} pair

# @
# Decorator - used to modify a callable object definition
# http://www.artima.com/weblogs/viewpost.jsp?thread=240808
class myDecorator(object):
	def __init__(self, f):
		print "Inside myDecorator.__init__()"

	def __call__(self):
		print "Inside myDecorator.__call__()"

@myDecorator
def some_function():
	print "this is equivalent to some_function = myDecorator(some_function)"

some_function()

# ,
# function(argument, delimiter)

# :
# sub-clause (loop) or slice notation [1:5] (1 to 4 inclusive)

# .
# decimal point

# =
# assignment

# ;
# separator; between; statements

# Assignment Operators

a = 10
print "a = 10"

# +=
a += 1
print "Add AND assign", a 

# -=
a -= 1
print "Subtract AND assign", a

# *=
a *= 4
print "Multiply AND assign", a

# /=
a /= 2
print "Divide AND assign", a

# //=
a //= 4
print "Floor divide AND assign", a

# %=
a %= 3
print "Modulus AND assign", a

# **=
a **= 3
print "Exponent AND assign", a
