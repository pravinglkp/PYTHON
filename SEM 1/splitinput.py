N=int(input())
s=[i for i in map(int,input().split())]
print(s)
count=0
for i in range(len(s)):
    count+=s[i]
count=count//4+count %4
print(count)
