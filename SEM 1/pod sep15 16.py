import sys
N=input()
l=len(N)
x=1
for i in range(0,x):
    a=int(N[0:x])
    print(x)
    
    if a%(l-i-1):
       continue
    else:
       print("No")
       sys.exit()
print("Yes")
