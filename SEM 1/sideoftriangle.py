n=int(input())
c=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i+j+k==n and (i+j<=k or j+k<=i or i+k<=j):
                x=[i,j,k]
                x.sort()
                print(1,x)
                if x not in c:
                    print(2,x)
                    c.append(x)
print(len(c))
