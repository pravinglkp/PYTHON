n=int(input())
n1=list(map(int,input().split()))[:n:]
n2=[[n1[j] for j in range(i+1,n-i-1)] for i in range(n//2-1)];print(*n2)
n2=[]
l=[]
for i in range(n//2-1):
    for j in range(i+1,n-(i+1)):
        l.append(n1[j])
    print(l)
    n2.append(l)
    print(n2)
    l=[]

l=[len(i) for i in n2];print(*l)
avg=[sum(i)/len(i) for i in n2];print(*avg)
for i in range(len(avg)-1):
    for j in range(i+1,len(avg)):
        d=abs(avg[i]-avg[j])
        if d<1.2:
            print(*n2[i])
            print(*n2[j])
