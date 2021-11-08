import sys
N=input()
l=len(N)
if 0<int(N)<10000000:
    for i in range(1,l+1):
        a=int(N[0:i])
        if a%(l-i+1)==0:
           continue
        else:
           print("No")
           sys.exit()
    print("Yes")
