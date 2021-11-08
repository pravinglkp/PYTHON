import re
V={}
Z={}
n=int(input())
for i in range (n):
    id=int(input())
    name=input()
    if not re.match("[A-Z a-z].[A-Z a-z]+$",name):
       break
    mobile=input()
    if not  mobile[0]!=0 and len(mobile)==10 :
        print("invalid")
        break
    V[id]=(name,mobile)
for i in V.keys():
	if i%3==0 and i%4!=0:
	  Z[i]=V[i]
	  print(Z)
for i in Z:
    print(Z[i][0])
    print(Z[i][1])
    print(i,Z[i])
    
