Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(1,2,3,4,5,6,7,8,9,0)
>>> tup[4]
5
>>> tup[5]=678
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tup[5]=678
TypeError: 'tuple' object does not support item assignment
>>> tup.count(5)
1
>>> tup.index(5)
4
>>> tup[10]=11
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tup[10]=11
TypeError: 'tuple' object does not support item assignment
>>> len(tup)
10
>>> max(tup)
9
>>> sum(tup)
45
>>> for i in range(0,len(tup)):print(tup[i])

1
2
3
4
5
6
7
8
9
0
>>> tup2=(1,2)
>>> tup=tup1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tup=tup1
NameError: name 'tup1' is not defined
>>> tup1=tup
>>> print(tup1)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
>>> tup1=tup2
>>> tup1
(1, 2)
>>> 
