import sys
n=int(input())
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
p=int(input())
q=p
T=1
c=0
while T!=0:
    for i in l:
        if i[0]==p:
            c=c+1
            p=i[1]
            if i[1]!=q:
                continue
            else:
                T=0
                break
    else:
        T=0
print(c)
