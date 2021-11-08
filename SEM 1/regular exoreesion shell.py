Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re

str = "hello world"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", str)
print(x)
SyntaxError: multiple statements found while compiling a single statement
>>> import re
>>> str="hello world"
>>> re.findall("he..o",str)
['hello']
>>> re.match("he..o",str)
<re.Match object; span=(0, 5), match='hello'>
>>> x=findall("he.l",str)
if x:
	print("a",x)
else:
	print(b)
	
SyntaxError: multiple statements found while compiling a single statement
>>> x=findall("he.l",str)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x=findall("he.l",str)
NameError: name 'findall' is not defined
>>> x=re.findall("he.l",str)
>>> if x:
	print("a",x)
else:
	print(b)

a ['hell']
>>> str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

SyntaxError: multiple statements found while compiling a single statement
>>> str = "The rain in Spain falls mainly in the plain!"
>>> x = re.findall("aix+", str)
>>> x
[]
>>> x = re.findall("ai+", str)
>>> x
['ai', 'ai', 'ai', 'ai']
>>> x = re.findall("aix*", str)['ai', 'ai', 'ai', 'ai']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x = re.findall("aix*", str)['ai', 'ai', 'ai', 'ai']
TypeError: list indices must be integers or slices, not tuple
>>> x = re.findall("aix*", str)
>>> x
['ai', 'ai', 'ai', 'ai']
>>> x = re.findall("aix.*", str)
>>> x
[]
>>> x = re.findall("aix.+", str)
>>> x
[]
>>> x = re.findall("ai.+", str)
>>> x
['ain in Spain falls mainly in the plain!']
>>> x = re.findall("ai.*", str)
>>> x
['ain in Spain falls mainly in the plain!']
>>> x = re.findall("aix..*", str)
>>> x
[]
>>> x = re.findall("aix..+", str)
>>> x
[]
>>> x = re.findall("ai..*", str)
>>> x
['ain in Spain falls mainly in the plain!']
>>> x = re.findall("ai..+", str)
>>> x
['ain in Spain falls mainly in the plain!']
>>> x = re.findall("ai..", str)
>>> x
['ain ', 'ain ', 'ainl', 'ain!']
>>> x = re.findall("ai.", str)
>>> x
['ain', 'ain', 'ain', 'ain']
>>> x = re.findall("ai{2}", str)
>>> x
[]
>>> x = re.findall("ai{1},,str)
	       
SyntaxError: EOL while scanning string literal
>>> x = re.findall("ai{1}", str)
>>> x
['ai', 'ai', 'ai', 'ai']
>>> x = re.findall("ai.{1}", str)
>>> x
['ain', 'ain', 'ain', 'ain']
>>> x = re.findall("ai.{2}", str)
>>> x
['ain ', 'ain ', 'ainl', 'ain!']
>>> x = re.findall("ai..{2}", str)
>>> x
['ain i', 'ain f', 'ainly']
>>> x = re.findall("ai.{2}.{2}", str)
>>> x
['ain in', 'ain fa', 'ainly ']
>>> x = re.findall("ai.{2}f", str)
>>> x
['ain f']
>>> 
