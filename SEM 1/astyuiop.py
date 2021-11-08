x=int(input())
y=int(input())
x=str(x)
y=str(y)
for i in str(x):
    if i in str(y):
        x.replace(i,"")
        y.replace(i,"")
if x=="" and y=="" :
    x=1
    y=1
if y==0:
    print("-1")
else:
    x=int(x)
    y=int(y)
    z=x/y
    z=format(z,'0.2f')
print(z)
