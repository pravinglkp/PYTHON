Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=[1,2,3,4,5]
>>> num[::-1]
[5, 4, 3, 2, 1]
>>> num[1::-1]
[2, 1]
>>> num[:1:-1]
[5, 4, 3]
>>> name=['a','s','d']
>>> J=[num,name]
>>> j
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> J
[[1, 2, 3, 4, 5], ['a', 's', 'd']]
>>> J[1]
['a', 's', 'd']
>>> J[1][1]
's'
>>> J[1][0]
'a'
>>> id=12344
>>> name=a.sdff
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name=a.sdff
NameError: name 'a' is not defined
>>> name="a.dslk"
>>> mobile number = 2357748087
SyntaxError: invalid syntax
>>> mobnum=1234567890
>>> x=(name,mobnum)
>>> x
('a.dslk', 1234567890)
>>> D={}
>>> D[id]=x
>>> D
{12344: ('a.dslk', 1234567890)}
>>> D[id]
('a.dslk', 1234567890)
>>> x=12
>>> n="assd"
>>> m=123445
>>> D[x]=n,m
>>> D
{12344: ('a.dslk', 1234567890), 12: ('assd', 123445)}
>>> D[12]
('assd', 123445)
>>> D[12]{0}
SyntaxError: invalid syntax
>>> dD[12][0]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dD[12][0]
NameError: name 'dD' is not defined
>>> D[12][0]
'assd'
>>> D[12,1]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    D[12,1]
KeyError: (12, 1)
>>> D[12][1]
123445
>>> D[1][1]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    D[1][1]
KeyError: 1
>>> D[13]=23
>>> D
{12344: ('a.dslk', 1234567890), 12: ('assd', 123445), 13: 23}
>>> D[13]=45
>>> D
{12344: ('a.dslk', 1234567890), 12: ('assd', 123445), 13: 45}
>>> D[13]
45
>>> D{1}
SyntaxError: invalid syntax
>>> D(1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    D(1)
TypeError: 'dict' object is not callable
>>> X=[1,3,2,5,4]
>>> X.append(0)
>>> X
[1, 3, 2, 5, 4, 0]
>>> X.clear(1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    X.clear(1)
TypeError: clear() takes no arguments (1 given)
>>> X
[1, 3, 2, 5, 4, 0]
>>> X.clear()
>>> X
[]
>>> X.copy(D)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    X.copy(D)
TypeError: copy() takes no arguments (1 given)
>>> A=[1,2]
>>> X.copy(A)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    X.copy(A)
TypeError: copy() takes no arguments (1 given)
>>> A=X.copy()
>>> A
[]
>>> =[1,2,3,4,55,6,7]
SyntaxError: invalid syntax
>>> X=[1,2,3,4,5,6,7,8]
>>> .insert(2,5)
SyntaxError: invalid syntax
>>> 
>>> X.insert(2,5)
>>> X
[1, 2, 5, 3, 4, 5, 6, 7, 8]
>>> X.insert(6)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    X.insert(6)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> A=[1,2,3,100]
>>> X=A.copy()
>>> X
[1, 2, 3, 100]
>>> X.remove(2)
>>> X
[1, 3, 100]
>>> X.clear()
>>> X
[]
>>> X=[1,,2,3,4,5,6,7,8,9,89]
SyntaxError: invalid syntax
>>> X=[0,1,2,3,4,5,7,8,9,9]
>>> X.pop(2)
2
>>> X
[0, 1, 3, 4, 5, 7, 8, 9, 9]
>>> X.pop(9)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    X.pop(9)
IndexError: pop index out of range
>>> X.pop(2)
3
>>>  X.remove(9)
 
SyntaxError: unexpected indent
>>> X
[0, 1, 4, 5, 7, 8, 9, 9]
>>> X.remove(9)
>>> X
[0, 1, 4, 5, 7, 8, 9]
>>> X.append(4)
>>> X
[0, 1, 4, 5, 7, 8, 9, 4]
>>> X.remove(4)
>>> X
[0, 1, 5, 7, 8, 9, 4]
>>> X.append(5,6)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    X.append(5,6)
TypeError: append() takes exactly one argument (2 given)
>>> X.extend(5)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    X.extend(5)
TypeError: 'int' object is not iterable
>>> X.append(5)
>>> X
[0, 1, 5, 7, 8, 9, 4, 5]
>>> X.remove(5,5)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    X.remove(5,5)
TypeError: remove() takes exactly one argument (2 given)
>>> X.remove(5)
>>> X
[0, 1, 7, 8, 9, 4, 5]
>>> X.remove(5)
>>> X.pop()
4
>>> X
[0, 1, 7, 8, 9]
>>> del X[2::]
>>> X
[0, 1]
>>> del X[1]
>>> X
[0]
>>> X=[1,2,3,4,5344,6,6,7,7765,4,3]
>>> del X[6]
>>> X
[1, 2, 3, 4, 5344, 6, 7, 7765, 4, 3]
>>> del X[3]
>>> X
[1, 2, 3, 5344, 6, 7, 7765, 4, 3]
>>> del X[:3]
>>> X
[5344, 6, 7, 7765, 4, 3]
>>> del X[3:]
>>> X
[5344, 6, 7]
>>> del X[1:4]
>>> X
[5344]
>>> 
