n=int(input())
m=[[int(input()) for i in range(n)] for j in range(n)]
m1=[]
m2=[]
for  j in m[0]:m1.append(j)
for i in range(1,n-1):m1.append(m[i][len(m[i])-1])
for j in m[n-1][n::-1]:m1.append(j)
for i in range(n-2,0,-1):m1.append(m[i][0])
x=m1[0]
for i in range(0,len(m1)-3):
    if i%2==0:m1[i]=m1[i+2]
m1[len(m1)-2]=x
for i in range(n):
    if i==0:
        for j in m1[0:n]:print(j,end='\t')
    if 0<i<n-1:
        for j in range(n):
            if j==0:print(m1[-(i)],end='\t')
            if 0<j<n-1:print(m[i][j],end='\t')
            if j==n-1:print(m1[n-1+i],end='\t')
    if i==n-1:
        for j in m1[3*n-3:2*n-3:-1]:print(j,end='\t')
    print()
