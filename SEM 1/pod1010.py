def fef(a,b):
    s=''
    for j in range(len(s1)):
        if j+1%2==1:
            s=s+chr(ord(a[j])+1)
        else:
            s=s+chr(ord(b[j])+1)
    return s


s1=input()
s2=input()
n=int(input())
l=[s1,s2]
i=0
print(l)
while i<n:
    x=fef(l[i],l[i+1])
    l.append(x)
    i=i+1
    print(l)
print(l[len(l)-1])
