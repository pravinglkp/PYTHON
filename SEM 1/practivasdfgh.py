x=int(input())
y=x
x1=[]
for i in range(1,len(str(x))+1):
    x2=y//(10**(len(str(x))-i))
    x1.append(x2)
    y=y%(10**(len(str(x))-i))
print(x1)
x1.remove(1)
print(x1)
