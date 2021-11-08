s1=input().rstrip()
s2=input().rstrip()
c=0
j=0
for i in range(len(s1)) :
    if j<len(s2) :
        if s1[i]==s2[j] :
            c+=1
            j+=1
if c==len(s2) :
    print('True')
else :
    print('False')
