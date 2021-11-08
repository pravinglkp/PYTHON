a=int(input())
b=int(input())
x=2
y=1
while x<=a and x<=b :
    if a%x==0 and b%x==0:
        y=y*x
        a=a/x
        b=b/x
        continue
    else:
        x=x+1
print("GCD",y)
y=y*a*b
print('LCM',int(y))
        
