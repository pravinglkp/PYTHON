c=[1,2,3,4,5,6]
d=[7,1,8,9,0,78,98,6]
print(c,d)
for i in c:
    if i in d:
	c.remove(i)
	d.remove(i)
print(c,d)
