A=input()
D={}
for i in A:
    f=A.count(i)
    D[i]=f
D2={}
for k,v in D.items():
    D2[v]=D2.get(v,[])
    D2[v].append(k)
print(sorted(D))
print(D2)
