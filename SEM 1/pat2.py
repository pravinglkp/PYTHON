l=[]
s=True
x=''
while s:
    name=input()
    if name!='':
        l.append(name)
        if len(name)>len(x):
            x=name
    else:
        break
print(len(l))
print(x)
print(len(x))
