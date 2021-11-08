Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="asd"
>>> a
'asd'
>>> a=int(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: 'asd'
>>> a
'asd'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(d)
NameError: name 'd' is not defined
>>> d="a"
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'a'
>>> d
'a'
>>> s="spam's"
>>> s
"spam's"
>>> s="s\np\ta\x00m"
>>> s
's\np\ta\x00m'
>>> s='''multiline'''
>>> s
'multiline'
>>> s='''....multiline...'''
>>> s
'....multiline...'
>>> s=b'sp\xc4m'
>>> s
b'sp\xc4m'
>>> s*3
b'sp\xc4msp\xc4msp\xc4m'
>>> s
"b'sp\xc4m'"
SyntaxError: multiple statements found while compiling a single statement
>>> s="b'sp\xc4m'"
>>> s
"b'spÄm'"
>>> s*3
"b'spÄm'b'spÄm'b'spÄm'"
>>> s[2]
's'
>>> s[4]
'Ä'
>>> s[1:4]
"'sp"
>>> len(s)
7
>>> s=b'sp\xc4m
SyntaxError: EOL while scanning string literal
>>> s=b'sp\xc4m'
>>> s
b'sp\xc4m'
>>> len(s)
4
>>> s="b'sp\xc4m'"
>>> s
"b'spÄm'"
>>> len(s)
7
>>> s=b'sp\xc4m'
>>> s
b'sp\xc4m'
>>> 
