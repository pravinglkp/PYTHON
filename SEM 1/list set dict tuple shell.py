Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> XX=[1,2,3,4,5,7,89,0,7]
>>> y=sort(XX)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    y=sort(XX)
NameError: name 'sort' is not defined
>>> Y=sorted(XX)
>>> Y
[0, 1, 2, 3, 4, 5, 7, 7, 89]
>>> X=['qwe','err','dft','cgv']
>>> X.sort()
>>> YY=X.sort()
>>> YY
>>> A=[1,2,3,4,5,6,7,8,9,0]
>>> A.sort()
>>> B=A.sort()
>>> B
>>> A.sort(min)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    A.sort(min)
TypeError: sort() takes no positional arguments
>>> a,b,c,d= X
>>> a
'cgv'
>>> b
'dft'
>>> c
'err'
>>> d
'qwe'
>>> A.insert(0,345)
>>> A
[345, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> A.insert(13,4,4,5,6,7)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    A.insert(13,4,4,5,6,7)
TypeError: insert() takes exactly 2 arguments (6 given)
>>> A.sort()
>>> A
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 345]
>>> Z=[4,6,7,3,0,5]
>>> sorted(Z)
[0, 3, 4, 5, 6, 7]
>>> Z
[4, 6, 7, 3, 0, 5]
>>> Z.sort()
>>> B=1,
>>> B
(1,)
>>> B=2,3
>>> B
(2, 3)
>>> B.clear()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    B.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> C=tuple(Z)
>>> C
(0, 3, 4, 5, 6, 7)
>>> M=list(C)
>>> M
[0, 3, 4, 5, 6, 7]
>>> N=([1,2],3)
>>> N.del([0][1])
SyntaxError: invalid syntax
>>> del(N[0][1])
>>> N
([1], 3)
>>> D=[(1,2),(3,4)]
>>> D
[(1, 2), (3, 4)]
>>> S=([(1, 2), (3, 4)])
>>> S
[(1, 2), (3, 4)]
>>> S[1]
(3, 4)
>>> S[1][1]
4
>>> W=(a=1,b=2,c=3,d=4,e=5,f=6)
SyntaxError: invalid syntax
>>> W=dict(a=1,b=2,c=3,d=4,e=5,f=6)
>>> W
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
>>> S=dict([(1, 2), (3, 4)])
>>> S
{1: 2, 3: 4}
>>> S=dict([(1, 2), (3, 4,5,6)])
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    S=dict([(1, 2), (3, 4,5,6)])
ValueError: dictionary update sequence element #1 has length 4; 2 is required
>>> S=dict([(1, [2,4]), (3,[5,6])])
>>> S
{1: [2, 4], 3: [5, 6]}
>>> S[1]
[2, 4]
>>> S[1][0]
2
>>> s[1][1]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s[1][1]
NameError: name 's' is not defined
>>> S[3][2]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    S[3][2]
IndexError: list index out of range
>>> S[3][1]
6
>>> 
S[3]=5
>>> S
{1: [2, 4], 3: 5}
>>> S[3]append(5)
SyntaxError: invalid syntax
>>> S.keys()
dict_keys([1, 3])
>>> S.values()
dict_values([[2, 4], 5])
>>> S.items()
dict_items([(1, [2, 4]), (3, 5)])
>>> for i in S:
	print(S[i][0])
	print(S[i][1])

2
4
Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    print(S[i][0])
TypeError: 'int' object is not subscriptable
>>> V={1:(1,2),2:(3,4)}
>>> for i in V:
	print(V[i][0])
	print(V[i][1])

1
2
3
4
>>> 
