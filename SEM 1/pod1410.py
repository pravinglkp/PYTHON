p=int(input())
m,n=map(int,input().split())
n1=int(input())
l=[]
for i in range(n1):
    l.append(input())
me,ne=map(int,input().split())
for i in l:
    if i=='l' and n>0:m,n=m,n-1
    elif i=='r' and n<p-1:m,n=m,n+1
    elif i=='d' and m>0:m,n=m-1,n
    elif i=='u' and m<p-1:m,n=m+1,n
if me==m and ne==n:print('Win')
else:print("Loss")
