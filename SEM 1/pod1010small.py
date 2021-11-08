s1,s2,n=input(),input(),int(input())
for z in range (n-2):
    s3=[chr(ord('a')+(ord(i)-ord('a'))%26) for i in [s1[j] if j%2==0 else s2[j] for j in range(len(s1))]]
    s1,s2=s2,s3
for i in s3:print(i,end='')


w,d=input(),int()
W=[chr(ord('a'))+(ord(i)-ord('a'))%26) for i in w]
for i in W:print(i,end='')
