x=input()
x=x.split()
s=input()
for i in range(len(x)):
    if x[i]==s:
        print(s,i)
