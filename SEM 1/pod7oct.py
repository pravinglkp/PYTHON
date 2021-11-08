x=input()
l=[x]
for i in range(len(x)):
    x=x[-1]+x[:-1]
    if x not in l:
        l.append(x)
print(len(l))
