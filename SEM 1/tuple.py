Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=('T,19,30 J,20,90 K,17,91 M,34,67 G,67,89')
>>> s
'T,19,30 J,20,90 K,17,91 M,34,67 G,67,89'
>>> tup1=[tuple(x.split(',') for x in s.split()]
      
SyntaxError: invalid syntax
>>> tup1=[tuple(x.split(',')) for x in s.split()]
>>> tup1
[('T', '19', '30'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('G', '67', '89')]
>>> sorted(tup1,key=lambda x:(x[0],x[1],x[2]))
[('G', '67', '89'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('T', '19', '30')]
>>> 
KeyboardInterrupt
>>> sorted(tup1,key=lambda x:(x[1],x[0],x[2]))
[('K', '17', '91'), ('T', '19', '30'), ('J', '20', '90'), ('M', '34', '67'), ('G', '67', '89')]
>>> tup1
[('T', '19', '30'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('G', '67', '89')]
>>> orted(tup1,key=lambda x:(x[2],x[1],x[0]))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    orted(tup1,key=lambda x:(x[2],x[1],x[0]))
NameError: name 'orted' is not defined
>>> sorted(tup1,key=lambda x:(x[2],x[1],x[0]))
[('T', '19', '30'), ('M', '34', '67'), ('G', '67', '89'), ('J', '20', '90'), ('K', '17', '91')]
>>> tup1.append(('T','20','29'))
>>> tup1
[('T', '19', '30'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('G', '67', '89'), ('T', '20', '29')]
>>> sorted(tup1,key=lambda x:(x[0],x[1],x[2]))
[('G', '67', '89'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('T', '19', '30'), ('T', '20', '29')]
>>> sorted(tup1,key=lambda x:(x[0],x[2],x[1]))
[('G', '67', '89'), ('J', '20', '90'), ('K', '17', '91'), ('M', '34', '67'), ('T', '20', '29'), ('T', '19', '30')]
>>> 
