d=input()
n=len(d)
k=int(input())
l=[]
l1=[]
for i in range(n):
    y=[]
    for j in range(i,n):
        y.append(j)
        if len(y)==n-k:break
    l.append(y)
print(l)
def remove(s,a):
    return ''.join(x for x in s if s.index(x)!=a)
for i in l:
    d1=d
    for j in i:
        d1=remove(d1,j)
    l1.append(d1)
print(l1)
