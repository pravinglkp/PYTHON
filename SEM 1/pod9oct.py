N=int(input())
s=[i for i in map(int,input().split(" "))]
a=0
a=a+s.count(4)
a3=s.count(3)
a1=s.count(1)
a2=s.count(2)
if a1==a3:
    a=a+a3
    a1=0
    a3=0
elif a1 != a3:
    if a3>a1:
        a=a+a1
        a3=a3-a1
        a=a+a3
        a1=0
        a3=0
    else:
        a=a+a3
        a1=a1-a3
        a3=0


    
if a2%2==0:
    a=a+a2//2
    a2=0
elif a2%2!=0:
    a=a+a2//2
    a2=a2%2
    if a1==1 or a1==2:
        a=a+1
        a1=0
        a2=0
        
a=a+a1//4
a1=a1%4


if 0<a1<4:
    a=a+1
if a2==1:
    a=a+1

        
    


        

print(a)

