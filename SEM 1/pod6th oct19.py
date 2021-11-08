import sys
S,N=map(int,input().split(" "))
ld=[]
for i in range (1,N+1):
    Xi,Yi=map(int,input().split(" "))
    ld.append((Xi,Yi))
ld=sorted(ld)
for i in ld:
    Xi=i[0]
    Yi=i[1]
    if S>Xi:
        S=S+Yi
    else:
        print("NO")
        sys.exit()
print("YES")
