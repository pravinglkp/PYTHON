n=int(input())
n1=str(n)
n2=[int(i) for i in n1]
n3=[]
for i in n2:
    if i<5:
        n3.append(i)
    else:
        n3.append(9-i)
for i in range(len(str(n))):
    if n3[i]==0:
        n3[i]=9
        continue
    else:
        break
s=""
for i in n3:
    s=s+str(i)
print(s)
