def gcd(a,b):
    if b==0:
        print(a,b)
        return a
    else:
        print(a,b)
        return gcd(b,a%b) 
a=int(input("input the value 1"))
b=int(input("input the value 2"))
GCD=gcd(a,b)
print("GCD is ",GCD)
