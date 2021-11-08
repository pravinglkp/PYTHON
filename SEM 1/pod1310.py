d,k='ccag',3;n=4
l=[]
for i in range(n):
    for j in range(i,i+k):
      s1=''+d[i:j+1]+d[j+n-k+1:]
      l.append(s1)
for i in l:
    if len(i)==k:print(i)
