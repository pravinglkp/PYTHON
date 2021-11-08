import sys
k=int(input())
x=0
sf=1
while k!=1:
    x=x+1
    if k>1:
        k=k/x
    else:
        sf=-1
        print(sf)
        sys.exit()
if x%2==0:
    y=2
else:
    y=1
for i in range (y,x+1,2):
    sf=sf*i
print(sf)
