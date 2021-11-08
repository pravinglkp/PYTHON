import sys
N=input()
l=len(N)
x=1
if 0<int(N)<10000000:
    for i in range(0,l):
        a=int(N[0:x])
        print(i,x,a,l-i)
        x=x+1
        if a%(l-i)==0:
           continue
        else:
           print("No")
           sys.exit()
    print("Yes")
