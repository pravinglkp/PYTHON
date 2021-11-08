Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x='nsj'
>>> x.capitalize()
'Nsj'
>>> x.casefold()
'nsj'
>>> x.casfold()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.casfold()
AttributeError: 'str' object has no attribute 'casfold'
>>> x.casefold()
'nsj'
>>> x.swapcase(0,1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.swapcase(0,1)
TypeError: swapcase() takes no arguments (2 given)
>>> x.swapcase()
'NSJ'
>>> x="gcd"
>>> y=list(x)
>>> y
['g', 'c', 'd']
>>> z=join(y)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    z=join(y)
NameError: name 'join' is not defined
>>> z=''
>>> z.join(t)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    z.join(t)
NameError: name 't' is not defined
>>> z.join(y)
'gcd'
>>> my_string = 'hello'
my_string = my_string[-1] + my_string[:-1]
print(my_string)
SyntaxError: multiple statements found while compiling a single statement
>>> x="abcd"
>>> x=x[-1]+x[:-1]
>>> x
'dabc'
>>> 
 RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/pod7oct.py 
abcd
4
>>> x[2]="a"
Traceback (most recent call last):

  File "<pyshell#18>", line 1, in <module>
    x[2]="a"
TypeError: 'str' object does not support item assignment
>>> 
